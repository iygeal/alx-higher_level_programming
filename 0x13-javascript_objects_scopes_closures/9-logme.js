#!/usr/bin/node

/**
 * Keeps track of the number of arguments already printed
 * and prints the new argument value.
 * @param {*} item - The argument value to be printed.
 */
let count = 0;

exports.logMe = function (item) {
  // Print the current count and the argument value
  console.log(count + ': ' + item);
  // Increment the count for the next argument
  count++;
};
