import json
import mariadb
import sys
import flask
import mysql.connector

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def index():
    return 'Success!'


#with open("D:\Devops\data.json", "r") as read_file:
#    data = json.load(read_file)
#
#    for key, value in data.items():
#        print(key, ":", value)


mydb = mysql.connector.connect(
  host="172.20.0.2",
  user="root",
  password="root",
  database="devops"
)
print(mydb)

mycursor = mydb.cursor()

sql = "INSERT INTO unity (id_unite, date_insertion , temp_cuve, temp_ex, poids_cuve, poids_pro, m_ph, m_k, c_nacl, bact_sal, bact_e_coli, bact_list) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val = (1, 0, 2.8, 13.6, 3545, 0, 7.0, 42, 1.6, 29, 38, 44)
mycursor.execute(sql, val)

mydb.commit()
