FROM python:3.9
WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /wait
RUN chmod +x /wait

CMD /wait && uvicorn server:app --host '0.0.0.0' --port 8000

