#!/usr/bin/node
// script returns sum of two numbers
function add(a, b) {
  return a + b;
}
if (process.argv.length > 3) {
  num1 = parseInt(process.argv[2]);
  num2 = parseInt(process.argv[3]);
  if (!isNaN(num1) && !isNaN(num2)) {
    console.log(add(num1, num2));
  } else {
    console.log('NaN');
  }
}
