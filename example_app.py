from flask import Flask
from flask_connexion import Connexion


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

def hello(name):
    return {'message': 'hello ' + name}

connexion = Connexion(app)
connexion.add_api('example.yaml')


if __name__ == '__main__':
    app.run(debug=True)
