# cryptoauto
비트코인 자동매매 python

### VSCODE 설치
- https://youtu.be/kWiCuklohdY 보고 따라하기

### Python 설정
- https://www.python.org/downloads/ 에서 python 3.8.9 다운 및 파일 설치 시 c드라이브에 python38-64파일 만들어서 그곳에 다운.
- 파일 탐색기 내pc에서 우클릭, 속성 들어가서 시스템 창에서 고급 시스템 설정, 환경 변수, 시스템 변수에서 path 더블 클릭, python38-64wscriptw 를 가장 위에 설정
- vscode 실행 하여 새폴더 cryptoauto 생성, terminal cmd 로 전환 후 python 쳐서 버전 확인, vscode도 3.8.9로 맞춰줘야함
- https://github.com/sharebook-kr/pyupbit.git 에서 pyupbit library 가져오기
- test.py 파일 만들어서 import pyupbit 이후 로그인 및 잔고 조회 코드 가져오기

### 자동 매매 파일 세부 설명
- Ubuntu에서 instance 만들고 git clone 나의 레포지토리
- ls -al 통해 파일 확인
- cd cryptoauto 를 통해 파일 이동 및 ls -al로 vim bitcoinAutoTradeWithSlack.py 파일 불러오기
- 이때 슬랙 명은 crypto
- k값 수정 이후 저장(최적의 k값은 python 파일 중 bestk.py에서 구함)
- python3 bitcoinAutoTradeWithSlack.py로 파일 실행 
- ctrl + c 로 환경 나온 후 백그라운드 실행 및 확인

### Ubuntu 서버 명령어
- (*추가)한국 기준으로 서버 시간 설정: sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
- 현재 경로 상세 출력: ls -al
- 경로 이동: cd 경로
- vim 에디터로 파일 열기: vim bitcoinAutoTrade.py
- vim 에디터 입력: i
- vim 에디터 저장: :wq!
- 패키지 목록 업데이트: sudo apt update
- pip3 설치: sudo apt install python3-pip
- pip3로 pyupbit 설치: pip3 install pyupbit
- 백그라운드 실행: nohup python3 bitcoinAutoTrade.py > output.log &
- 실행되고 있는지 확인: ps ax | grep .py
- 프로세스 종료(PID는 ps ax | grep .py를 했을때 확인 가능): kill -9 PID


### Windows 인공지능 (Prophet) 자동매매 환경 설치 방법
- 아나콘다(https://www.anaconda.com/) 설치
- pip install pyupbit
- pip install schedule
- conda install -c conda-forge fbprophet
- pip install pystan --upgrade

### Ubuntu 20.4 인공지능 (Prophet) 자동매매 환경 설치 방법
- 4GB이상 RAM 필요 (AWS t2.medium 이상)
- sudo apt update
- sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
- sudo apt install python3-pip
- pip3 install pyupbit
- pip3 install schedule
- pip3 install pystan==2.19.1.1
- pip3 install convertdate
- pip3 install fbprophet
