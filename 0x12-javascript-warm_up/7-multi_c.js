#!/usr/bin/node
// script prints "c is fun" x times
if (process.argv.length >= 3) {
  const val = process.argv[2];
  const newval = parseInt(val);
  if (!isNaN(newval)) {
    for (let x = 0; x < newval; x++) {
      console.log('C is fun');
    }
  } else {
    console.log('Missing number of occurences');
  }
}
