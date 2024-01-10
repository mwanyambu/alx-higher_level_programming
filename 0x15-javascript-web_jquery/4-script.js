const $headerElement = $('header');
const divRed = $('DIV#toggle_header');

$divRed.on('click', () => {
  const myClass = $headerElement.attr('class');

  if (myClass === 'green') {
    $headerElement.toggleClass(`${myClass} red`);
  }
  if (myClass === 'red') {
    $headerElement.toggleClass(`${myClass} green`);
  }
});
