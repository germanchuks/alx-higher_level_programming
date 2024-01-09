#!/usr/bin/node
/* Defines a rectangle:
Constructor takes 2 arguments w and h
Initialize the instance attribute width with the value of w
Initialize the instance attribute height with the value of h
If w or h is equal to 0 or not a positive integer, create an empty object
Contains an instance method called print() that prints the rectangle using the character X
Contains an instance method called rotate() that exchanges the width and the height of the rectangle
Contains an instance method called double() that multiples the width and the height of the rectangle by 2
*/

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return {};
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    const rtempHeight = this.width;
    this.width = this.height;
    this.height = rtempHeight;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
