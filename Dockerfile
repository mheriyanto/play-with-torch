FROM python:3.6-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN apt update
RUN apt install ffmpeg libsm6 libxext6  -y

COPY . .

CMD [ "python3", "inference.py"]
