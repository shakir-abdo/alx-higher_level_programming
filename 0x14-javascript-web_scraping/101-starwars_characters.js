#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

const printCharacters = (characters, index) => {
  request(characters[index], function (error, res, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
};
request(url, (error, res, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});
