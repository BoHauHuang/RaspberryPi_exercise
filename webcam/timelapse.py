import picamera
import schedule
import time
import os

img_cnt = 1
camera = picamera.PiCamera()

def job():
	t = time.localtime()
	print("At %d:%d, start capturing...", t[3], t[4])
	camera.capture(str(img_cnt)+'.png')
	img_cnt+=1

schedule.every().minute.at(":00").do(job)

try:
	while True:
		schedule.run_pending()
		time.sleep(1)
except KeyboardInterrupt:
	print("Exit")