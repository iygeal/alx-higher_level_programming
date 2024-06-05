#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const url = 'https://swapi-api.alx-tools.com/api/films/${movieId}';

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const characters = JSON.parse(body);

  characters.forEach((character) => {
    console.log(character.name);
  });
});
