#!/usr/bin/node
if (!parseInt(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log(parseInt(process.argv[2]));
}
