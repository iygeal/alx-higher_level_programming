#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  // Initialize a variable to count occurrences
  let count = 0;

  // Loop through the list
  for (let i = 0; i < list.length; i++) {
    // Check if the current element is equal to the search element
    if (list[i] === searchElement) {
      // If yes, increment the count
      count++;
    }
  }

  // Return the count of occurrences
  return count;
};
