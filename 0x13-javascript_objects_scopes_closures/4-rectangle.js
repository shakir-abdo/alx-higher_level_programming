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

  rotate () {
    const rt = this.width;
    this.width = this.height;
    this.height = rt;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
