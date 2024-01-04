#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, _res, body) {
  if (err) {
    console.log(err);
  } else {
    const finished = {};
    body = JSON.parse(body);

    for (let x = 0; x < body.length; ++x) {
      const userId = body[x].userId;
      const completed = body[x].completed;

      if (completed && !finished[userId]) {
        finished[userId] = 0;
      }
      if (completed) ++finished[userId];
    }
    console.log(finished);
  }
});
