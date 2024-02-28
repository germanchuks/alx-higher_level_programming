/*
  Script that fetches and lists the title for all movies by using the URL:
  'https://swapi-api.alx-tools.com/api/films/?format=json'
*/
$(function () {
  const $movies_list = $('#list_movies');
  
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (response) {
      $.each(response.results, function(i, movie) {
        $movies_list.append('<li>' + movie.title + '</li>');
      });
    }
  });
});
