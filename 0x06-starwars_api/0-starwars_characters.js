#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.error('Error:', error);
        return;
      }
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});

