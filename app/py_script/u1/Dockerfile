FROM python:3.8

RUN pip install python-socketio
RUN pip install eventlet
RUN pip install aiohttp
RUN pip install numpy

COPY . .

CMD ["python", "./main.py", "--host", "0.0.0.0"]