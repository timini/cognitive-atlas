/** Publish only the validated static artifact, retaining gh-pages branch history. */
import {spawnSync} from 'node:child_process';
import {cp, mkdtemp, readdir, rm, writeFile} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import path from 'node:path';

function run(command, args, options = {}) {
  const result = spawnSync(command, args, {encoding: 'utf8', ...options});
  if (result.status !== 0) throw new Error(result.stderr || `${command} failed`);
  return result.stdout.trim();
}
const root = process.cwd();
const remote = run('git', ['remote', 'get-url', 'origin']);
const repo = run('gh', ['repo', 'view', '--json', 'nameWithOwner', '--jq', '.nameWithOwner']);
const sourceCommit = run('git', ['rev-parse', 'HEAD']);
if (run('git', ['status', '--porcelain'])) throw new Error('Commit source changes before publishing');
const artifact = path.join(root, 'out/pages');
if (!(await readdir(artifact)).includes('index.html')) throw new Error('Run npm run build:pages first');
const staging = await mkdtemp(path.join(tmpdir(), 'cognitive-atlas-pages-'));
try {
  const git = (...args) => run('git', args, {cwd: staging});
  git('init', '--quiet');
  git('remote', 'add', 'origin', remote);
  if (git('ls-remote', '--heads', 'origin', 'gh-pages')) {
    git('fetch', '--depth=1', 'origin', 'gh-pages');
    git('checkout', '-B', 'gh-pages', 'FETCH_HEAD');
    for (const name of await readdir(staging)) {
      if (name !== '.git') await rm(path.join(staging, name), {recursive: true, force: true});
    }
  } else {
    git('checkout', '--orphan', 'gh-pages');
  }
  await cp(artifact, staging, {recursive: true});
  await writeFile(path.join(staging, 'build-info.json'), JSON.stringify({source_commit: sourceCommit, repository: repo, generated_at: new Date().toISOString()}, null, 2)+'\n');
  git('add', '--all');
  git('commit', '-m', `Publish static atlas from ${sourceCommit.slice(0, 12)}`);
  console.log(git('push', 'origin', 'HEAD:gh-pages'));
  run('gh', ['api', '--method', 'PUT', `repos/${repo}/pages`, '--input', '-'], {
    input: JSON.stringify({build_type: 'legacy', source: {branch: 'gh-pages', path: '/'}}),
  });
  console.log(run('gh', ['api', `repos/${repo}/pages`, '--jq', '.html_url']));
  console.log('Source branch configured; check the GitHub Pages build before claiming it is live.');
} finally {
  await rm(staging, {recursive: true, force: true});
}
