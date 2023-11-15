#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (cha) {
    if (cha === undefined) {
      this.print();
    } else {
      for (let x = 0; x < this.height; x++) console.log(cha.repeat(this.width));
    }
  }
};
