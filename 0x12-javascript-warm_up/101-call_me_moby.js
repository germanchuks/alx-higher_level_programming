#!/usr/bin/node
// Executes x times in a function.

function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

module.exports = { callMeMoby };
