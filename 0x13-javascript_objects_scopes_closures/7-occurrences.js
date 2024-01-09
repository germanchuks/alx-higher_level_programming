#!/usr/bin/node
// Returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let numberOfOccurrence = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      numberOfOccurrence++;
    }
  }
  return numberOfOccurrence;
};
