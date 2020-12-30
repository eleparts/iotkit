'''
# GPIO 동작 테스트 프로그램
# > 20,21번 GPIO에 연결된 LED 두개를 번갈아 가며 켜 줍니다. (5회 반복)
#
# 제작 : eleparts / yeon
'''
import RPi.GPIO as GPIO
import time

# GPIO 설정
GPIO.setmode(GPIO.BCM)

# LED가 연결된 GPIO번호
LED_A = 20 # 초록색
LED_B = 21 # 빨간색

# LED가 연결돤 GPIO 출력 핀으로 설정 
GPIO.setup(LED_A, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)

# 5회 반복
for i in range(5): 

    # LED A 켜기, LED B 끄기
    GPIO.output(LED_A , True)
    GPIO.output(LED_B , False)

    # 1초 대기
    time.sleep(1)

    # LED A 켜기, LED B 끄기
    GPIO.output(LED_A , False)
    GPIO.output(LED_B , True)

    # 1초 대기
    time.sleep(1)


# GPIO 설정 초기화
GPIO.cleanup()
