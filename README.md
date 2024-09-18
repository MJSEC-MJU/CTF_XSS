# CTF_XSS

# 서버설치 단계
sudo apt update
sudo apt install docker.io
sudo systemctl enable --now docker

git clone https://github.com/MJSEC-MJU/CTF_XSS.git
cd CTF_XSS

# 가상환경설정
sudo apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate

# scretkey 생성
python -c 'import secrets; print(secrets.token_urlsafe(50))'
요거를 settings에 비밀키 넣기

# pylog/settings.py   allowed_hosts 설정 바꾸기
ALLOWED_HOSTS = ["your_domain"]

# 도커 컨테이너 실행
docker-compose build
docker-compose up -d