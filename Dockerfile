FROM python:3
RUN mkdir /dungeonrun
WORKDIR /dungeonrun
COPY requirements.txt /dungeonrun
RUN pip install -r requirements.txt
COPY . /dungeonrun

EXPOSE 8080/tcp
