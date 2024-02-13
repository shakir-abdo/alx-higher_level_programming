#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let q = '';
      for (let j = 0; j < this.width; j++) {
        q += 'X';
      }
      console.log(q);
    }
  }
}

module.exports = Rectangle;
