function send(colonne){
  $.ajax({
    url: '/', // on donne l'URL du fichier de traitement
    type: "POST", // la requête est de type POST
    data: {'colonne':colonne}, // et on envoie nos données
    success: function(response) {
      if (response!='None'){ // si le joueur a pu jouer
        $('table').html(response); // on affiche le nouveau tableau
        $('#error').html(''); // on vide les erreurs
      }else{
        $('#error').html('Vous ne pouvez pas jouer ici'); // on affiche l'erreur
      }
    },
  });
}
