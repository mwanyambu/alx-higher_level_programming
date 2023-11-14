#!/usr/bin/node
// script computes and prints factorial of a number
if (process.argv.length >= 2) {
  let n = parseInt(process.argv[2]);
  if (!isNaN(n)) {
    let y = 1;
    for (let x = 1; x <= n; x++) {
      y *= x;
    }
    console.log(y);
  } else {
    console.log(1);
  }
} else {
  console.log(1);
}
