$(document).ready(function () {
  url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  $.getJSON(url, function (data) {
    const movies = data.results;
    const list = $('ul#list_movies');

    $.each(movies, function (index, movie) {
      list.append('<li>' + movie.title + '</li>');
    });
  });
});
