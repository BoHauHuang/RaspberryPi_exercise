import RPi.GPIO as GPIO
import time

TRIGGER_PIN = 16
ECHO_PIN = 18
LED_PIN = 22

temperature = 25
v = 331+0.6*temperature

GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

def blink(duration):
    timer = 0
    while timer <= 2*duration:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(duration)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(duration)

def measure():
    GPIO.output(TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIGGER_PIN, GPIO.LOW)
    pluse_start = time.time()
    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == GPIO.HIGH:
        pulse_end = time.time()
    
    t = pulse_end - pulse_start
    d = t*v/2

    return d*100

while True:
    distance = measure()
    print distance
    if distance < 30:
        for i in range(2):
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(0.1)
    elif distance < 100 and distance >= 30:
        for i in range(2):
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(0.3)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)

GPIO.cleanup()
