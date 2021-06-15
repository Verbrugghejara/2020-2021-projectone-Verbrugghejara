from bluedot.btcomm import BluetoothClient
import datetime
import threading
import time
from flask_cors import CORS
from flask_socketio import SocketIO
from flask import Flask, jsonify, request
from typing import Counter
from repositories.DataRepository import DataRepository
from helpers import temperatuur
from RPi import GPIO
from helpers import LCD_pcf
from subprocess import check_output
from helpers.zhx711 import HX711
GPIO.setmode(GPIO.BCM)



app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hier mag je om het even wat schrijven, zolang het maar geheim blijft en een string is'
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)

# ----------------------------lcd---------------------------------
def lcd_functie():
    mylcd = LCD_pcf.lcd()
    ips = str(check_output(["hostname", "--all-ip-addresses"]))
    ips = ips.replace("b","").replace("'","")
    wlan = ips.split(" ")
    tekst = "The easy cat set"
    mylcd.lcd_display_string(tekst, 1)
    mylcd.lcd_display_string(wlan[1], 2)

# ----------------------------esp---------------------------------
def data_received(data):
    print("recv - {}".format(data))
    if data == 'T':
        today = datetime.datetime.now()
        print(today)
        datum = today.strftime('%Y-%m-%d')
        print(datum)
        tijd = today.strftime('%H:%M:%S')
        print(tijd)
        DataRepository.create_kattenluik(datum, tijd)
        print('er is een nieuwe kattenluik toegevoegd')



def setup():
    # ----------------------------set gram bakjes---------------------------------
    gewichtdrink = DataRepository.read_gewicht_drinkbak()
    gewichtvoer = DataRepository.read_gewicht_voerbak()
    print(gewichtdrink)
    print(gewichtvoer)
    for drink in gewichtdrink:
        gewichtdrink = drink['gewicht_drinkbak']
        print(gewichtdrink)

    for voer in gewichtvoer:
        gewichtvoer = voer['gewicht_voerbak']
        print(gewichtvoer)
    socketio.emit('B2F_set_gram', {
                  'gewichtdrink': gewichtdrink, 'gewichtvoer': gewichtvoer})

# ----------------------------gewicht---------------------------------
    today = datetime.datetime.now()
    now = today.strftime('%Y-%m-%d')
    nowtime = today.strftime('%H:%M:%S')
    # print('gewicht')
    print('voer')
    voerbak = HX711(27, 22)
    print('drinken')
    drinkbak = HX711(13, 19)
    drinkbak.set_reading_format("MSB", "MSB")
    voerbak.set_reading_format("MSB", "MSB")
    drinkbak.set_reference_unit(476.623563352)
    voerbak.set_reference_unit(457.42495126)
    # drinkbak.reset()
    # voerbak.reset()

    # drinkbak.tare()
    # voerbak.tare()
    # print('plaats een gewicht')
    # time.sleep(5)
    # print('meten...')
    gewicht_drinkbak = drinkbak.get_weight(7)
    gewicht_voerbak = voerbak.get_weight(7)  # eten
    gewicht_drinkbak = gewicht_drinkbak-gewichtdrink-406 # drinkeen
    gewicht_voerbak = gewicht_voerbak-gewichtvoer-67.8
    print('drinkbak')
    print(gewicht_drinkbak)
    print(gewicht_voerbak)
    socketio.emit('B2F_gewichten', {
                  'gewicht1': gewicht_drinkbak, 'gewicht2': gewicht_voerbak})

# ----------------------------temperatuur---------------------------------
    today = datetime.datetime.now()
    now = today.strftime('%Y-%m-%d')
    nowtime = today.strftime('%H:%M:%S')
    id = DataRepository.create_bak(
        None, None, temperatuur.temperatuur.start(), now, nowtime)
    data = DataRepository.read_temp(id)
    socketio.emit('B2F_new_temp', {'temperatuur': data})
# ----------------------------detectie---------------------------------
    dataMotionLast = DataRepository.read_last_kattenluik()
    for el in dataMotionLast:
        print('motion')
        print(el['datum'])
        print(el['tijd'])
    tijd = el['tijd']
    datum = el['datum']
    socketio.emit('B2F_motion_detect', {
                  'datum': str(datum), 'tijd': str(tijd)})
    # motion all ----------------------------
    dataMotionAll = DataRepository.read_all_kattenluik()

    for el in dataMotionAll:
        tijd2 = el['tijd']
        datum2 = el['datum']
        socketio.emit('B2F_motion_all', {
            'datum': str(datum2), 'tijd': str(tijd2)})

    lcd_functie()
    print('setup klaar')


# ----------------------------servo kattenluik---------------------------------
knopservo =25
GPIO.setup(knopservo, GPIO.IN, pull_up_down=GPIO.PUD_UP)
servo = 18
global tellerservo
tellerservo = 0
GPIO.setup(servo, GPIO.OUT)
servo = GPIO.PWM(servo, 50)


servo.ChangeDutyCycle(1)
def buttonfalling(channel):
    print(GPIO.input(knopservo))
    servo.start(1)
    if channel is 25:
        global tellerservo
        print('open')
        servo.ChangeDutyCycle(6)
        time.sleep(0.25)
        tellerservo += 1
        if tellerservo == 1:
            tellerservo = 0
            # time.sleep(0.25)
            servo.ChangeDutyCycle(1)
            print('toe')
    


