FROM python:3.7.10-alpine3.12

RUN apk update && apk add python3-dev \
    gcc \
    libc-dev \
    libffi-dev

WORKDIR /usr/src/app
RUN python3 -m pip install \
    schedule==1.1.0 \
    python-dotenv==0.17.0 \
    twython==3.9.1 \
    pymongo==3.4.0

COPY data_collection.py main.py sentences.py .env ./
CMD ["python3", "main.py"]
