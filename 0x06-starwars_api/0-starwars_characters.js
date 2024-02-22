#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data: ${response.statusCode}`);
    return;
  }

  const film = JSON.parse(body);
  const charactersUrls = film.characters;

  charactersUrls.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error(`Failed to fetch character data: ${response.statusCode}`);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
