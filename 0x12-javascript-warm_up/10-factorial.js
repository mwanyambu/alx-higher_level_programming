#!/usr/bin/node
// script computes and prints factorial of a number
function factorial(n) {
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const result = parseInt(process.argv[2]);
console.log(factorial(result);
