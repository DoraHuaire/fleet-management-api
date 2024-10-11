from src.database.db import db 

#Tabla trayectorias
class Trajectories(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    taxi_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    
    def convert_to_dictionary(self):
        return {
            'latitude': self.latitude,
            'longitude': self.longitude,
            'timestamp': self.date
        }