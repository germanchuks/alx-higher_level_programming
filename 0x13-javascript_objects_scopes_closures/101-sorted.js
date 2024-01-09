#!/usr/bin/node
// Imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

const dict = require('./101-data.js').dict;

const allValues = Object.values(dict);
const uniqValues = [...new Set(allValues)];

const newDict = {};

for (const key in dict) {
  const value = dict[key];

  if (uniqValues.includes(value)) {
    if (!newDict[value]) {
      newDict[value] = [];
    }
    newDict[value].push(key);
  }
}
console.log(newDict);
