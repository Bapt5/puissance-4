from flask import Flask, render_template, request, redirect, session, url_for
from flask_session import Session
import os

# Création de l'application
app = Flask(__name__)

# matrice du jeu
jeu = [["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], [
    "", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""]]


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'jeu' in session:
        if request.method == 'GET':
            return render_template('index.html', matrice=session['jeu'])
        else:
            jouer = False
            for ligne in range(len(jeu) - 1, -1, -1):
                colonne = int(request.form['colonne']) - 1
                if session['jeu'][ligne][colonne] == "":
                    session['jeu'][ligne][colonne] = 'X'
                    jouer = True  # indique que le joueur à jouer
                    break
            # Si il n'a pas jouer on le refera jouer
            return str(jouer)
    else:
        session['jeu'] = jeu
        return render_template('index.html', matrice=session['jeu'])


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    # Lancement de l'application, à l'adresse 127.0.0.0 et sur le port 3000
    app.run(host="127.0.0.1", port=3000, debug=True)
