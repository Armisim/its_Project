# coding=utf-8
# Copyright (c)
# Author: Simone Bollati

# Importazione delle librerie utilizzate all'interno del progetto
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import datetime
import sqlite3 as sqlite
from Led import Led
from Sensore import Sensore
from Database import Database

class Condizionatore:
    # Costruttore del condizionatore
    def __init__(self, sensore, led, database, valoreMax):
        self.sensore = sensore
        self.led = led
        self.database = database
        self.tempMax = valoreMax

    # Ritorna il valore soglia definito nel main
    def getValoreMax(self):
        return self.tempMax

    # Ritorna la data e l'orario
    def getData(self):
        return datetime.datetime.utcnow()
