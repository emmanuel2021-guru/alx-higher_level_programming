#!/usr/bin/node
const nb0ccurences = require('./7-occurrences').nb0ccurences;

console.log(nb0ccurences([1, 2, 3, 4, 5, 6], 8));
console.log(nb0ccurences([3, 2, 3, 4, 5, 3, 3], 3));
console.log(nb0ccurences(['S', 12, 'c', 'S', 'School', 8], 'S'));
