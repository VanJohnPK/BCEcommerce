# 使用官方的 Python 镜像作为基础镜像
FROM python:3.11

# 设置工作目录
WORKDIR /app

# 将当前目录内容复制到工作目录
COPY . /app

# 安装项目依赖
RUN pip install -r requirements.txt

# 暴露Django开发服务器的端口
EXPOSE 8000

# 运行Django开发服务器
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
