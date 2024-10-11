from src.database.db import db 

#Tabla Taxi
class Taxis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String, nullable=False)
    
    def convert_to_dictionary(self):
        return {
            'id': self.id,
            'plate': self.plate
        }