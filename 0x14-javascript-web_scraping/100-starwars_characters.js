#!/usr/bin/node

const req = require('request');
const sw = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

req(sw, function (_err, _res, body) {
  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; ++i) {
    req(characters[i], function (_cErr, _cRes, cBody) {
      console.log(JSON.parse(cBody).name);
    });
  }
});
