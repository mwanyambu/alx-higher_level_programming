#!/usr/bin/node
// a class square that inherits from rectangle
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let y = 0; y < this.height; y++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
