#!/usr/bin/node

// Define a function named executeXTimes as a property of the exports object, named callMeMoby.
// This function takes two parameters: x (number of times) and theFunction (the function to execute).
exports.callMeMoby = function executeXTimes (x, theFunction) {
  // Loop x times
  for (let i = 0; i < x; i++) {
    // Call theFunction x times
    theFunction();
  }
};
