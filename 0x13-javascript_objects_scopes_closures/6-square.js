#!/usr/bin/node

/**
 * Represents a square, inherits from Square
 * @extends Square
 */
class Square extends require('./5-square.js') {
  /**
   * Creates a square with the specified size
   */

  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
