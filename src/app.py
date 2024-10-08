from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Inicializar Flask y SQLAlchemy
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Importar las rutas
from routes import *

if __name__ == '__main__':
    app.run(debug=True)