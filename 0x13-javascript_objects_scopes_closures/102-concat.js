#!/usr/bin/node
const fs = require('fs');

const firstFile = fs.readFileSync(process.argv[2]).toString();
const secondsFile = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], firstFile + secondsFile);
