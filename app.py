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

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=80)