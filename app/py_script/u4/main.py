import automate
import json
import socket
from datetime import datetime
import time

def object_to_json(auto):
    auto_json = {
        "id_unite": auto.id_unite,
        "date_epoch": str(datetime.now()),
        "temp_cuve": auto.temp_cuve,
        "temp_ex": auto.temp_ex,
        "poids_cuve": auto.poids_cuve,
        "poids_pro": auto.poids_pro,
        "m_ph": auto.m_ph,
        "m_k": auto.m_k,
        "c_nacl": auto.c_nacl,
        "bact_sal": auto.bact_sal,
        "bact_e_coli": auto.bact_e_coli,
        "bact_list": auto.bact_list
    }
    return auto_json



json_1 = object_to_json(automate.Automate())
with open("developer.json", "w") as write_file:
    json.dump((json_1), write_file)


file = open("developer.json", "rb")
SendData = file.read(1024)

host = "172.20.0.3"  # as both code is running on same pc
port = 1234  # socket server port number

client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))  # connect to the server

#message = "Hello server"  # take input

client_socket.send(SendData)  # send message

client_socket.close()  # close the connection

time.sleep(60)