import assert from 'node:assert/strict';
import {readFile, readdir, stat} from 'node:fs/promises';
import {createServer} from 'node:http';
import path from 'node:path';

const root = path.resolve('out/pages');
const base = (process.env.ATLAS_PAGES_BASE_PATH ?? '/cognitive-atlas') + '/';
const html = await readFile(path.join(root, 'index.html'), 'utf8');
assert.match(html, /Cognitive Atlas/);
assert.equal(await readFile(path.join(root, '.nojekyll'), 'utf8'), '');
const references = [...html.matchAll(/(?:src|href)="([^"]+)"/g)].map(m => m[1]).filter(u => u.startsWith('/'));
assert(references.length > 0);
for (const ref of references) {
  assert(ref.startsWith(base), `Asset escaped project prefix: ${ref}`);
  await stat(path.join(root, ref.slice(base.length).split('?')[0]));
}
let files = 0;
async function verify(dir) {
  for (const entry of await readdir(dir, {withFileTypes: true})) {
    const file = path.join(dir, entry.name);
    if (entry.isDirectory()) { await verify(file); continue; }
    files++;
    const content = await readFile(file);
    assert(!/AIza[\w-]{30,}|github_pat_[A-Za-z0-9_]+|ghp_[A-Za-z0-9]{30,}/.test(content.toString()), `Potential secret in ${file}`);
    if (entry.name.endsWith('.css')) {
      for (const match of content.toString().matchAll(/url\(["']?(\/[^)"']+)/g)) {
        assert(match[1].startsWith(base), `CSS asset escaped project prefix: ${match[1]}`);
        await stat(path.join(root, match[1].slice(base.length).split('?')[0]));
      }
    }
  }
}
await verify(root);
// Exercise the actual project prefix on a local HTTP server, without browser QA.
const server = createServer(async (req, res) => {
  const pathname = new URL(req.url, 'http://localhost').pathname;
  if (!pathname.startsWith(base)) { res.writeHead(404).end(); return; }
  const suffix = pathname.slice(base.length) || 'index.html';
  const file = path.resolve(root, suffix);
  if (!file.startsWith(root + path.sep)) { res.writeHead(404).end(); return; }
  try {
    if (req.method === 'HEAD') {
      res.writeHead(200, {'Content-Length': (await stat(file)).size}).end();
    } else res.writeHead(200).end(await readFile(file));
  } catch { res.writeHead(404).end(); }
});
await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
const origin = `http://127.0.0.1:${server.address().port}`;
try {
  assert.equal((await fetch(origin + base)).status, 200);
  const index = await (await fetch(origin + base + 'data/experiments.json')).json();
  const sourceIndex = JSON.parse(await readFile('public/data/experiments.json', 'utf8'));
  assert.deepEqual(index, sourceIndex);
  const paperIndex = JSON.parse(await readFile('paper/experiment-index.json', 'utf8'));
  const publishedIds = new Set(index.map(e => e.id));
  assert(paperIndex.every(e => publishedIds.has(e.id)), 'Current paper experiments must remain selectable');
  assert(index.length === 3 && index.every(e => e.capital_count === 100));
  const publication = await (await fetch(origin + base + 'paper/publication.json')).json();
  assert.equal(publication.completed_answers, 148500);
  for (const file of ['paper/cognitive-atlas-paper.pdf','paper/reproduction.zip']) assert.equal((await fetch(origin + base + file, {method:'HEAD'})).status, 200);
  const languages = new Set();
  for (const entry of index) {
    const response = await fetch(origin + base + entry.url.replace(/^\//, ''));
    assert.equal(response.status, 200);
    const data = await response.json();
    if (data.experiment.prompt_family) languages.add(data.experiment.language);
    const folder = entry.url.replace('/result.json', '');
    const csvResponse = await fetch(origin + base + folder.replace(/^\//, '') + '/responses.csv', {method: 'HEAD'});
    assert.equal(csvResponse.status, 200);
    assert.equal(Number(csvResponse.headers.get('content-length')), (await stat(path.join(root, folder.replace(/^\//, ''), 'responses.csv'))).size);
  }
  assert.deepEqual([...languages].sort(), ['ar','en','zh']);
  const comparison = await (await fetch(origin + base + 'data/comparisons.json')).json();
  const sourceComparison = JSON.parse(await readFile('public/data/comparisons.json', 'utf8'));
  assert.deepEqual(comparison, sourceComparison);
  assert(comparison.language_cohorts.length >= 1);
  const inferenceResponse = await fetch(origin + base + 'data/language-inference.json');
  assert.equal(inferenceResponse.status, 200);
  const inference = await inferenceResponse.json();
  const exportIds = new Set(index.map(e => e.id));
  for (const cohort of inference.cohorts) {
    assert(cohort.export_ids.every(id => exportIds.has(id)));
    const audit = await fetch(origin + base + cohort.report_url.replace(/^\//, ''));
    assert.equal(audit.status, 200);
    assert.equal((await audit.json()).complete_pairs, cohort.complete_pairs);
  }
  for (const cohort of inference.map_cohorts ?? []) {
    assert(cohort.export_ids.every(id => exportIds.has(id)));
    const response = await fetch(origin + base + cohort.report_url.replace(/^\//, ''));
    assert.equal(response.status, 200);
    assert.equal((await response.json()).total_pairs, cohort.total_pairs);
  }
  for (const ref of references) assert.equal((await fetch(origin + ref)).status, 200);
  console.log(`Verified ${files} static files, ${index.length} experiments, ${languages.size} languages, CSV downloads, comparison data, and project-prefixed assets.`);
} finally {
  server.closeAllConnections();
  await new Promise(resolve => server.close(resolve));
}
