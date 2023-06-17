#!/usr/bin/node
if (process.argv.length === 2) {
  console.log('0');
} else {
  let hiNum = 0;
  for (let i = 2; i < process.argv.length; i++) {
    if (process.argv[i] > hiNum) {
      hiNum = process.argv[i];
    }
  }
  let secNum = 0;
  for (let i = 2; i < process.argv.length; i++) {
    if (process.argv[i] > secNum && process.argv[i] < hiNum) {
      secNum = process.argv[i];
    }
  }
  console.log(secNum);
}
