#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const jsonObj = JSON.parse(body);
    let result = {};
    for (let i = 0; i < jsonObj.length; i++) {
      if (jsonObj[i].completed === true) {
        if (jsonObj[i].userId in result) {
          result[jsonObj[i].userId] += 1;
	} else {
          result[jsonObj[i].userId] = 1;
	}
      }
    }
    console.log(result);
  }
});
