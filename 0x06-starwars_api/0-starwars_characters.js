#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
  } else {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    // Function to fetch and print character names
    const printCharacterNames = async () => {
      for (const characterUrl of characters) {
        await new Promise((resolve, reject) => {
          request(characterUrl, (error, response, body) => {
            if (error) {
              reject(error);
            } else if (response.statusCode !== 200) {
              reject(new Error(`Unexpected status code for ${characterUrl}: ${response.statusCode}`));
            } else {
              const characterData = JSON.parse(body);
              console.log(characterData.name);
              resolve();
            }
          });
        });
      }
    };

    printCharacterNames().catch(error => console.error('Error fetching characters:', error));
  }
});
