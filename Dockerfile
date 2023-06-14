FROM python:3.11-slim-buster

WORKDIR /application

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
# Add waitress as runtime dependency
RUN pip install waitress==2.1.2

COPY . .

ENV PYTHONUNBUFFERED 1
# The waitress settings.
ENV PORT "8080"
ENV HOST "0.0.0.0"
ENV THREADS "10"

ENTRYPOINT [ "python", "entrypoint.py"]
