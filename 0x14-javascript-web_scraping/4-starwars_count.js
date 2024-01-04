#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

let times = 0;

request(apiUrl, function (_err, _res, body) {
  body = JSON.parse(body).results;

  for (let x = 0; x < body.length; ++x) {
    const chars = body[x].chars;

    for (let y = 0; y < chars.length; ++y) {
      const charr = chars[y]
      const charId = charr.split('/')[5];

      if (charId === '18') {
        times += 1;
      }
    }
  }
  console.log(times);
});
