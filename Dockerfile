FROM python:3.8

ENV SRC_DIR /usr/bin/src/webapp/src

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY src/* ${SRC_DIR}/

WORKDIR ${SRC_DIR}

ENV PYTHONUNBUFFERED=1

CMD ["python", "simple_server.py"]