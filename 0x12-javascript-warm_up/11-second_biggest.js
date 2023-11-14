#!/usr/bin/node
// script returns the second biggest in array
const myArr = process.argv.slice(2).map(Number);
if (myArr.length <= 1) {
  console.log(0);
} else {
  const sortedarr = myArr.sort((x, y) => y - x);
  console.log(sortedarr[1]);
}
