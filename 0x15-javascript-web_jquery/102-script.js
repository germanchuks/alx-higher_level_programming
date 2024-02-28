/*
  Script that fetches and prints how to say “Hello” depending on the language.
*/
$(document).ready(function () {
  $('#btn_translate').on('click', function () {
    const languageCode = $('#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode,
      success: function (response) {
        $('#hello').append(response.hello);
      },
    });
  });
});
