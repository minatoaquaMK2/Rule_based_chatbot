FROM alpine:latest

RUN apk add --no-cache python3-dev
RUN pip3 install --upgrade pip

COPY ./app /service
WORKDIR /service

RUN pip3 install -r requirements.txt
EXPOSE 7778

WORKDIR /service/timesolt
ENTRYPOINT ["python3"]
CMD ["__init__.py"]