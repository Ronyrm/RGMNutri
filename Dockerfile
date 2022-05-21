FROM python:3.8.5
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install mysqlclient
RUN pip install -r requirements.txt
COPY . .
CMD python wsgi.py