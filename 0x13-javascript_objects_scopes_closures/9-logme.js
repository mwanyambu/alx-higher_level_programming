#!/usr/bin/node
// script prints number of args already printed and value
let count = 0;
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
