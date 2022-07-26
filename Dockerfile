FROM python:3.8-slim-buster

RUN apt-get update

WORKDIR /myapp

COPY . .

RUN apt-get update && apt-get install -y git && apt-get install -y libsndfile1 

RUN pip install fastapi uvicorn soundfile

RUN cd /myapp/app/vietTTS && pip install -e .

CMD ["uvicorn","wsgi:app","--host", "0.0.0.0", "--port", "8090"]