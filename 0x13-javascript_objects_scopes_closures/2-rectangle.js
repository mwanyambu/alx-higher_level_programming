#!/usr/bin/node
// script initializes width and height
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height  = h;
    }
  }
}
