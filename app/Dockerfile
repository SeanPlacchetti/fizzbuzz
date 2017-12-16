FROM python:3.6-alpine
WORKDIR /FizzBuzzApp
RUN mkdir ./static
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
ADD . /code/
EXPOSE 8000
CMD exec gunicorn -w 4 -b :8000 todoer.wsgi