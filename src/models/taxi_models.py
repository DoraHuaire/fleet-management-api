from flask_sqlalchemy import SQLAlchemy
from database.db import db

#Tabla Taxi
class Taxis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String, nullable=False)
    
    def convert_to_dictionary(self):
        return {
            'id': self.id,
            'plate': str(self.plate)
        }
        
def get_filtered_taxis(id, plate, page, per_page, limit):
    query = Taxis.query
# Filtramos por ID, si se especifica
    if id:
       query = query.filter(Taxis.id == id)
    
# Filtramos por plate, si se especifica
    if plate:
       query = query.filter(Taxis.plate.ilike(f"%{plate}%"))

# aplicamos la paginación y definimos límites
    taxis = query.offset((page - 1) * per_page).limit(limit).all()

# convertimos taxis a disccionarios
    return [taxi.convert_to_dictionary() for taxi in taxis]