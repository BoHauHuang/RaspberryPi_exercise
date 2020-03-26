import RPi.GPIO as GPIO
import dht11
import time
import datetime

LED_PIN = 23

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# read data using pin 
instance = dht11.DHT11(pin=17)

try:
    while True:
        result = instance.read()
        if result.is_valid():
            print("Last valid input: " + str(datetime.datetime.now()))

            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)

        if result.temperature > 25:
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(1)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)

except KeyboardInterrupt:
    print("Cleanup")

finally:
    GPIO.cleanup()
