# coding=utf-8
# Copyright (c)
# Author: Simone Bollati

# Importazione delle librerie utilizzate all'interno del progetto
import Adafruit_DHT
import time
import datetime
import sqlite3 as sqlite
from Led2 import Led
from Condizionatore2 import Condizionatore
from Sensore2 import Sensore
from Database2 import Database
import threading
import Server2

# Setting variabili 
valoreMax = 27
pinSensore = 25
pinLed = 17
tipoSensore = Adafruit_DHT.DHT11
query = "INSERT INTO VALORI VALUES(?,?)"

# Setting connessione al DB
connessione=sqlite.connect("log.db")

# Creazione oggetti led, sensore, database, condizionatore
led = Led(pinLed, False)
sensore = Sensore(tipoSensore, pinSensore)
database = Database(connessione, connessione.cursor(), query)
condizionatore = Condizionatore(sensore, led, database, valoreMax)

# Setup Led
condizionatore.led.setup()

# Creazione e avvio del thread inerente al server
server=threading.Thread(target=Server2.avviaServer)
server.start()

# Istruzioni inerenti al processo di controllo temperatura
while True:
    # In temp andrà il valore istantaneo della temperatura
    temp = condizionatore.sensore.getTemperatura()
    # Stampa della temperatura
    condizionatore.sensore.printTemperatura(temp)
    # Settaggio variabili utilizzate dal DB
    cursore = condizionatore.database.getCursore()
    comandosql = condizionatore.database.getComandosql()

    # Se il valore della temperatura è maggiore uguale alla soglia verrà acceso il Led e verrà stampato un messaggio d'allarme, infine verrà effettuata una query 
    # di inserimento nel DB
    if(temp >= float(condizionatore.getValoreMax())):
        print(condizionatore.led.accendiLed())
        condizionatore.led.printAllarme()
        condizionatore.database.eseguiQuery(comandosql, condizionatore.getData(), temp)
        
    # Se il valore della temperatura è minore del valore soglia verrà spento il Led e stampato un messaggio di avviso
    if (temp < float(condizionatore.getValoreMax())):
        print(condizionatore.led.spegniLed())
        condizionatore.led.printAllarmeOK()
    # Attesa di 30 secondi prima di controllare nuovamente
    time.sleep(30)

