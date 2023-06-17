#!/usr/bin/node
if (process.argv.length === 2) {
  console.log('0');
} else {
  let hiNum = 0;
  for (let i = 2; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > hiNum) {
      hiNum = parseInt(process.argv[i]);
    }
  }
  let secNum = 0;
  for (let i = 2; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > secNum && parseInt(process.argv[i]) < hiNum) {
      secNum = parseInt(process.argv[i]);
    }
  }
  console.log(secNum);
}
