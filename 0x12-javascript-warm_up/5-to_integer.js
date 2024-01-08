#!/usr/bin/node
/* Prints My number: <first argument converted in integer> if the first argument can be converted to an integer:
If the argument can’t be converted to an integer, print “Not a number”
*/

const inputInt = parseInt(process.argv[2]);

if (!inputInt) {
  console.log('Not a number');
} else {
  const outputString = 'My number: ' + inputInt;
  console.log(outputString);
}
