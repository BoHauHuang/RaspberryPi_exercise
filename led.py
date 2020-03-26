import RPi.GPIO as gpio
import time

LED_PIN = 3
gpio.setmode(gpio.BOARD)
gpio.setup(LED_PIN, gpio.OUT)

try:
    while 1:
        print("LED on")
        gpio.output(LED_PIN, gpio.HIGH)
        time.sleep(1)
        print("LED off")
        gpio.output(LED_PIN, gpio.LOW)
        time.sleep(1)
except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

finally:
    gpio.cleanup()
