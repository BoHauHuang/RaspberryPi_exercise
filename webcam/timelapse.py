import schedule
import time

def job():
	print("executing code")

schedule.every().minute.at(":00").do(job)

try:
	while True:
		schedule.run_pending()
		time.sleep(1)
except KeyboardInterrupt:
	print("Exit")
