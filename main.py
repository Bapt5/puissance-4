from flask import Flask, render_template, request, redirect, session, url_for
from flask_session import Session
import os

# Création de l'application
app = Flask(__name__)

# matrice du jeu
jeu = [["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], [
    "", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""]]


@app.route('/')
def index():
    session['jeu'] = jeu
    return redirect(url_for('game'))


@app.route('/game')
def game():
    return render_template('index.html', matrice=session['jeu'])


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    # Lancement de l'application, à l'adresse 127.0.0.0 et sur le port 3000
    app.run(host="127.0.0.1", port=3000, debug=True)
