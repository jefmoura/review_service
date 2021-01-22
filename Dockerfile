FROM python:3.8-alpine3.12

# Do not buffer log messages in memory; some messages can be lost otherwise
ENV PYTHONUNBUFFERED 1

RUN apk update

WORKDIR /code

RUN apk add --no-cache postgresql-libs bash && \
    apk add --no-cache --virtual .build-deps ca-certificates gcc postgresql-dev \
    linux-headers libc-dev make libffi-dev git

# Add the GitHub Token, so private dependencies(repos) can be retrieved
ARG GITHUB_TOKEN
RUN git config --global url."https://${GITHUB_TOKEN}@github.com/".insteadOf "https://github.com/"

COPY ./requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

ADD . /code

RUN apk del .build-deps gcc libc-dev make

ENV PYTHONPATH=/code

EXPOSE 8080
ENTRYPOINT ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "/code/gunicorn_conf.py", "app.main:app"]