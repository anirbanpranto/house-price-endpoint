FROM python:3.8-slim-buster
RUN apt-get update -y && apt-get upgrade -y

WORKDIR /app
COPY requirements.txt .

# install ssh to access github
RUN  apt-get -yq update && \
    apt-get -yqq install ssh git

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY data/model.joblib /app/data/
COPY data/data.csv /app/data/
COPY data/config.json /app/data/
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]