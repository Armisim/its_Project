# coding=utf-8
# Copyright (c)
# Author: Simone Bollati

# Importazione delle librerie utilizzate all'interno del progetto
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import datetime
import sqlite3 as sqlite

class Led:
    # Costruttore Led
    def __init__(self, pin, stato):
        self.pin = int(pin)
        self.stato = stato
        
    # Metodo i setup del Led
    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.OUT)

    # Metodo di accensione del Led
    def accendiLed(self):
        self.stato = True
        GPIO.output(self.pin, GPIO.HIGH)
        return self.stato

    # Metodo di spegnimento del Led
    def spegniLed(self):
        self.stato = False
        GPIO.output(self.pin, GPIO.LOW)
        return self.stato

    # Stampa dell'avviso di raggiungimento della temperatura limite
    def printAllarme(self):
        print("Temperatura limite raggiunta")

    # Avviso di temperatura entro la soglia prefissata
    def printAllarmeOK(self):
        print("Temperatura entro i limiti")
