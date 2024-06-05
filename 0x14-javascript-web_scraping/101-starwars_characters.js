#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const characters = JSON.parse(body).characters;
  const charPromises = characters.map((character) => {
    return new Promise((resolve, reject) => {
      request.get(character, (charErr, charRes, charBody) => {
        if (charErr) {
          reject(charErr);
        } else {
          resolve(JSON.parse(charBody).name);
        }
      });
    });
  });
  Promise.all(charPromises)
    .then((charNames) => {
      charNames.forEach((name) => {
        console.log(name);
      });
    })
    .catch((error) => {
      console.error(error);
    });
});
