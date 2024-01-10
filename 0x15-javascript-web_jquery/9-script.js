$(document).ready(function () {
  const myUrl = 'https://fourtonfish.com/hellosalut/?lang=fr';
  const myHello = $('div#hello');

  function getSalut () {
    return $.get({
      url: myUrl,
      dataType: 'json'

    });
  }
  getSalut().then((res) => {
    $myHello.text(res.hello);
  });
});
