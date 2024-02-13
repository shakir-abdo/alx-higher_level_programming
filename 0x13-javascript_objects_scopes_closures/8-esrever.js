#!/usr/bin/node
exports.esrever = function (list) {
  let i = 0;
  let len = list.length - 1;
  while (len - i > 0) {
    const aux = list[len];
    list[len] = list[i];
    list[i] = aux;
    len--;
    i++;
  }
  return list;
};
