#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const characters = JSON.parse(body).characters;

  characters.forEach((character) => {
    request.get(character, (charErr, charRes, Charbody) => {
      if (charErr) {
        console.error(charErr);
        return;
      }
      const charName = JSON.parse(Charbody).name;
      console.log(charName);
    });
  });
});
