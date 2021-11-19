FROM python:3.8-buster
COPY . /usr/src/app
WORKDIR /usr/src/app
ENV WORKDIRPATH=/usr/src/app/
RUN pip install -r requirements.txt
CMD ["python", "api.py"]