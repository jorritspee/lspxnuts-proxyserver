# syntax=docker/dockerfile:1

FROM python:3.11-slim-buster

WORKDIR /lspxnuts-proxy-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .


CMD [ "python3", "-u", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8000" ]

# OLD:
# FROM python:3

# ENV SRC_DIR /usr/bin/src/webapp/src

# COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt

# COPY src/* ${SRC_DIR}/

# WORKDIR ${SRC_DIR}

# ENV PYTHONUNBUFFERED=1

# CMD ["python", "index.py"]
