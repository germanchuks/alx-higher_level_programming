#!/usr/bin/node
/* Prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop
The first line: “C is fun”
The second line: “Python is cool”
The third line: “JavaScript is amazing” */

const lineArray = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

for (let i = 0; i < lineArray.length; i++) {
  console.log(lineArray[i]);
}
