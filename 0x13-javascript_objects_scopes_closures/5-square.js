#!/usr/bin/node
// a class square that inherits from rectangle
module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
};
