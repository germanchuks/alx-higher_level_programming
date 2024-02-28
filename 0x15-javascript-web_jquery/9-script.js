/*
  Script that fetches from 'https://hellosalut.stefanbohacek.dev/?lang=fr' and
  displays the value of hello from that fetch in the HTML tag DIV#hello.
*/

// $(function () {    
//   $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
//     $('#hello').text(data.hello);
//   })
// });

$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (response) {
      $('#hello').text(response.hello);
    }
  });
});
