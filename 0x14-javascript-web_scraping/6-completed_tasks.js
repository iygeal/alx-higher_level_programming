#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const todos = JSON.parse(body); // parse JSON response
  const completedTasks = {}; // object to store completed tasks for each user

  todos.forEach((todo) => {
    if (todo.completed) { // check if todo is completed
      if (!completedTasks[todo.userId]) { // check if user id already exists
        completedTasks[todo.userId] = 1; // add user id to object
      } else {
        completedTasks[todo.userId]++; // increment count for user id
      }
    }
  });

  console.log(completedTasks);
});
