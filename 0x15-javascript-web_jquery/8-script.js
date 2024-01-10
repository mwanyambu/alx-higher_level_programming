const $filmUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';
const $movieList = $('ul#list_movies');

$.ajax({
  url: filmUrl,
  dataType: 'json'
}).done((data) => {
  const movies = data.results;

  for (let x = 0; x < movies.length; ++x) {
    const titles = movies[x].title;
    const element = `<li>${titles}`;
    $movieList.append(element);
  }
});
