FROM python:3-slim
ARG MLFLOW_VERSION=1.19.0

WORKDIR /usr/src/mlfs-app/

RUN pip install --no-cache-dir mlflow==$MLFLOW_VERSION psycopg2-binary

EXPOSE 5000

CMD mlflow server \
    --backend-store-uri postgresql://root:root@postgres:5432/mlflowdb \
    --default-artifact-root /usr/src/mlfs-app/mlflow-data/artifacts \
    --host 0.0.0.0