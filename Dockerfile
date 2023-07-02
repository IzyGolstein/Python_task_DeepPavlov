FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN apt-get update && apt-get install -y tar
RUN echo "Installing dependencies"
RUN pip install -r requirements.txt

COPY data.tgz data.tgz

RUN tar zxfv data.tgz

CMD python csv_sum.py