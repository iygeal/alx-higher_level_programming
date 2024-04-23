#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (Object.keys(this).length === 0) {
      return;
    }
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    if (Object.keys(this).length === 0) {
      return;
    }
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    if (Object.keys(this).length === 0) {
      return;
    }
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
