# coding=utf-8
# Copyright (c)
# Author: Simone Bollati

# Importazione delle librerie utilizzate all'interno del progetto
import time
import datetime
import sqlite3 as sqlite
import bottle
from bottle import Bottle, request, redirect
import threading

# Rotta che svuota la tabella del DB
@bottle.route("/delete")
def paginaTemperature():
    connessione = sqlite.connect("log.db")
    cursore = connessione.cursor()
    cursore.execute("DELETE FROM VALORI")
    connessione.commit()
    return redirect('tabella')
    
# Rotta che aggiorna la tabella del DB
@bottle.route("/refresh")
def refresh():
    return redirect('/tabella')

# Rotta che renderizza la tabella del DB nella pagina web del server, riaggiornando la tabella
@bottle.route("/tabella")
def paginaTemperature():
    connessione = sqlite.connect("log.db")
    righe=list()
    cursore = connessione.cursor()
    cursore.execute("SELECT * FROM VALORI")
    riga=True
    while riga!=None:
        riga=cursore.fetchone()
        if riga==None:
            break
        righe.append(riga)

    return bottle.template("table", righe=righe)

# Rotta che reindirizza alla pagina 'login'
@bottle.route('/login')
def login():
    return bottle.template("login")

# Rotta che recupera i dati del login dell'utente e li controlla, se corrispondono a quelli registrati si verrà reindirizzati alla pagina 'home', in caso contrario alla pagina 'loginFailed'
@bottle.route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return redirect('/home')
    else:
        return bottle.template("loginFailed")

def check_login(username, password):
    if username == "mario" and password == "rossi":
        return True

# Rotta che reindirizza alla pagina 'login'
@bottle.route("/")
def homePage():
    return redirect('/login')

# Rotta che reindirizza alla pagina 'home'
@bottle.route('/home')
def home():
    return bottle.template("home")

# Rotta che reindirizza alla pagina 'about'
@bottle.route('/about')
def about():
    return bottle.template("about")

# Funzione che si occupa di far partire il server web
def avviaServer():
    bottle.run(host="0.0.0.0", port=8080)



