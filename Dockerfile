FROM python:3.8-slim-buster
RUN apt-get update -y && apt-get upgrade -y

WORKDIR /app
COPY requirements.txt .

RUN  apt-get -yq update

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY pipeline/data/model.joblib /app/pipeline/data/
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]