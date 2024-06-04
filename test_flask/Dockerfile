# 베이스 이미지 설정
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요 패키지 설치
RUN apt-get update && apt-get install -y \
    libopencv-dev \
    && rm -rf /var/lib/apt/lists/*

# 파이썬 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 추가 패키지 설치
RUN pip install flask_cors

# 애플리케이션 파일 복사
COPY . .

# 포트 설정
EXPOSE 8080

# 컨테이너 시작 명령어 설정
CMD ["python", "private/app.py"]
