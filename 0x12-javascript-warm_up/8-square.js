#!/usr/bin/node
// script prints a square
if (process.argv.length >= 3) {
  const val = process.argv[2];
  const newval = parseInt(val);
  if (!isNaN(newval)) {
    for (let x = 0; x < newval; x++) {
      let z = '';
      for (let y = 0; y < newval; y++) {
        z += 'X';
      } console.log(z);
    }
  } else {
    console.log('Missing size');
  }
}
