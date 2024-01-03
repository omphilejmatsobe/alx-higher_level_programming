#!/usr/bin/node

const req = require('request');
const fileSystem = require('fs');

req(process.argv[2], function (_err, _res, body) {
  fileSystem.writeFile(process.argv[3], body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
