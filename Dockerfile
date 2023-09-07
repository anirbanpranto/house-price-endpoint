FROM python:3.8-slim-buster
RUN apt-get update -y && apt-get upgrade -y

WORKDIR /app
COPY requirements.txt .

RUN  apt-get -yq update

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY inference/artifacts/model.joblib /app/inference/artifacts/
COPY . .

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]