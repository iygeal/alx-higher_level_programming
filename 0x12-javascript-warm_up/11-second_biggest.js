#!/usr/bin/node

// Extract all arguments passed to the script and convert them to integers
const integers = process.argv.slice(2).map((arg) => parseInt(arg));

// Sort the integers in descending order
const sortedIntegers = integers.sort((a, b) => b - a);

// Check if there are no arguments or only one argument
if (sortedIntegers.length === 0 || sortedIntegers.length === 1) {
  console.log(0);
} else {
  // Print the second largest integer
  console.log(sortedIntegers[1]);
}
