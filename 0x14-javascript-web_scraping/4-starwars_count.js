#!/usr/bin/node
/* Script prints the number of movies where the character “Wedge Antilles”
is present. */
const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmsData = JSON.parse(body).results;
    const filmsWithId = filmsData.filter((film) =>
      film.characters.includes(
        `https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    );
    console.log(filmsWithId.length);
  }
});
