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
  password="rootpass",
  database="devops"
)
print(mydb)

#mycursor = mydb.cursor()
#
#sql = "INSERT INTO unity (id_unite) VALUES (%s)"
#val = (12)
#mycursor.execute(sql, val)
#
#mydb.commit()


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM unity")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)