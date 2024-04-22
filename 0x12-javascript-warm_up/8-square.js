#!/usr/bin/node

const ac = process.argv[2];

if (!isNaN(ac)) {
  for (let i = 0; i < ac; i++) {
    let str = '';
    for (let j = 0; j < ac; j++) {
      str += 'X';
    }
    console.log(str);
  }
} else {
  console.log('Missing size');
}
