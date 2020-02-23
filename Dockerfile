FROM ubuntu:18.04

RUN mkdir /app

COPY /backend /app

RUN apt-get update 

RUN apt-get install python3-pip

RUN pip3 install -r /app/requirements.txt

EXPOSE 5000

CMD ["python3","/app/app.py"]
