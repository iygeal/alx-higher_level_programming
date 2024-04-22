#!/usr/bin/node

// Extract the first argument and convert it to an integer
const a = parseInt(process.argv[2]);

// Extract the second argument and convert it to an integer
const b = parseInt(process.argv[3]);

// Define a function to add two integers
function add (a, b) {
  return a + b;
}

// Print the result of adding the two integers
console.log(add(a, b));
