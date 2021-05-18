alert(document.getElementById('fleche').value);

function touche(e){
  var touche = event.keyCode;
      if (touche==37){
           document.getElementById('fleche').style.marginLeft ="6%" ;
      }if (touche==39){
           document.getElementById('fleche').style.marginLeft ="6%" ;
      }
    }
