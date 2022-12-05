import datetime
import pprint

import pymongo as pyM
from pymongo.server_api import ServerApi

client = pyM.MongoClient("mongodb+srv://pymongo:teste@cluster0.ztwghg4.mongodb.net/?retryWrites=true&w=majority",
                         server_api=ServerApi('1'))
db = client.test
collection = db.test_collection
print(db.list_collection_names)

# inserido informacoes
bank = {
    "cliente": "Fernanda",
    "cpf": "32544555490",
    "endereco": "rua joe cardoso , 195",
    "conta": ["0001", "225",351]
}

new_bank=[{  "cliente": "Maria",
    "cpf": "457872115444",
    "endereco": "rua andradina , 195",
    "conta": ["0003", "226",351]},

{  "cliente": "jOAO",
    "cpf": "254545454545",
    "endereco": "rua almirante , 225",
    "conta": ["002", "25454",1000]},


          ]





banks=db.banks
banks_id=banks.insert_one(bank).inserted_id
print(banks_id)


result = banks.insert_many(new_bank)
print(banks_id)

print(banks.find())

for bank in banks.find():
    pprint.pprint(bank)

banks.delete_one({"cliente":"Fernanda"})
print(banks.count_documents({}))

collections = db.list_collection_names()
for x in collections:
    print(x)
