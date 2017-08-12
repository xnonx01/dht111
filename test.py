import RPi.GPIO as GPIO
import dht11
import time
import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance = dht11.DHT11(pin = 13)
while(1):
	result = instance.read()
	now = datetime.datetime.now()
	date = now.strftime("%Y-%m-%d : %H:%M:%S")
	if result.is_valid():
		print("Temperature: %d C" % result.temperature)
		print("Humidity: %d %%" % result.humidity)
		print (date)
		time.sleep(2)
		with open ("kuy.txt" , "a") as f:
			f.write("datetime: %s Humid: %s %% Temp: %s c\n"%(date,result.humidity,result.temperature))
