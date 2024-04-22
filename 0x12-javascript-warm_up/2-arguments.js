#!/usr/bin/node

ac = process.argv.length;

if (ac > 2) {
  console.log("Argument" + (ac > 3 ? "s" : "") + " found");
} else {
  console.log("No argument");
}
