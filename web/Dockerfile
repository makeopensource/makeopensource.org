FROM python:3.14-trixie

WORKDIR /app/web

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

ENV PYTHONPATH=/app
WORKDIR /app/web/makeopensource

ENTRYPOINT ["/app/web/entrypoint.sh"]
