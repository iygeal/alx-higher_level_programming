#!/usr/bin/node

/**
 * Represents a square, inherits from Rectangle
 */

class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
