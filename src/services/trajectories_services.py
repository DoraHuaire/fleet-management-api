from src.models.trajectories_models import Trajectories
from sqlalchemy import cast, Time
from datetime import datetime
from flask import jsonify

def get_filtered_trajectories(taxiId, date):
    query = Trajectories.query
     # Filtrar por taxiId si se proporciona
    if taxiId:
        query = query.filter(Trajectories.taxi_id == taxiId)
        
    # Filtrar por fecha si se proporciona    
    # Si la fecha es proporcionada, comparar solo por la hora
    if date:
        # Si es un string, convertirlo; si ya es un objeto datetime, tomar la hora directamente
        if isinstance(date, str):
            try:
                # Convertir la fecha en hora (en caso de ser un string)
                date = datetime.strptime(date, '%Y-%m-%d').time()
            except ValueError:
                return jsonify({"error": "La fecha debe estar en formato YYYY-MM-DD"}), 400
        elif isinstance(date, datetime):
            # Si ya es un datetime, tomar la parte de la hora
            date = date.time()
        
        # Hacer la comparación solo por la parte de la hora
        query = query.filter(cast(Trajectories.date, Time) == date)
        
    trajectories = query.all()
    return [trajectory.convert_to_dictionary() for trajectory in trajectories]