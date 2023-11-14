#!/usr/bin/node
// runs a function x times
exports.callMeMoby = function (x, theFunction) {
  for (let y = 0; y < x; y++) {
    theFunction();
  }
};
