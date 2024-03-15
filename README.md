# eleparts - 라즈베리파이 IOT KIT V2.0 예제  
  
본 저장소는 [라즈베리파이 IOT키트 V2.0](https://www.eleparts.co.kr/EPXMVGDB)의 예제 코드 및 관련 자료가 저장되어 있습니다.  
  
## 라즈베리파이 IOT키트 V2.0 예제코드 사용법  
  
아래는 예제 프로그램 사용을 위한 설치 명령어 입니다.  

### IOT KIT 예제 다운로드 및 설치  

```bash
git clone https://github.com/eleparts/iotkit  
cd iotkit  
chmod +x start.sh  
./start.sh  
```
  
위 명령어로 본 저장소를 clone하여 다운로드 한 뒤 같이 다운로드 된 스크립트 파일을 실행하여 나머지 예제 및 라이브러리를 다운로드 해 줍니다.

### Blynk 사용을 위한 Blynk2.0 라이브러리 다운로드 및 설치  

라즈베리파이에서 blynk 예제를 실행하기 위해서는 아래 명령어로 blynk2.0용 라이브러리를 다운로드 후 설치해 주어야 합니다.  
※ pip명령 사용 시 구버전 라이브러리가 설치되므로 저장소를 직접 다운로드&설치합니다.  

**새로운 터미널 창을 열고(혹은 기본 경로로 이동 후)** 아래 명령어를 입력해 다운로드&설치를 해 줍니다.  
  
```bash
# 복제된 lynk-library-python 라이브러리
git clone https://github.com/eleparts/blynk-library-python
cd blynk-library-python
sudo python setup.py install
```  

[참조: blynk-library-python 원본 라이브러리 저장소](https://github.com/vshymanskyy/blynk-library-python)  

### 라즈베리파이5에서 사용을 위한 lgpio 설치  

라즈베리파이5를 사용한다면 아래 명령어로 pi5 호환 GPIO 라이브러리를 설치해 주어야 합니다.  

```bash
# 반드시 라즈베리파이 5 사용시에만 설치
pip install --break-system-packages rpi-lgpio
```
  
## start.sh  
  
예제코드, 라이브러리 등을 자동으로 다운로드/각 디렉터리에 배치시켜 주는 스크립트 입니다.  
예제 사용을 위해 처음 1회 실행시켜 주시면 됩니다.  
  
## hardware  
  
하드웨어 연결 방법 안내 이미지 파일이 저장되어 있습니다.  
[hardware README로 이동](https://github.com/eleparts/iotkit/tree/master/hardware)  
  
각 핀은 중복 사용되지 않아 한번 연결한 핀을 다시 뽑지 않고 사용 가능합니다.  
  
## example  
  
GPIO 및 먼지센서 사용 테스트 예제가 저장되어 있습니다.  
먼지 센서 예제는 **start.sh**를 실행할때 자동으로 다운로드됩니다.  

각 예제는 `python 예제코드.py`로 실행하면 됩니다.  
  
## blynk_examples  
  
blynk를 응용해 같이 사용하는 예제 코드가 저장되어 있습니다.  
위에 안내된 Blynk2.0 라이브러리를 설치해 주어야 사용 가능합니다.  

**start.sh**를 실행해 주셔야 다운로드됩니다.  
**start.sh** 실행 시 내부 blynk_python_GPIO_V2.py 예제코드는 GPIO 디렉터리로 자동으로 복사됩니다.  

각 예제는 코드의 `YourAuthToken`을 변경한 뒤 `python 예제코드.py`로 실행하면 됩니다.  

[AuthToken을 확인 가능한 Blynk 대시보드 페이지](https://blynk.cloud/dashboard/)  

## iotkit.py  
  
IOTKIT에 포함된 먼지센서 및 릴레이보드, LED와 SW를 blynk를 이용해 제어하는 전체 예제 코드 파일입니다.  

코드의 `YourAuthToken`을 변경한 뒤 `python iotkit.py`로 실행하면 됩니다.  
  
## usermenual  
  
본 저장소의 예제코드 및 IOT KIT에 대한 사용법 가이드북입니다.  

- [가이드북 - 기본교재](https://www.eleparts.co.kr/data/goods_attach/202403/good-pdf-7705965-2.pdf)  
  
## 참고자료 - 엘레파츠 블로그
  
- [라즈베리파이용 3V 릴레이 사용하기](https://blog.naver.com/elepartsblog/221358322401)  
  
- [라즈베리파이에서 PMS7003 먼지센서 사용하기](https://blog.naver.com/elepartsblog/221347040698)  
  