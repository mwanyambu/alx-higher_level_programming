#!/usr/bin/node
// script to calculate the number of occurences
exports.nbOccurences = function (list, searchElement) {
  const occurences = list.reduce((count, element) => {
    return element === searchElement ? count + 1 : count;
  }, 0);
  return occurences;
};
