#!/usr/bin/node
// converts number from base10 to another base
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
