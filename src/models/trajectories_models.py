from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import cast, Time
from datetime import datetime
from flask import jsonify
from database.db import db

#Tabla trayectorias
class Trajectories(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    taxi_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    
    def convert_to_dictionary(self):
        return {
            'id': self.id,
            'taxi_id': self.taxi_id,
            'date': self.date.strftime("%d-%m-%Y %H:%M:%S"),
            'latitude': self.latitude,
            'longitude': self.longitude
        }

def get_filtered_trajectories(taxiId, date):
    query = Trajectories.query
     # Filtrar por taxiId si se proporciona
    if taxiId:
        query = query.filter(Trajectories.taxi_id == taxiId)
    if date:
        query = query.filter(Trajectories.date == date)
        
    trajectories = query.all()
    return [trajectory.convert_to_dictionary() for trajectory in trajectories]