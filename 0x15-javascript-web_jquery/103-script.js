$(document).ready(function () {
  function fetchTranslation() {
    const langCode = $('#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`;

    $.get(url, function (data) {
      $('#hello').text(data.hello);
    });
  }

  // Fetch translation when the button is clicked
  $('#btn_translate').click(fetchTranslation);

  // Fetch translation when Enter key is pressed while the input field is focused
  $('#language_code').keypress(function (e) {
    if (e.which === 13) {
      // 13 is the Enter key
      fetchTranslation();
    }
  });
});
