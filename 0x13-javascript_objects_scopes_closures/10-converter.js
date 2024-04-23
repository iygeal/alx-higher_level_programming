#!/usr/bin/node

/**
 * Returns a function that converts a number from base 10 to the specified base.
 * @param {number} base - The base to which the number will be converted.
 * @returns {function} - A function that converts a number to the specified base.
 */
exports.converter = function (base) {
  // Return a function that converts a number to the specified base
  return function (number) {
    return number.toString(base);
  };
};
