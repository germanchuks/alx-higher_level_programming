/*
  Script that fetches and prints how to say “Hello” depending on the language.
*/
$(document).ready(function () {
  function fetchTranslation() {
    const languageCode = $('#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode,
      success: function (response) {
        $('#hello').append(response.hello);
      },
    });
  }
  $('#btn_translate').on('click', fetchTranslation);
  $('#language_code').on('keypress', function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
});
