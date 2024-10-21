from flask import Flask
from database.config import Config
from routes.taxis_routes import init_routes_taxis
from routes.trajectories_routes import init_routes_trajectories
from routes.latest_routes import init_routes_trajectories_latest
from routes.users_routes import init_routes_users
from database.db import db

# Inicializar Flask
app = Flask(__name__)
app.config.from_object(Config)
# Inicializar la base de datos con la app
db.init_app(app)

init_routes_taxis(app)
init_routes_trajectories(app)
init_routes_trajectories_latest(app)
init_routes_users(app)

if __name__ == '__main__':
    app.run(debug=True)