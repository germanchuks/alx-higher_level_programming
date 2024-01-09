#!/usr/bin/node
/* Defines a square and inherits from Square (5-square.js):
Contains an instance method called charPrint(c) that prints the rectangle using the character c
If c is undefined, use the character X
*/

const baseSquare = require('./5-square');

class Square extends baseSquare {
  charPrint (c) {
    const character = c || 'X';

    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += character;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
