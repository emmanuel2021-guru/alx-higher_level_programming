#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super();
    if (size > 0) {
      super.width = size;
      super.height = size;
    }
  }
};
