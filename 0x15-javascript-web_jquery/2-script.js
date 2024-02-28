/*
  Script to update the text color of the <header> element to
  red (#FF0000) when the user clicks on the tag DIV#red_handler
  using JQuery API.
*/
$('#red_header').on('click', function () {
  $('header').css('color', '#FF0000');
});
