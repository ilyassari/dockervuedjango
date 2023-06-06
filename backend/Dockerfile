# pull official base image
FROM python:3.8-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add icu-data-full\
    && apk add --no-cache postgresql-dev gcc libc-dev g++ libffi-dev libxml2 python3-dev musl-dev unixodbc unixodbc-dev mariadb-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
 
# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]