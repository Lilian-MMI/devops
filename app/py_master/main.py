import json
import mariadb
import sys
import flask
import mysql.connector

from aiohttp import web
import socket
import eventlet

from decimal import *
from datetime import datetime

mydb = mysql.connector.connect(
  host="172.20.0.2",
  user="root",
  password="root",
  database="devops"
)
#print(mydb)

host = socket.gethostname()
port = 1234  # initiate port no above 1024

server_socket = socket.socket()  # get instance
# look closely. The bind() function takes tuple as argument
server_socket.bind((host, port))  # bind host address and port together

# configure how many client the server can listen simultaneously
server_socket.listen(5)
conn, address = server_socket.accept()  # accept new connection
#print("Connection from: " + str(address))

# receive data stream. it won't accept data packet greater than 1024 bytes
data = conn.recv(1024).decode("utf-8")

#print("from connected user: " + str(data))

data_decode = json.loads(data)

mycursor = mydb.cursor()

sql = "INSERT INTO unity (id_unite, date_insertion, date_releve, temp_cuve, temp_ex, poids_cuve, poids_pro, m_ph, m_k, c_nacl, bact_sal, bact_e_coli, bact_list) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val = (data_decode['id_unite'],
       datetime.now(),
       data_decode['date_epoch'],
       data_decode['temp_cuve'],
       data_decode['temp_ex'],
       data_decode['poids_cuve'],
       data_decode['poids_pro'],
       data_decode['m_ph'],
       data_decode['m_k'],
       data_decode['c_nacl'],
       data_decode['bact_sal'],
       data_decode['bact_e_coli'],
       data_decode['bact_list'])
mycursor.execute(sql, val)

mydb.commit()

conn.send(data.encode())  # send data to the client

conn.close()  # close the connection

