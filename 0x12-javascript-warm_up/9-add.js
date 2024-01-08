#!/usr/bin/node
/* Prints the addition of 2 integers:
The first argument is the first integer
The second argument is the second integer
*/

function add (a, b) {
  return a + b;
}

const firstInt = parseInt(process.argv[2]);
const secondInt = parseInt(process.argv[3]);

console.log(add(firstInt, secondInt));
