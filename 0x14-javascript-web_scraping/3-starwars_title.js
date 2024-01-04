#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(apiUrl, function (_err, _res, body) {
  body = JSON.parse(body);
  console.log(body.title);
});
