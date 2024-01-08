#!/usr/bin/node
/* Computes and prints a factorial
The first argument is integer (argument can be cast as integer) used for computing the factorial
*/

function factorial (a) {
  if (a === 0 || isNaN(a)) {
    return 1;
  }
  return a * factorial(a - 1);
}

const inputNumber = parseInt(process.argv[2]);
console.log(factorial(inputNumber));
