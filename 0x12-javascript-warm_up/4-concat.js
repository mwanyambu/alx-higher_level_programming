#!/usr/bin/node
// script prints two args concatnated by "is"
if (process.argv[2] === undefined && process.argv[3] === undefined) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
