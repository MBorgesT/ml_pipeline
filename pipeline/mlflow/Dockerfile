FROM python:3-slim
ARG MLFLOW_VERSION=1.21.0

WORKDIR /srv/
RUN pip install --no-cache-dir mlflow==$MLFLOW_VERSION

EXPOSE 5000

CMD mlflow server \
    --backend-store-uri /srv/mlflow_srv \
    --default-artifact-root /srv/mlflow_srv \
    --host 0.0.0.0