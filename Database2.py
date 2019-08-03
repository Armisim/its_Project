# coding=utf-8
# Copyright (c)
# Author: Simone Bollati

# Importazione delle librerie utilizzate all'interno del progetto
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import datetime
import sqlite3 as sqlite
import server2

class Database:
    # Costruttore Database
    def __init__(self, connessione, cursore, comandosql):
        self.connessione = connessione
        self.cursore = cursore
        self.comandosql = comandosql

    # Ritorna il tipo di connessione
    def getConnessione(self):
        return self.connessione

    # Ritorna il tipo di cursore
    def getCursore(self):
        return self.cursore

    # Ritorna il comando sql
    def getComandosql(self):
        return self.comandosql

    # Esegue la query sul DB e stampa l'avviso a console
    def eseguiQuery(self, comandosql, data, temp):
        self.cursore.execute(comandosql, (data, temp))
        self.connessione.commit()
        print("Dati salvati - temperatura: " + str(temp))
