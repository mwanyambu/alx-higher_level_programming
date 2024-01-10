const $headerElement = $('header');
const divRed = $('div#red_header');

$divRed.on('click', function () {
  $headerElement.css('color', '##FF0000');
});
