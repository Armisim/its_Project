# coding=utf-8
# Copyright (c)
# Author: Simone Bollati

# Importazione delle librerie utilizzate all'interno del progetto
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import datetime
import sqlite3 as sqlite

class Sensore:
    # Costruttore del sensore
    def __init__(self, tipo, pin):
        self.tipo = tipo
        self.pin = pin

    # Ritorna il valore della temperatura
    def getTemperatura(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.tipo, self.pin)
        temp = float(temperature)
        return temp

    # Stampa la temperatura
    def printTemperatura(self, temp):
        print(temp)
