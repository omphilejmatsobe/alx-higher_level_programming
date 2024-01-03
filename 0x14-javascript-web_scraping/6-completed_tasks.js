#!/usr/bin/node

const req = require('request');

req(process.argv[2], function (err, _res, body) {
  if (err) {
    console.log(err);
  } else {
    const completed = {};
    body = JSON.parse(body);

    for (let x = 0; x < body.length; ++x) {
      const userId = body[x].userId;
      const complete = body[x].completed;

      if (complete && !completed[userId]) {
        completed[userId] = 0;
      }

      if (complete) ++completed[userId];
    }

    console.log(completed);
  }
});
