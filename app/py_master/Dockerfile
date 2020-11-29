FROM python:latest

RUN pip3 install mariadb
RUN pip3 install flask
RUN pip install mysql-connector-python
RUN pip install python-socketio
RUN pip install eventlet
RUN pip install aiohttp

COPY . .

CMD [ "python", "./main.py", "--host", "0.0.0.0"]
