#!/usr/bin/node

/**
 * Represents a rectangle
 */
class Rectangle {
  constructor (w, h) {
    // Initialize instance attributes
    this.width = w;
    this.height = h;

    // Check if w or h is not a positive integer or equal to 0
    if (w <= 0 || !Number.isInteger(w) || h <= 0 || !Number.isInteger(h)) {
      return {}; // Return an empty object if conditions are met
    }
  }
}

module.exports = Rectangle;
