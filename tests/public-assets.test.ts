import assert from 'node:assert/strict';
import {test} from 'node:test';
import {publicAsset} from '../lib/public-assets.ts';

test('research assets keep the hosting prefix for fetches and downloads', () => {
  assert.equal(publicAsset('/data/experiments.json'), '/data/experiments.json');
  assert.equal(publicAsset('/data/experiments.json', '/cognitive-atlas'), '/cognitive-atlas/data/experiments.json');
  assert.equal(publicAsset('/data/run/responses.csv', '/cognitive-atlas/'), '/cognitive-atlas/data/run/responses.csv');
  assert.equal(publicAsset('data/comparisons.json', '/'), '/data/comparisons.json');
});
