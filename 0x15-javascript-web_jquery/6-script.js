const $myHeader = $('header');
const $headerUpdate = $('div#update_header');

$headerUpdate.on('click', () => {
  $myHeader.text('New header!!!');
});
