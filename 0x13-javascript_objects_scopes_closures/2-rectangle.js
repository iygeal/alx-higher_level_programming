#!/usr/bin/node

/**
 * Represents a rectangle
 */
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return {}; // Create an empty object if any condition is met
    }
    // Otherwise, initialize the properties of the rectangle
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
