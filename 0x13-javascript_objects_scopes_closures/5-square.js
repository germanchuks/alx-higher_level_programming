#!/usr/bin/node
/* Defines a square and inherits from Rectangle:
Constructor takes 1 argument: size
Constructor of Rectangle be called using super()
*/

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
