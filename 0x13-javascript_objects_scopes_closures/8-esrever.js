#!/usr/bin/node
// script prints list in reversed order
exports.esrever = function (list) {
  esrever = [];
  for (let x = list.length - 1; x >= 0; x--) {
   esrever.push(list[x]);
  }
  return esrever;
};
