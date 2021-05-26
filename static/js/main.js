function send(colonne){
  $.ajax({
    url: '/jeu', // on donne l'URL du fichier de traitement
    type: "POST", // la requête est de type POST
    data: {'colonne':colonne}, // et on envoie nos données
    success: function(response) {
      $('#contentRefresh').html(response); // on affiche le nouveau tableau
    },
  });
}
