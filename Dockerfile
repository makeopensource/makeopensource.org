FROM python:3.8

ENV HOME /root
WORKDIR /root

COPY . .

RUN pip3 install -r requirements.txt
RUN python3 manage.py migrate

EXPOSE 8000

CMD python3 manage.py runserver 0.0.0.0:8000