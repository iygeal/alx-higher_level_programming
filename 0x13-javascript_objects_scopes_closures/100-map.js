#!/usr/bin/node

const list = require('./100-data').list;
/*
* Use map to create a new array where each element
* is the element from the original list multiplied
* by its index
*/
const newList = list.map((element, index) => element * index);

// Print the initial list
console.log(list);

// Print the new list
console.log(newList);
