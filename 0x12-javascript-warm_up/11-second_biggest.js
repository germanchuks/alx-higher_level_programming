#!/usr/bin/node
/* Searches the second biggest integer in the list of arguments.
If no argument passed, prints 0.
If the number of arguments is 1, prints 0.
*/

let secondBiggest = 0;
const argList = [];

if (process.argv.length > 3) {
  for (let i = 2; i < process.argv.length; i++) {
    argList.push(parseInt(process.argv[i]));
  }
  argList.sort((a, b) => b - a);
  secondBiggest = argList[1];
}
console.log(secondBiggest);
