#!/usr/bin/node
/* Prints x times “C is fun”
Where x is the first argument of the script
If the first argument can’t be converted to an integer, print “Missing number of occurrences”
*/

const occurrences = parseInt(process.argv[2]);

if (!occurrences) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < occurrences) {
    console.log('C is fun');
    i++;
  }
}
