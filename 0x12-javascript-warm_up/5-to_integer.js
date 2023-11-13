#!/usr/bin/node
// script returns an iteger if the first argument is an integer
if (process.argv.length >= 3) {
  const val = process.argv[2];
  const newval = parseInt(val);
  if (!isNaN(newval)) {
    console.log('My number:', newval);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
