#!/usr/bin/node

const req = require('request');

req(process.argv[2], function (_err, res) {
  console.log('code:', res.statusCode); // Print the response status code if a response was received
});
