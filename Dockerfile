# 基础镜像
FROM registry.baidubce.com/paddlepaddle/paddle:2.1.3-gpu-cuda10.2-cudnn7
# 作者
LABEL author="katzhen"
# 暴露端口
EXPOSE 5000

COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY index.py ./

CMD ["python", "./index.py"]
