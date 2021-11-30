FROM python:3.8-buster
COPY requirements.txt /usr/src/app/requirements.txt
WORKDIR /usr/src/app
ENV WORKDIRPATH=/usr/src/app/
RUN pip install -r requirements.txt
COPY . /usr/src/app
RUN pip install -e .
CMD aim up --host 0.0.0.0 & python api/api.py