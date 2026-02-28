FROM python:3.9-alpine

RUN apk add --no-cache curl

RUN adduser -D http-server

WORKDIR /home/http-server

COPY app.py .
RUN chown http-server:http-server app.py

USER http-server

EXPOSE 8080

CMD ["python", "app.py"]