from flask import Flask
from src.db import pesquisaBens, populateBase


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/indicador/<document>', methods=['GET'])
def indicator(document):
    return pesquisaBens(document)
    
@app.route('/updatebase/<document>&<matricula>', methods=['GET'])
def updatebase(document, matricula):
    return populateBase(document, matricula)
    
app.run(debug=True)
    