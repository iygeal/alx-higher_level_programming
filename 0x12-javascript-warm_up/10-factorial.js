#!/usr/bin/node

function factorial (n) {
  return n === 0 || isNaN(n) ? 1 : n * factorial(n - 1);
}
const result = parseInt(process.argv[2]);

console.log(factorial(result));
