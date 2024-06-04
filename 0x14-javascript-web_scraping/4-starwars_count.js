#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = '18';

let counter = 0;
request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const movie = JSON.parse(body);
    movie.results.forEach((movie) => {
      movie.characters.forEach((character) => {
        if (character.includes(characterId)) {
          counter += 1;
        }
      });
    });
    console.log(counter);
  }
});
