#!/usr/bin/node
const size = parseInt(process.argv[2]);
const unit = 'X';
let myUnit;
if (size) {
  for (let i = 0; i < size; i++) {
    myUnit = unit;
    for (let j = 1; j < size; j++) {
      myUnit = myUnit + unit;
    }
    console.log(myUnit);
  }
} else {
  console.log('Missing size');
}
