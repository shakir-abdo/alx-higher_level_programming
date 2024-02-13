#!/usr/bin/node
const SquareQ = require('./5-square');

class Square extends SquareQ {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let q = '';
      for (let j = 0; j < this.width; j++) {
        q += c;
      }
      console.log(q);
    }
  }
}

module.exports = Square;
