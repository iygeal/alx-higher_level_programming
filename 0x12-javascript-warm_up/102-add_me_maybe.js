#!/usr/bin/node

// Define a function named addMeMaybe as a property of the exports object.
exports.addMeMaybe = function (number, theFunction) {
  // Increment the number by 1
  const incrementedNumber = number + 1;
  // Call the provided function with the incremented number as an argument
  theFunction(incrementedNumber);
};
