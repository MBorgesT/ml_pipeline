FROM python:3.8-buster
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install mlflow==1.21.0
CMD ["mlflow", "server", "--file-store", "./mlruns", "--host", "0.0.0.0"]