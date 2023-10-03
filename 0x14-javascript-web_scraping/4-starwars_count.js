#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const jsonObj = JSON.parse(body);
    let count = 0;
    for (let i = 0; i < jsonObj.results.length; i++) {
      for (let j = 0; j < jsonObj.results[i].characters.length; j++) {
        if (jsonObj.results[i].characters[j] === 'https://swapi-api.alx-tools.com/api/people/18/') {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
