import RPi.GPIO as GPIO
import time
import Adafruit_SSD1306
import datetime
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(6,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)
u=0
l=0
x=0

from PIL import Image,ImageDraw,ImageFont

RST=1

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

disp.begin()
disp.clear()

while 1:
	while x:
		now=datetime.datetime.now()
		now1=now.strftime("%H::%M:%S")
		now2=now.strftime("%d-%m-%Y")
		width=disp.width
		height=disp.height
		image=Image.new('1',(width,height))
		draw=ImageDraw.Draw(image)
		font=ImageFont.truetype('VCR_OSD_MONO_1.001.ttf',22)
		draw.text((0,0),'Date/time',font=font,fill=1)
		draw.text((0,20), now1,font=font,fill=1)
		draw.text((0,40),now2,font=font,fill=1)
		disp.image(image)
		disp.display()
		if not GPIO.input(22):
			while not GPIO.input(22):
				pass
			x=0
			u=0
			l=0
	while not x:
        
		if not GPIO.input(6):
			while not GPIO.input(6):
				pass
			u-=1
			if u<0:
				u=0
		if not GPIO.input(23):
			while not GPIO.input(23):
				pass
			u+=1
			if u>3:
				u=3
		if not GPIO.input(18):
			while not GPIO.input(18):
				pass
			l=1
		if not GPIO.input(17):
			while not GPIO.input(17):
				pass
			l=0
		if not GPIO.input(22):
			while not GPIO.input(22):
				pass
			x=1
		if l==0 and u==0:
			width=disp.width
			height=disp.height
			image=Image.new('1',(width,height))
			draw=ImageDraw.Draw(image)
			font=ImageFont.truetype('VCR_OSD_MONO_1.001.ttf',22)
			draw.text((0,0),'>Antman',font=font,fill=1)
			draw.text((0,20),'Ironman',font=font,fill=1)
			draw.text((0,40),'Spiderman',font=font,fill=1)
			disp.image(image)
			disp.display()
		if l==0 and u==1:
			width=disp.width
			height=disp.height
			image=Image.new('1',(width,height))
			draw=ImageDraw.Draw(image)
			font=ImageFont.truetype('VCR_OSD_MONO_1.001.ttf',22)
			draw.text((0,0),'Antman',font=font,fill=1)
			draw.text((0,20),'>Ironman',font=font,fill=1)
			draw.text((0,40),'Spiderman',font=font,fill=1)
			disp.image(image)
			disp.display()
		if l==0 and u==2:
			width=disp.width
			height=disp.height
			image=Image.new('1',(width,height))
			draw=ImageDraw.Draw(image)
			font=ImageFont.truetype('VCR_OSD_MONO_1.001.ttf',22)
			draw.text((0,0),'Antman',font=font,fill=1)
			draw.text((0,20),'Ironman',font=font,fill=1)
			draw.text((0,40),'>Spiderman',font=font,fill=1)
			disp.image(image)
			disp.display()
		if l==0 and u==3:
			width=disp.width
			height=disp.height
			image=Image.new('1',(width,height))
			draw=ImageDraw.Draw(image)
			font=ImageFont.truetype('VCR_OSD_MONO_1.001.ttf',22)
			draw.text((0,0),'Ironman',font=font,fill=1)
			draw.text((0,20),'Spiderman',font=font,fill=1)
			draw.text((0,40),'>Superman',font=font,fill=1)
			disp.image(image)
			disp.display()
		if l==1 and u==3:
			width=disp.width
			height=disp.height
			image=Image.new('1',(width,height))
			draw=ImageDraw.Draw(image)
			font=ImageFont.truetype('VCR_OSD_MONO_1.001.ttf',22)
			draw.text((0,0),'>Superman',font=font,fill=1)
			draw.text((0,20),'in 8:30',font=font,fill=1)
			draw.text((0,40),'out 16:30',font=font,fill=1)
			disp.image(image)
			disp.display()
		if l==1 and u==2:
			width=disp.width
			height=disp.height
			image=Image.new('1',(width,height))
			draw=ImageDraw.Draw(image)
			font=ImageFont.truetype('VCR_OSD_MONO_1.001.ttf',22)
			draw.text((0,0),'>Spiderman',font=font,fill=1)
			draw.text((0,20),'in 8:30',font=font,fill=1)
			draw.text((0,40),'out 16:30',font=font,fill=1)
			disp.image(image)
			disp.display()
		if l==1 and u==1:
			width=disp.width
			height=disp.height
			image=Image.new('1',(width,height))
			draw=ImageDraw.Draw(image)
			font=ImageFont.truetype('VCR_OSD_MONO_1.001.ttf',22)
			draw.text((0,0),'>Ironman',font=font,fill=1)
			draw.text((0,20),'in 7:30',font=font,fill=1)
			draw.text((0,40),'out 16:00',font=font,fill=1)
			disp.image(image)
			disp.display()
		if l==1 and u==0:
			width=disp.width
			height=disp.height
			image=Image.new('1',(width,height))
			draw=ImageDraw.Draw(image)
			font=ImageFont.truetype('VCR_OSD_MONO_1.001.ttf',22)
			draw.text((0,0),'>Antman',font=font,fill=1)
			draw.text((0,20),'in 7:00',font=font,fill=1)
			draw.text((0,40),'out 16:20',font=font,fill=1)
			disp.image(image)
			disp.display()										
			
				
								
		
		
		




