"""
* blynk GPIO 제어 및 PMS7003 데이터 수신 프로그램
* 수정 : 2024. 02. 07
* 제작 : eleparts 부설연구소
* SW ver. 2.0.0

> H/W 연결 참고
https://github.com/eleparts/iotkit/tree/master/hardware

GPIO 20 : LED
GPIO 21 : LED
GPIO 18 : RELAY
GPIO 16 : S/W

> Blynk 위젯 설정

V1 : Button /   MODE : SWITCH           - integer 0/1
V2 : Button /   MODE : SWITCH           - integer 0/1
V3 : Value Display                      - string
V4 : LED                                - integer 0/255
V5 : Button /   MODE : SWITCH           - integer 0/1
V6 : LED                                - integer 0/255
V7 : Value Display or Labeled Value     - string
V8 : Value Display or Labeled Value     - string
V9 : Value Display or Labeled Value     - string

기반 코드 및 필수 라이브러리 - blynk / python (Blynk Python Library V1.0.0)
https://github.com/vshymanskyy/blynk-library-python
"""

import BlynkLib
#import time
import serial
import RPi.GPIO as GPIO 
from PMS7003 import PMS7003
from BlynkTimer import BlynkTimer


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
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Create BlynkTimer Instance
timer = BlynkTimer()

# Create Dust sensor
dust = PMS7003()

# GPIO set
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(16,GPIO.IN, GPIO.PUD_DOWN)


# 부팅 시 서버 데이터 받아와 동기화 (LED SW 등)
@blynk.on("connected")
def blynk_connected():
    print("Updating V1,V2... values from the server...")
    blynk.sync_virtual(1,2,5)

# Virtual 핀 변경사항 터미널에 출력 - 디버그
@blynk.on("V*")
def blynk_handle_vpins(pin, value):
    print("V{} value: {}".format(pin, value))


# Register Virtual Pins
# blynk앱에서 버튼 누를경우 동작 (LED) - write (Virtual Pins 1)
@blynk.on("V1")
def handler_V1(value):
    if(value == ['1']):
        GPIO.output(21, 1)
    else:
        GPIO.output(21, 0)

# blynk앱에서 버튼 누를경우 동작 (LED) - write (Virtual Pins 2)
@blynk.on("V2")
def handler_V2(value):
    if(value == ['1']):
        GPIO.output(20, 1)
    else:
        GPIO.output(20, 0)

# blynk앱에서 버튼 누를경우 동작 (RELAY) - write (Virtual Pins 5)
@blynk.on("V5")
def handler_V5(value):
    if(value == ['1']):
        GPIO.output(18, 1)
    else:
        GPIO.output(18, 0)


# 타이머 사용해 주기적으로 GPIO 읽어 변경 시 blynk앱으로 전송 - (Virtual Pins 3)
@blynk.on("V3")
def handler_V3():
    SW = GPIO.input(16)

    try:  
        if(SW != handler_V3.lastSW):
            print("SW GPIO value : %d "% (SW))

            if(SW):
                blynk.virtual_write(3, " ON")
                handler_V3.lastSW = SW
                
            else:
                blynk.virtual_write(3, "OFF")
                handler_V3.lastSW = SW

    # 최초 1회 - 스위치 기존 value값 저장용 변수 선언
    except AttributeError:
        handler_V3.lastSW = False



# 1회성 타이머 테스트용 함수 - 최초 1회 구동
def hello_world():
    print("Hello World!")


# 타이머로 LED 주기적 깜빡임 제어 - LED ON/OFF (Virtual Pins 4)
@blynk.on("V4")
def LED_task():

    try:
        if(LED_task.LED_flag):
            blynk.virtual_write(4, 255)   # Vpin =  4, value = 255
            LED_task.LED_flag = False
            #print("V4 LED ON")
        else:
            blynk.virtual_write(4, 0)     # Vpin =  4, value = 0
            LED_task.LED_flag = True
            #print("V4 LED OFF")

    # 최초 1회 변수 선언
    except AttributeError:
        LED_task.LED_flag = True
        blynk.virtual_write(4, 255)
        #print("V4 LED ON")


# PMS 먼지센서 정보 읽은 후 데이터 연동 함수 - 하단 타이머로 실행
# V7,V8,V9
def send_pms_data():
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
        # Display Value
        #blynk.virtual_write(7, ("PM1.0 : " + str(data[dust.DUST_PM1_0_ATM])))
        #blynk.virtual_write(8, ("PM2.5 : " + str(data[dust.DUST_PM2_5_ATM])))
        #blynk.virtual_write(9, ("PM10  : " + str(data[dust.DUST_PM10_0_ATM])))

        blynk.virtual_write(6,'0')

    else: 
        # protocol_chk fail
        
        print("data Err")
        blynk.virtual_write(6,'255')


# Add Timers
# timer : 설정해 둔 시간마다 실행됨
timer.set_timeout(1, hello_world)       # 최초 1회, 1초후 실행
timer.set_interval(1, handler_V3)       # 1초마다 반복실행
timer.set_interval(3, LED_task)         # 3초마다 반복실행
timer.set_interval(2, send_pms_data)    # 2초마다 반복실행


# Start Blynk, Start timer
while True:
    blynk.run()
    timer.run()