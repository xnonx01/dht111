import RPi.GPIO as GPIO
import dht11
import datetime
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup
while(1):
	now=datetime.datetime.now()
	date=now.strftime("%y-%m-%d: %H:%M:%s")
	ins=dht11.DHT11(pin=14)
	result=ins.read()
	print(now)
	print("Tem:%d c"%result.temperature)
	print("Hum:%d %%"% result.humidity)
	with open('pee.txt','a')as f:
		f.write("datetime:%s Hum:%d %%Tem :%d c\n"%(date,result.humidity,result.temperature))
		time.sleep(2)
