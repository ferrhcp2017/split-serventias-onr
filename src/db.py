import firebase_admin
from firebase_admin import credentials, firestore

from collections import defaultdict

def json(matricula):
    print (matricula)
    return {'matricula': matricula}, 200
    

def populateBase(document, matricula):
    try:     
        cred = credentials.Certificate("/Users/fernando/Documents/rest_split_onr/app/src/serviceAccountKey.json")
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        db.collection('indicador').add({'documento':document, 'matricula': matricula})
        return "Dado incluído com sucesso", 201
    except:
        return "Não foi possível conectar-se a base", 500    


#consulta = db.collection('indicador').document("1Ni9GRxfNrkzc2RJ74wk").get()
#print (consulta.to_dict())

def pesquisaBens(document):
    cred = credentials.Certificate("/Users/fernando/Documents/rest_split_onr/app/src/serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    docs = db.collection('indicador').where("documento", "==", document).get()
    matriculas = defaultdict(list)
    for doc in docs:
        doc = doc.to_dict()
        matriculas["matriculas"].append(int(doc["matricula"]))
    return matriculas, 200
