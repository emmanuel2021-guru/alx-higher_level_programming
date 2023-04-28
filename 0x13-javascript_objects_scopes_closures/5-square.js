#!/usr/bin/node
const Rectangle = require('./4-Rectangle.js');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super();
    this.size = size;
  }
};
