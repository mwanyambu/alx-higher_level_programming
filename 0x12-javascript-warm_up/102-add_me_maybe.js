#!/usr/bin/node
// exports add function
exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
