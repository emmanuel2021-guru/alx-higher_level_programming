#!/usr/bin/node
const request = require('request');
request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const jsonObj = JSON.parse(body);
    console.log(jsonObj.title);
  }
});
