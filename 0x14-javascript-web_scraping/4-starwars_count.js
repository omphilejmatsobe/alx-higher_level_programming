#!/usr/bin/node

const req = require('request');
const sw = process.argv[2];
let x = 0;

req(sw, function (_err, _res, body) {
  body = JSON.parse(body).results;

  for (let i = 0; i < body.length; ++i) {
    const characters = body[i].characters;

    for (let j = 0; j < characters.length; ++j) {
      const character = characters[j];
      const characterId = character.split('/')[5];

      if (characterId === '18') {
        x += 1;
      }
    }
  }

  console.log(x);
});
