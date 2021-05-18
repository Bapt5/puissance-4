function send(colonne){
  $.ajax({
    url: '/', // on donne l'URL du fichier de traitement
    type: "POST", // la requête est de type POST
    data: {'colonne':colonne}, // et on envoie nos données
    success: function() {
      document.location.reload();
    },  
  });
}
