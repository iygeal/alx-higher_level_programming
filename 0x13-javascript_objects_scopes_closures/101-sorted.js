#!/usr/bin/node

const dict = require('./101-data').dict;

// Initialize an empty object to store the new dictionary
const userOccurrenceDict = {};

// Iterate through the keys (user ids) of the input dictionary
for (const userId in dict) {
  // Get the number of occurrences for the current user id
  const occurrences = dict[userId];

  // If the occurrences is not a key in the new dictionary, initialize it with an empty array
  if (!userOccurrenceDict[occurrences]) {
    userOccurrenceDict[occurrences] = [];
  }

  // Push the current user id to the list of user ids for the current occurrences
  userOccurrenceDict[occurrences].push(userId);
}

// Print the new dictionary
console.log(userOccurrenceDict);
