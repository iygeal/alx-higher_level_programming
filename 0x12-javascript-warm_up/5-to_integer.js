#!/usr/bin/node

const ac = process.argv[2];

if (!isNaN(ac)) {
  console.log('My number: ' + ac);
} else {
  console.log('Not a number');
}
