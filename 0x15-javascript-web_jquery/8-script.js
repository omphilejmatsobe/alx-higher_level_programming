$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (getmovie) {
  $('UL#list_movies').append(...getmovie.results.map(movie => `<li>${movie.title}</li>`));
});

