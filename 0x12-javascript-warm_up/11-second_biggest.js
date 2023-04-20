#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let maxNum = 0;
  let secondMax = 0;
  for (let n = 2; n < process.argv.length; n++) {
    if (parseInt(process.argv[n]) > maxNum) {
      maxNum = parseInt(process.argv[n]);
    }
  }
  for (let n = 2; n < process.argv.length; n++) {
    if (parseInt(process.argv[n]) > secondMax && parseInt(process.argv[n]) < maxNum) {
      secondMax = parseInt(process.argv[n]);
    }
  }
  console.log(secondMax);
}
