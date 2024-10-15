from flask import Flask
from database.config import Config
from routes.taxis_routes import init_routes_taxis
from routes.trajectories_routes import init_routes_trajectories
from database.db import db

# Inicializar Flask
app = Flask(__name__)
app.config.from_object(Config)
# Inicializar la base de datos con la app
db.init_app(app)

init_routes_taxis(app)
init_routes_trajectories(app)

if __name__ == '__main__':
    app.run(debug=True)