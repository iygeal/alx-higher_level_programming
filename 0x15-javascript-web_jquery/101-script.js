$(document).ready(function () {
  // Add item to the list
  $('DIV#add_item').click(function () {
    // Create a new <li> element with text "Item"
    const newItem = $('<li>Item</li>');
    // Append the new <li> element to the list with class "my_list"
    $('ul.my_list').append(newItem);
  });

  // Remove last item from the list
  $('DIV#remove_item').click(function () {
    // Remove the last <li> element from the list with class "my_list"
    $('ul.my_list li:last-child').remove();
  });

  // Clear all items from the list
  $('DIV#clear_list').click(function () {
    // Remove all <li> elements from the list with class "my_list"
    $('ul.my_list').empty();
  });
});
