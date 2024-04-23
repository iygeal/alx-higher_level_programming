#!/usr/bin/node
exports.esrever = function (list) {
  // Initialize an empty array to store the reversed list
  let reversedList = [];

  // Loop through the input list in reverse order
  for (let i = list.length - 1; i >= 0; i--) {
    // Add each element of the input list to the reversed list
    reversedList.push(list[i]);
  }

  // Return the reversed list
  return reversedList;
};
