const sourceUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const charDiv = $('div#character');

$.ajax({
  url: sourceUrl,
  dataType: 'json'
}).done((data) => {
  $charDiv.text(data.name);
});
