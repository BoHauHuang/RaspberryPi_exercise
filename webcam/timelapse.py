import picamera
import schedule
import time
import os

img_cnt = 1
camera = picamera.PiCamera()

def job():
	global img_cnt
        t = time.localtime()
        print("At "+str(t[3])+":"+str(t[4])+", start capturing...")
	camera.capture(str(img_cnt)+'.png')
	img_cnt+=1

schedule.every().minute.at(":00").do(job)

try:
	while True:
		schedule.run_pending()
		time.sleep(1)
except KeyboardInterrupt:
	print("Exit")
