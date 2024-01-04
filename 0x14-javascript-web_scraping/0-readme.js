#!/usr/bin/node

const fs = require('fs');

if (process.argv.length < 3) {
  process.exit(1);
}

const path = process.argv[2];

fs.readFile(path, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});
