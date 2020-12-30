'''
# GPIO 동작 테스트 프로그램
# > 18번 GPIO에 연결된 릴레이보드를 5초간 켜 줍니다.
# #
# 제작 : eleparts / yeon
'''
import RPi.GPIO as GPIO
import time

# GPIO 설정
GPIO.setmode(GPIO.BCM)

# 릴레이보드가 연결된 GPIO번호
RELAY = 18

# 릴레이보드가 연결돤 GPIO 출력 핀으로 설정 
GPIO.setup(RELAY, GPIO.OUT)


# 릴레이 켜기 
GPIO.output(RELAY , True)

# 5초 대기
time.sleep(5)

# 릴레이 끄기 
GPIO.output(RELAY , False)

# 5초 대기
time.sleep(5)

# GPIO 설정 초기화
GPIO.cleanup()
