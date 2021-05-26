from flask import Flask, render_template, request, redirect, session, url_for
from flask_session import Session
import os
from random import randint

# Création de l'application
app = Flask(__name__)

# matrice du jeu
matriceJeu = [['', '', '', '', '', '', ''],
              ['', '', '', '', '', '', ''],
              ['', '', '', '', '', '', ''],
              ['', '', '', '', '', '', ''],
              ['', '', '', '', '', '', ''],
              ['', '', '', '', '', '', '']]
# [["" for i in range(7)] for i in range(6)]


def verifWin(liste):
    chaine = ''.join(liste)
    if 'XXXX' in chaine:
        return 'X'
    elif 'OOOO' in chaine:
        return 'O'
    else:
        return


def defilVerif(matrice):
    for ligne in matrice:
        result = verifWin(ligne)
        if result:
            return result
    for col in range(0, len(matrice[0])):
        colonne = []
        for lign in range(0, len(matrice)):
            colonne.append(matrice[lign][col])
        result = verifWin(colonne)
        if result:
            return result


print(defilVerif(matriceJeu))


def posePion(jeu, colonne, joueur):
    '''Prend en paramètre la matrice du jeu et la colonne ou
    on joue et renvoie la matrice et si le pion a pu etre placé'''
    aJoue = False
    # on défile les lignes dans le sens inverse
    for ligne in range(len(jeu) - 1, -1, -1):
        # si la case est libre on place le pion
        if jeu[ligne][colonne] == "":
            jeu[ligne][colonne] = joueur
            aJoue = True  # indique que le pion a été placé
            break
    return jeu, aJoue


@app.route('/')
def accueil():
    return render_template('accueil.html')


@app.route('/jeu', methods=['GET', 'POST'])
def jeu():
    # si la matrice de jeu est en session
    if 'jeu' in session:
        # si la methode est GET on génére le template avec la matrice
        if request.method == 'GET':
            return render_template('index.html', matrice=session['jeu'])
        else:
            # sinon on pose le pion dans la colonne envoyer en POST
            session['jeu'], aJoue = posePion(
                session['jeu'], int(request.form['colonne']) - 1, session['joueur'])
            win = defilVerif(session['jeu'])
            if aJoue == True:
                if session['joueur'] == 'X':
                    session['joueur'] = 'O'
                elif session['joueur'] == 'O':
                    session['joueur'] = 'X'
                message = ''
            elif win:  # si un des joueurs a gagné
                if win == 'X'
                message = 'Les rouges ont gagné'
                else:
                    message = 'Les jaunes ont gagné'
            else:  # Si il n'a pas jouer on le refait jouer
                message = 'Tu ne peux pas jouer ici ! Rejoue !'
            return render_template('refresh.html', matrice=session['jeu'], message=message)
    else:
        # créé la matrice de jeu
        session['jeu'] = matriceJeu
        resul = randint(0, 1)
        if resul == 0:
            session['joueur'] = 'O'
        if resul == 1:
            session['joueur'] = 'X'
        return render_template('index.html', matrice=session['jeu'])


@app.route('/rejouer/')
def rejouer():
    # vide la matrice de jeu pour rejouer
    session['jeu'] = matriceJeu
    resul = randint(0, 1)
    if resul == 0:
        session['joueur'] = 'O'
    if resul == 1:
        session['joueur'] = 'X'
    return redirect(url_for('jeu'))


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    # Lancement de l'application, à l'adresse 127.0.0.0 et sur le port 3000
    app.run(host="127.0.0.1", port=3000, debug=True)
