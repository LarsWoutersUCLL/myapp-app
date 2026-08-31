from flask import Flask
app = Flask(__name__)

@app.route('/') 
def hello():
    return 'Hello Cloud Native Collective'

@app.route('/health')
def health():
    return 'OK', 200

@app.route('/info')
def info():
    return {'app': 'larsucll', 'status': 'running'}

@app.route('/about')
def about():
    return 'Deze app is gebouwd door Lars Wouters voor het vak Cloud - Systeem- en Netwerkbeheer, UCLL'