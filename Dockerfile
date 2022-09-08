FROM python:3.8-slim

ARG LIST_URLS
ENV LIST_URLS ${LIST_URLS}

WORKDIR /app

ADD requirements.txt /app
RUN pip install -r requirements.txt
ADD . /app

EXPOSE 8990

CMD ["python", "main.py"]
