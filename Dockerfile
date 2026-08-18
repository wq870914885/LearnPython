FROM python:3.10
RUN python3 -m pip install numpy==1.26.4 matplotlib==3.8.4 -i https://pypi.tuna.tsinghua.edu.cn/simple
WORKDIR /opt/project