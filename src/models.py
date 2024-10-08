from app import db

#Tabla Taxi
class Taxis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String, nullable=False)
    
    def convert_to_dictionary(self):
        return {
            'id': self.id,
            'plate': self.plate
        }

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
            'date': self.date.strftime("%Y-%m-%d %H:%M:%S"),
            'latitude': self.latitude,
            'longitude': self.longitude
        }