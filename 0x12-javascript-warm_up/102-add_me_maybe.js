#!/usr/bin/node
// Increments and calls a function.

function addMeMaybe (number, theFunction) {
  return theFunction(number + 1);
}
module.exports = { addMeMaybe };
