#!/usr/bin/node

const ac = process.argv[2];

if (!isNaN(ac)) {
  for (let i = 0; i < ac; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
