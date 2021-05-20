from flask import Flask, render_template, request, redirect, session, url_for
from flask_session import Session
import os
from random import randint

# Création de l'application
app = Flask(__name__)

# matrice du jeu
matrice = [["" for i in range(7)] for i in range(6)]



def posePion(jeu, colonne, joueur):
    '''Prend en paramètre la matrice du jeu et la colonne ou
    on joue et renvoie la matrice et si le pion a pu etre placé'''
    if joueur=='X':
        session['joueur']='O'
    if joueur=='O':
        session['joueur']='X'
    aJoue = False
    # on défile les lignes dans le sens inverse
    for ligne in range(len(jeu) - 1, -1, -1):
        # si la case est libre on place le pion
        if jeu[ligne][colonne] == "":
            jeu[ligne][colonne] = joueur

            aJoue = True  # indique que le pion a été placé
            break
    return jeu, aJoue

def win(jeu):
    for ligne in range(len(jeu) - 1, -1, -1):
        # si la case est libre on place le pion
        if jeu[ligne][colonne] == "":
            jeu[ligne][colonne] = joueur
    return winer

@app.route('/', methods=['GET', 'POST'])
def index():
    # si la matrice de jeu est en session
    if 'jeu' in session:
        # si la methode est GET on génére le template avec la matrice
        if request.method == 'GET':
            return render_template('index.html', matrice=session['jeu'])
        else:
            # sinon on pose le pion dans la colonne envoyer en POST
            session['jeu'], aJoue = posePion(
                session['jeu'], int(request.form['colonne']) - 1, session['joueur'])
            if aJoue == True:
                return render_template('refresh.html', matrice=session['jeu'])
            else:  # Si il n'a pas jouer on le refait jouer
                return 'None'
    else:
        # créé la matrice de jeu
        session['jeu'] = matrice
        resul=randint(0,1)
        if resul==0:
            session['joueur']='O'
        if resul==1:
            session['joueur']='X'
        return render_template('index.html', matrice=session['jeu'])


@app.route('/rejouer/')
def rejouer():
    # vide la matrice de jeu pour rejouer
    session['jeu'] = matrice
    resul=randint(0,1)
    if resul==0:
        session['joueur']='O'
    if resul==1:
        session['joueur']='X'
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    # Lancement de l'application, à l'adresse 127.0.0.0 et sur le port 3000
    app.run(host="127.0.0.1", port=3000, debug=True)
