#!/usr/bin/node
const sq = require('./5-square');
module.exports = class Square extends sq {
  constructor (size) {
    super();
    super.size = size;
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < super.size; i++) {
        console.log(c.repeat(super.size));
      }
    } else {
      super.print();
    }
  }
};
