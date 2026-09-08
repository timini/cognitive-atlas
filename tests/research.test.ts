import assert from 'node:assert/strict';
import {test} from 'node:test';
import {histogram, interpolate, pathFor, formatNumber, renderPrompt, type Place} from '../lib/research.ts';

test('histogram preserves every sample including the upper boundary',()=>{
  const bins=histogram([100,100,200,300,400,500]);
  assert.equal(bins.reduce((n,b)=>n+b.count,0),6);
  assert.equal(bins.at(-1)?.count,1);
});
test('constant samples produce a single bin, without artificial variance',()=>{
  assert.deepEqual(histogram([100,100,100]),[{low:100,high:100,count:3}]);
  assert.deepEqual(histogram([]),[]);
});
test('map endpoints reproduce source and inferred locations exactly',()=>{
  assert.deepEqual(interpolate([1,2],[7,8],0),[1,2]);
  assert.deepEqual(interpolate([1,2],[7,8],1),[7,8]);
  assert.deepEqual(interpolate([1,2],[7,8],.5),[4,5]);
  assert.equal(pathFor([[1,2]],[[7,8]],1),'M7.000,8.000Z');
});
test('missing statistics do not render as zero',()=>{
  assert.equal(formatNumber(null),'—');
  assert.equal(formatNumber(Number.NaN),'—');
  assert.equal(formatNumber(0),'0');
});

test('translated prompt inspection preserves canonical names and pair order',()=>{
  const a={capital_name:'Brasília', country_name:'Brazil'} as Place;
  const b={capital_name:'Tokyo', country_name:'Japan'} as Place;
  const template='بين {city_a}، {country_a} و{city_b}، {country_b}. استخدم الأرقام 0–9.';
  assert.equal(renderPrompt(template,a,b),'بين Brasília، Brazil وTokyo، Japan. استخدم الأرقام 0–9.');
});