GPIO.add_event_detect(knopservo, GPIO.BOTH,
                      callback=buttonfalling, bouncetime=150)




# API ENDPOINTS

endpoint = '/api/v1'


@app.route(endpoint + '/gewicht/drinken', methods=['GET'])
def get_gewichten_drinken():
    if request.method == 'GET':
        return jsonify(gewicht_drinken=DataRepository.read_gewicht_van_drinken()), 200


@app.route(endpoint + '/gewicht/voer', methods=['GET'])
def get_gewichten_voer():
    if request.method == 'GET':
        return jsonify(gewicht_voer=DataRepository.read_gewicht_van_voer()), 200


@app.route(endpoint + '/temperatuur', methods=['GET', 'POST'])
def get_last_temperatuur():
    if request.method == 'GET':
        return jsonify(temperatuur=DataRepository.read_last_temperatuur()), 200
    elif request.method == 'POST':
        today = datetime.datetime.now()
        now = today.strftime('%Y-%m-%d')
        nowtime = today.strftime('%H:%M:%S')
        print(temperatuur.temperatuur.start())
        return jsonify(BakID=DataRepository.create_bak(None, None, temperatuur.temperatuur.start(), now, nowtime)), 200


@app.route(endpoint + '/temperatuur/<tempID>', methods=['GET'])
def get_temp(tempID):
    if request.method == 'GET':
        return jsonify(temperatuur=DataRepository.read_temp(tempID))

# SOCKET IO


@socketio.on('F2B_gewicht_bak')
def gewicht_bakken(json):
    drinkbak = json['Gewicht_drinkbak']
    voerbak = json['Gewicht_voerbak']
    print(drinkbak)
    print(voerbak)
    DataRepository.update_gewicht_drinkbak(drinkbak, voerbak)


@socketio.on('connect')
def initial_connection():
    print('A new client connects')
    setup()

# ----------------------------servo optie---------------------------------

servo_actie = None

@socketio.on('F2B_keuze')
def keuze_kattenluik(dict):
    global servo_actie
    print('er is een nieuwe keuze')
    print(dict['KattenluikOptieID'])
    print(dict['Optie'])
    servo_actie = dict['Optie']
    # print("Connecting")
    # BTserial.send(dict['Optie'])
    # BTserial.send('\n')

# ----------------------------thread---------------------------------

def current_weight():
    print('*** reset gewicht ***')

    gewichtdrink = DataRepository.read_gewicht_drinkbak()
    gewichtvoer = DataRepository.read_gewicht_voerbak()
    for drink in gewichtdrink:
        gewichtdrink = drink['gewicht_drinkbak']

    for voer in gewichtvoer:
        gewichtvoer = voer['gewicht_voerbak']
    
    today = datetime.datetime.now()
    datum = today.strftime('%Y-%m-%d')
    tijd = today.strftime('%H:%M:%S')
    drinkbak = HX711(5, 6)
    voerbak = HX711(27, 22)
    drinkbak.set_reading_format("MSB", "MSB")
    voerbak.set_reading_format("MSB", "MSB")
    drinkbak.set_reference_unit(476.623563352)
    voerbak.set_reference_unit(457.42495126)
    gewicht_drinkbak = drinkbak.get_weight(5)
    gewicht_voerbak = voerbak.get_weight(5)
    gewicht_drinkbak = gewicht_drinkbak-gewichtdrink-406 # drinkeen
    gewicht_voerbak = gewicht_voerbak-gewichtvoer-67.8
    print(gewicht_drinkbak)
    print(gewicht_voerbak)
    print('reset done')
    DataRepository.create_bak(1,gewicht_drinkbak,None,datum,tijd)
    DataRepository.create_bak(2,gewicht_voerbak,None,datum,tijd)
    id = DataRepository.create_bak(1,4.44,temperatuur.temperatuur.start(),datum,tijd)
    data = DataRepository.read_temp(id)
    # print(data)


def read_pir():
    global servo_actie
    BTserial = BluetoothClient("esp", data_received)
    print('connected')

    # serial connectie

    start_time_weight = 0
    current_time_weight = 0
    start_time_temp = 0
    current_time_temp = 0
    while True:
        current_time_weight = current_time_weight + 1
        current_time_temp = current_time_temp + 1
        if (servo_actie is not None):
            print("Servo actie: " + servo_actie)
            BTserial.send(servo_actie)
            BTserial.send('\n')
            servo_actie = None

        BTserial.send("pir")
        onnodig = 'onnodig ' + str(current_time_weight)
        print(onnodig)
        time.sleep(1)
        if current_time_weight - start_time_weight > 900:  # (in minuten bvb-
            start_time_weight = current_time_weight
            current_weight()
        if current_time_temp - start_time_temp > 3600:
            start_time_temp = current_time_temp
            today = datetime.datetime.now()
            now = today.strftime('%Y-%m-%d')
            nowtime = today.strftime('%H:%M:%S')
            DataRepository.create_bak(
                None, None, temperatuur.temperatuur.start(), now, nowtime)


t1 = threading.Thread(target=read_pir)
t1.start()
#threading.Timer(3600, current_weight).start()

if __name__ == '__main__':
    socketio.run(app, debug=False, host='0.0.0.0')
