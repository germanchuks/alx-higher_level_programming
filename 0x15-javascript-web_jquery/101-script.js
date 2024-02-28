/*
Script that adds, removes and clears LI elements from a list when the
user clicks
*/
$(function () {
  // Add item to UL.my_list
  $('#add_item').on('click', function () {
    $('.my_list').append('<li>Item</li>');
  });

  // Remove item from UL.my_list
  $('#remove_item').on('click', function () {
    $('.my_list li:last').remove();
  });

  // Clear all elements of UL.my_list
  $('#clear_list').on('click', function () {
    $('.my_list').empty();
  });
});
