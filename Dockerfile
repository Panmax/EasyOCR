FROM python:3.6

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /tmp/ocr
RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
COPY . /code/

EXPOSE 5000
CMD gunicorn -b 0.0.0.0:5000 app:app -w 2 --timeout 120 -k gevent --max-requests 10000
