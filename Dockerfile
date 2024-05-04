# 使用 Python 官方映像作為基礎
FROM python:3.10-slim

# 設定工作目錄
WORKDIR /app

# 複製程式碼到容器中
COPY /web-crawler .

# 安裝相依套件
RUN pip install --no-cache-dir -r requirements.txt

# 執行爬蟲程式
CMD ["python", "./app/crawler.py"]