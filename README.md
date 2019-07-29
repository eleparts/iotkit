# eleparts - 라즈베리파이 IOT KIT V2.0 예제  
  
본 저장소는 [라즈베리파이 IOT키트 V2.0](https://www.eleparts.co.kr/EPXMVGDB)의 예제 코드 및 관련 자료가 저장되어 있습니다.  
  
## 라즈베리파이 IOT키트 V2.0 예제코드 사용법
  
이하 예제 프로그램 사용을 위한 명령어 입니다.  
> git clone https://github.com/eleparts/iotkit  
> cd iotkit  
> chmod +x start.sh  
> ./start.sh  
  
본 저장소를 clone하여 다운로드 한 뒤 같이 다운로드 된 스크립트 파일을 실행하여 나머지 예제 및 라이브러리를 다운로드 해 줍니다.

추가로 blynk 예제를 실행하기 위해서 아래 명령어로 blynk 라이브러리를 다운로드 해 줍니다.
> pip3 install blynklib  
  
만일 권한 문제로 다운로드 되지 않으면 앞에 sudo 를 붙여 실행해 줍니다.
  
## start.sh  
  
예제코드, 라이브러리 등을 자동으로 다운로드/각 디렉터리에 배치시켜 주는 스크립트 입니다.
예제 사용을 위해 처음 1회 실행시켜 주시면 됩니다.  
  
## hardware  
  
하드웨어 연결 방법 안내 이미지 파일이 저장되어 있습니다.  
[hardware README로 이동](https://github.com/eleparts/iotkit/tree/master/hardware)  
  
각 핀은 중복 사용되지 않아 한번 연결한 핀을 다시 뽑지 않고 사용 가능합니다.  
  
## example  
  
GPIO 및 먼지센서 사용 테스트 예제가 저장되어 있습니다.  
먼지 센서 예제는 **start.sh**를 실행해 주셔야 다운로드됩니다.  
  
## blynk_examples
  
blynk를 응용해 같이 사용하는 예제 코드가 저장되어 있습니다.  
**start.sh**를 실행해 주셔야 다운로드됩니다.  
**start.sh** 실행 시 내부 http://blynk_python_GPIO_V2.py 예제코드는 GPIO 디렉터리로 자동으로 복사됩니다.  
  
## iotkit.py
  
IOTKIT에 포함된 먼지센서 및 릴레이보드, LED와 SW를 blynk를 이용해 제어하는 예제 코드 파일입니다.  
아래 사용자 가이드를 따라 실행 해 주시면 됩니다.  
  
## usermenual  
  
본 저장소의 예제코드 및 IOT KIT에 대한 사용법 가이드북입니다.  
- [사용자 가이드](https://www.eleparts.co.kr/data/_gextends/good-pdf/201907/good-pdf-7705965-2.pdf)  

## 참고자료 - 엘레파츠 블로그
  
- [라즈베리파이에서 blynk 파이썬 버전 사용하기 - 01.앱 다운로드 및 동작 테스트](https://blog.naver.com/elepartsblog/221590120617)  
  
- [라즈베리파이에서 blynk 파이썬 버전 사용하기 - 02. 스마트폰으로 GPIO 원격 제어하기](https://blog.naver.com/elepartsblog/221592159830)  
  
- [라즈베리파이에서 blynk 파이썬 버전 사용하기 - 03. 먼지센서 데이터를 스마트폰으로 받아보기](https://blog.naver.com/elepartsblog/221594252948)  
  
- [라즈베리파이용 3V 릴레이 사용하기](https://blog.naver.com/elepartsblog/221358322401)  
  
- [라즈베리파이에서 PMS7003 먼지센서 사용하기](https://blog.naver.com/elepartsblog/221347040698)  
  
