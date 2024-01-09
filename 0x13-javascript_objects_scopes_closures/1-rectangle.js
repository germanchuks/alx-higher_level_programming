#!/usr/bin/node
/* Defines a rectangle:
Constructor takes 2 arguments w and h
Initialize the instance attribute width with the value of w
Initialize the instance attribute height with the value of h
*/

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
