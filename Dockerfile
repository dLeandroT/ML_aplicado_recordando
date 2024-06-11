FROM python:3.12-rc-slim-buster

WORKDIR /app

COPY api/requirements.txt .

RUN pip install -U pip install -r requirements.txt

COPY api ./api

COPY models/model.pkl ./models/model.pkl

COPY initializer.sh .

RUN chmod +x initializer.sh

EXPOSE 8000

ENTRYPOINT ["./initializer.sh"]