#!/usr/bin/node
const myString = 'C is fun';
const num = parseInt(process.argv[2]);
if (num) {
  for (let i = 0; i < num; i++) {
    console.log(myString);
  }
} else {
  console.log('Missing number of occurences');
}
