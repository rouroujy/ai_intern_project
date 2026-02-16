FROM python:3.10-slim

WORKDIR /app

# 复制项目文件
COPY . /app

# 如果未来有依赖可以启用
RUN pip install --no-cache-dir -r requirements.txt || true

# 设置默认启动命令
ENTRYPOINT ["python", "-m", "app.main"]
CMD ["data/sample.txt"]
