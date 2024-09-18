# CTF_XSS

## 서버 설치 단계
1. 시스템 패키지 업데이트 및 Docker 설치:
    ```sh
    sudo apt update
    sudo apt install docker.io
    sudo systemctl enable --now docker
    ```

2. 프로젝트 클론:
    ```sh
    git clone https://github.com/MJSEC-MJU/CTF_XSS.git
    cd CTF_XSS
    ```

## 가상환경 설정
1. Python 가상환경 설치:
    ```sh
    sudo apt-get install python3-venv
    python3 -m venv venv
    source venv/bin/activate
    ```

2. Secret Key 생성:
    ```sh
    python -c 'import secrets; print(secrets.token_urlsafe(50))'
    ```
    생성된 Secret Key를 `settings.py` 파일의 `SECRET_KEY` 변수에 추가합니다.

3. `pylog/settings.py` 파일에서 `ALLOWED_HOSTS` 설정 변경:
    ```python
    ALLOWED_HOSTS = ["your_domain"]
    ```

## 도커 컨테이너 실행
1. Docker Compose 빌드 및 실행:
    ```sh
    docker-compose build
    docker-compose up -d
    ```

이제 프로젝트가 Docker 컨테이너에서 실행됩니다.
