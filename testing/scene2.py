import RPi.GPIO as GPIO
import time

from firebase import firebase

firebase = firebase.FirebaseApplication('https://dj-hack.firebaseio.com', None)
# result = firebase.get('/dustbins/', None)

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

print "Distance Measurement In Progress"

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print "Waiting For Sensor To Settle"
time.sleep(2)

current_distance = 0

c = 10
while (c):
    time.sleep(2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)
    pd = round(100 - distance * 100 / 31, 2)

    print "Percentage:", pd, "%"


    #data3 => daddy1
    data3 = {'cash': 300, 'currentUser': '', 'parent': '', 'percentFull': pd, 'queryText': '','queryType': -1, 'streak': 0}
    data4 = {'cash': 300, 'currentUser': '', 'parent': '', 'percentFull': 0, 'queryText': '','queryType': -1, 'streak': 0}
    if (pd >= 80.0 ):
        data3 = {'cash': 270, 'currentUser': '', 'parent': '', 'percentFull': 100,
                 'queryText': 'Daddy1 wants to buy dustbin from Daddy2',
                 'queryType': 2, 'streak': 5}
        data4 = {'cash': 330, 'currentUser': '', 'parent': '', 'percentFull': 0,
                 'queryText': 'Daddy2 agrees to sell dustbin Daddy1',
                 'queryType': 2, 'streak': 0}

    firebase.put('/dustbins', "1518880087182", data3)
    firebase.put('/dustbins',"1518880134851",data4)
    c -= 1
GPIO.cleanup()
