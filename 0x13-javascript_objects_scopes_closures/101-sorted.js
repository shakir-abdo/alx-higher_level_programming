#!/usr/bin/node
const dict = require('./101-data').dict;

const myValues = Object.values(dict);
const myList = Object.entries(dict);
const myValuesUniq = [...new Set(myValues)];
const newDict = {};
for (const j in myValuesUniq) {
  const list = [];
  for (const k in myList) {
    if (myList[k][1] === myValuesUniq[j]) {
      list.unshift(myList[k][0]);
    }
  }
  newDict[myValuesUniq[j]] = list;
}
console.log(newDict);
