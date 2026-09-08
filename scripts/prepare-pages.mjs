import {cp, mkdir, readdir, rm, writeFile} from 'node:fs/promises';
import path from 'node:path';

const basePath = process.env.ATLAS_PAGES_BASE_PATH ?? '/cognitive-atlas';
if (!/^\/[a-zA-Z0-9_-]+(?:\/[a-zA-Z0-9_-]+)*$/.test(basePath)) {
  throw new Error('Pages requires a project base path such as /cognitive-atlas');
}
const destination = path.resolve('out/pages');
await rm(destination, {recursive: true, force: true});
await mkdir(destination, {recursive: true});
await cp(path.join('dist/client', basePath.slice(1)), destination, {recursive: true});
await cp('dist/client/404.html', path.join(destination, '404.html'));
await writeFile(path.join(destination, '.nojekyll'), '');
const forbidden = ['server', '.env', '.git', '.openai'];
for (const name of await readdir(destination)) {
  if (forbidden.includes(name)) throw new Error(`Unexpected private/build directory: ${name}`);
}
console.log(`GitHub Pages files prepared in out/pages for ${basePath}/`);
