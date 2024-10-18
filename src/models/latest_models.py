from sqlalchemy import func
from models.trajectories_models import Trajectories
from models.taxi_models import Taxis
from database.db import db

# Obtenemos la última trayectoria registrada
def get_latest_trajectories():
    # Subconsulta para obtener la última fecha (date) por taxi_id
    subquery = db.session.query(
        Trajectories.taxi_id,
        func.max(Trajectories.date).label('latest_date')
    ).group_by(Trajectories.taxi_id).subquery()

    # Consulta principal, une la subconsulta con la tabla original para obtener los otros campos
    latest_trajectories = db.session.query(
        Taxis.id,
        Taxis.plate,
        Trajectories.taxi_id,
        Trajectories.date,
        Trajectories.latitude,
        Trajectories.longitude
    ).join(
        Trajectories, 
        (Taxis.id == Trajectories.taxi_id) 
    ).join(
        subquery,
        (Trajectories.taxi_id == subquery.c.taxi_id) & (Trajectories.date == subquery.c.latest_date)
    ).all()

    # Convertir los resultados a una lista de diccionarios con los nombres que el test espera
    latest_trajectories_dict = [
        {
            'id': row.id,  # Taxis
            'plate': row.plate,  # taxi
            'taxiId': row.taxi_id,  # Cambiar el nombre a taxiId 
            'timestamp': row.date.strftime("%Y-%m-%d %H:%M:%S"),  # Cambiar el nombre a timestamp 
            'latitude': row.latitude,
            'longitude': row.longitude
        }
        for row in latest_trajectories
    ]

    return latest_trajectories_dict