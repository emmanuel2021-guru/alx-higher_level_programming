$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
  $('header').text(data.name);
});
