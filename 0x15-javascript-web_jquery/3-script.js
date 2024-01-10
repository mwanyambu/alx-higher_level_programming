const $headerElement = $('header');
const divRed = $('div#red_header');

$divRed.on('click', function () {
  $headerElement.addClass('red');
});
