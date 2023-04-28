#!/usr/bin/node
function factorial (n) {
  if (!n) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const fact = factorial(parseInt(process.argv[2]));
console.log(fact);