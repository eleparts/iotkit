"""
* blynk GPIO 제어 및 PMS7003 데이터 수신 프로그램
* 수정 : 2019. 07. 26
* 제작 : eleparts 부설연구소
* SW ver. 0.9.0

> H/W 연결 참고
https://github.com/eleparts/iotkit/tree/master/hardware

GPIO 20 : LED 
GPIO 21 : LED
GPIO 18 : RELAY
GPIO 16 : S/W

> Blynk 위젯 설정

V1 : Button / MODE : SWITCH
V2 : Button / MODE : SWITCH
V3 : Value Display / READING RATE : 1sec
V4 : LED
V5 : Button / MODE : SWITCH
V6 : LED
V7 : Value Display or Labeled Value / READING RATE : PUSH
V8 : Value Display or Labeled Value / READING RATE : PUSH
V9 : Value Display or Labeled Value / READING RATE : PUSH

기반 코드 및 필수 라이브러리 - blynk / python (Blynk Python Library V0.2.4)
https://github.com/blynkkk/lib-python
"""

import blynklib
import blynktimer
import time
import serial
import RPi.GPIO as GPIO 
from PMS7003 import PMS7003


#이메일로 받은 토큰을 여기에 추가
BLYNK_AUTH = 'YourAuthToken'

#========================================
# Baud Rate
Speed = 9600

# UART / USB Serial
USB0 = '/dev/ttyUSB0'
UART = '/dev/ttyAMA0'

# USE PORT  
SERIAL_PORT = USB0  #기본값 USB0, 연결방식에 맞춰 변경

#serial setting 
ser = serial.Serial(SERIAL_PORT, Speed, timeout = 1)
#========================================

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

# Create BlynkTimer Instance
timer = blynktimer.Timer()

# Create Dust sensor
dust = PMS7003()

# GPIO set
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(16,GPIO.IN, GPIO.PUD_DOWN)

WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"
READ_PRINT_MSG = "[READ_VIRTUAL_PIN_EVENT] Pin: V{}"


# Register Virtual Pins
# blynk앱에서 버튼 누를경우 동작 - write (Virtual Pins 1)
@blynk.handle_event('write V1')
def write_virtual_pin_handler(pin, value):
  print(WRITE_EVENT_PRINT_MSG.format(pin,value))

  if(value == ['1']):
    GPIO.output(21, 1)
  else:
    GPIO.output(21, 0)

# blynk앱에서 버튼 누를경우 동작 - write (Virtual Pins 2)
@blynk.handle_event('write V2')
def write_virtual_pin_handler(pin, value):
  print(WRITE_EVENT_PRINT_MSG.format(pin,value))

  if(value == ['1']):
    GPIO.output(20, 1)
  else:
    GPIO.output(20, 0)


# blynk앱에서 주기적으로 호출하도록 설정 - Read (Virtual Pins 3)
@blynk.handle_event('read V3')
def read_virtual_pin_handler(pin):
  
  SW = GPIO.input(16)

  try:  
    if(SW != read_virtual_pin_handler.lastSW):
      print(READ_PRINT_MSG.format(pin))
      print("SW GPIO value : %d "% (SW))

      if(SW):
        blynk.virtual_write(3, " ON")
        read_virtual_pin_handler.lastSW = SW
        
      else:
        blynk.virtual_write(3, "OFF")
        read_virtual_pin_handler.lastSW = SW

  # 최초 1회 - 스위치 기존 value값 저장용 변수 선언
  except AttributeError:
    read_virtual_pin_handler.lastSW = False


# blynk앱에서 버튼 누를경우 동작 - write (Virtual Pins 5)
@blynk.handle_event('write V5')
def write_virtual_pin_handler(pin, value):
  print(WRITE_EVENT_PRINT_MSG.format(pin,value))

  if(value == ['1']):
    GPIO.output(18, 1)
  else:
    GPIO.output(18, 0)


# Add Timers
# timer : 설정해 둔 시간마다 실행됨
@timer.register(interval=1, run_once=True) # 최초 1회, 1초후 실행
def hello_world():
  print("Hello World!")


@timer.register(interval=2, run_once=False) # 2초마다 반복실행
def my_user_task():

  try:
    if(my_user_task.LED_flag):
      blynk.virtual_write(4, 255)   # Vpin =  V4, value = 255
      my_user_task.LED_flag = False
      #print("V4 LED ON")
    else:
      blynk.virtual_write(4, 0)     # Vpin =  V4, value = 0
      my_user_task.LED_flag = True
      #print("V4 LED OFF")

  # 최초 1회 변수 선언
  except AttributeError:
    my_user_task.LED_flag = True
    blynk.virtual_write(4, 255)
    #print("V4 LED ON")


@timer.register(interval=5, run_once=False) # 5초마다 반복실행
def my_user_task_2():
  # do any non-blocking operations
  
  ser.flushInput()
  buffer = ser.read(1024)

  if(dust.protocol_chk(buffer)):
    data = dust.unpack_data(buffer)

    print("send - PM1.0: %d | PM2.5: %d | PM10: %d" %(data[dust.DUST_PM1_0_ATM],data[dust.DUST_PM2_5_ATM],data[dust.DUST_PM10_0_ATM]) )
    # Labeled Value (Display)
    blynk.virtual_write(7, data[dust.DUST_PM1_0_ATM])
    blynk.virtual_write(8, data[dust.DUST_PM2_5_ATM])
    blynk.virtual_write(9, data[dust.DUST_PM10_0_ATM])
    # Value Display
    #blynk.virtual_write(7, ("PM1.0 : " + str(data[dust.DUST_PM1_0_ATM])))
    #blynk.virtual_write(8, ("PM2.5 : " + str(data[dust.DUST_PM2_5_ATM])))
    #blynk.virtual_write(9, ("PM10  : " + str(data[dust.DUST_PM10_0_ATM])))
    
    blynk.virtual_write(6,'0')
    
  else: 
    # protocol_chk fail
    
    print("data Err")
    blynk.virtual_write(6,'255')
  

# Start Blynk, Start timer
while True:
  blynk.run()
  timer.run()