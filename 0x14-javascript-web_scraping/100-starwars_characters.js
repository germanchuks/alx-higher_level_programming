#!/usr/bin/node
/* Script that prints all characters of a Star Wars movie. */
const request = require('request');

const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(movieUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmData = JSON.parse(body);
    filmData.characters.forEach(characterUrl => {
      request(characterUrl, (err, res, bd) => {
        if (!err) {
          const characterData = JSON.parse(bd);
          console.log(characterData.name);
        }
      });
    });
  }
});
