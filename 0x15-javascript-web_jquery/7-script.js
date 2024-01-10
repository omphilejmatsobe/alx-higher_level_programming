$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (chara) {
  $('DIV#character').text(chara.name);
});

