from flask import Flask, render_template, request, redirect, session, url_for
from flask_session import Session
import os

# Création de l'application
app = Flask(__name__)

# matrice du jeu
matrice = [["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], [
    "", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""]]


def posePion(jeu, colonne):
    aJoue = False
    for ligne in range(len(jeu) - 1, -1, -1):
        if jeu[ligne][colonne] == "":
            jeu[ligne][colonne] = 'X'
            aJoue = True  # indique que le joueur à jouer
            break
    return jeu, aJoue


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'jeu' in session:
        if request.method == 'GET':
            return render_template('index.html', matrice=session['jeu'])
        else:
            session['jeu'], aJoue = posePion(
                session['jeu'], int(request.form['colonne']) - 1)
            # Si il n'a pas jouer on le refera jouer
            if aJoue == True:
                return render_template('refresh.html', matrice=session['jeu'])
            else:
                return 'None'
    else:
        session['jeu'] = matrice
        return render_template('index.html', matrice=session['jeu'])


@app.route('/rejouer/')
def rejouer():
    session['jeu'] = matrice
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    # Lancement de l'application, à l'adresse 127.0.0.0 et sur le port 3000
    app.run(host="127.0.0.1", port=3000, debug=True)
