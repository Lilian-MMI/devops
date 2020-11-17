import automate
import json
import socket

def object_to_json(auto):
    auto_json = {
        "id_unite": auto.id_unite,
        "date_epoch": 0,
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


def connect():
    HOST, PORT = "localhost", 9999

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    return sock


if __name__ == '__main__':
    while True:
        json_1 = object_to_json(automate.Automate())
        json_2 = object_to_json(automate.Automate())
        json_3 = object_to_json(automate.Automate())
        json_4 = object_to_json(automate.Automate())
        json_5 = object_to_json(automate.Automate())
        json_6 = object_to_json(automate.Automate())
        json_7 = object_to_json(automate.Automate())
        json_8 = object_to_json(automate.Automate())
        json_9 = object_to_json(automate.Automate())
        json_10 = object_to_json(automate.Automate())
        with open("developer.json", "w") as write_file:
            json.dump((json_1, json_2, json_3, json_4, json_5, json_6, json_7, json_8, json_9, json_10), write_file)

        s = connect()
        file = open("developer.json", "rb")
        SendData = file.read(1024)

        while SendData:
            s.send(SendData)
            SendData = file.read(1024)
        s.close()