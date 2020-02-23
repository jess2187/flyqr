FROM python:3

RUN mkdir /app

COPY /backend /app

RUN ls /app

WORKDIR /app

EXPOSE 5000 6379

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["app.py"]
