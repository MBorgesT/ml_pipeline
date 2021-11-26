FROM python:3.8-buster
COPY requirements.txt /usr/src/coord-app/requirements.txt 
WORKDIR /usr/src/coord-app
ENV WORKDIRPATH=/usr/src/coord-app/
RUN pip install -r requirements.txt
COPY . /usr/src/coord-app
CMD ["python", "api.py"]