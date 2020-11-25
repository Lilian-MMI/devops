FROM python:3.8

RUN pip3 install mariadb
RUN pip3 install flask
RUN pip install mysql-connector-python

COPY . .

CMD [ "python", "./main.py", "--host", "0.0.0.0"]