#!/usr/bin/node
// script prints the first argument passed to it
if (process.argv[2] !== undefined) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
