#!/usr/bin/node
/* Imports an array and computes a new array.
A new list is created with each value equal to the value of the initial list, multipled by the index in the list
Prints both the initial list and the new list
*/

const list = require('./100-data.js').list;

const newList = list.map((num, index) => {
  return num * index;
});

console.log(list);
console.log(newList);
