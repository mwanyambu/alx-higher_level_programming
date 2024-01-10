const $myList = $('ul.my_list');
const $addItem = $('div#add_item');

$addItem.on('click', () => {
  $myList.append('<li>Item</li>');
});
