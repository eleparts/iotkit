'''
# 스위치 동작 테스트 프로그램
# > 16번 핀에 연결된 스위치가 눌릴때까지 대기하다가 스위치가 눌리면 LED를 켜 줍니다.
# >> 21번에 연결된 LED는 프로그램이 동작하면 항상 켜지고, 20번핀에 연결된 LED는 스위치가 눌리면 3초간 켜집니다.
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

# 스위치가 연결된 GPIO번호
SW = 16

# LED가 연결돤 GPIO 출력 핀으로 설정
GPIO.setup(LED_A, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)

# LED A 끄기, LED B 켜기
GPIO.output(LED_A , False)
GPIO.output(LED_B , True)

# 스위치가 연결된  GPIO를 입력 핀으로 설정 / 풀다운(기본값 LOW로 설정)
GPIO.setup(SW, GPIO.IN, GPIO.PUD_DOWN)

# 스위치 읽기
read_PIN = GPIO.input(SW)

# SW핀이 눌리지 않은 상태인 경우 스위치가 눌러질때까지 대기하며 0.3초마다 SW정보 읽기
while not read_PIN:

    # 0.3초 대기
    time.sleep(0.3)

    # 스위치 읽기
    read_PIN = GPIO.input(SW)


# LED A, B 켜기
GPIO.output(LED_A , True)
GPIO.output(LED_B , True)

# 3초 대기
time.sleep(3)

# LED 끄기
GPIO.output(LED_A , False)
GPIO.output(LED_B , False)

# GPIO 설정 초기화
GPIO.cleanup()
