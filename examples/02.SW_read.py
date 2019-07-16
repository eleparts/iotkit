import RPi.GPIO as GPIO
import time

# GPIO 설정
GPIO.setmode(GPIO.BCM)

# LED가 연결된 GPIO번호
LED_A = 20
LED_B = 21

# 스위치가 연결된 GPIO번호
SW = 16

# LED가 연결돤 GPIO 출력 핀으로 설정, LED 끄기
GPIO.setup(LED_A, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)

# LED A 끄기, LED B 켜기
GPIO.output(LED_A , False)
GPIO.output(LED_B , True)

# 스위치가 연결된  GPIO를 입력 핀으로 설정
GPIO.setup(SW, GPIO.IN, GPIO.PUD_DOWN)

# SW핀 기읽
read_PIN = GPIO.input(SW)

# SW핀이 눌리지 않은 상태인 경우 스위치가 눌러질때까지 대기하며 0.5초마다 SW정보 읽기
while not read_PIN:

  # 0.5초 대기
  time.sleep(0.5)

  # SW핀 읽기
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
