$('document').ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=f', function (data) {
    $('DIV#hello').text(data.hello);
  });
});

