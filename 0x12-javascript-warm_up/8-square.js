#!/usr/bin/node
/* Prints a square:
The first argument is the size of the square
If the first argument can’t be converted to an integer, print “Missing size”
*/

const sizeInput = parseInt(process.argv[2]);

if (!sizeInput) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sizeInput; i++) {
    let row = '';
    for (let j = 0; j < sizeInput; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
