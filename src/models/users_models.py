from database.db import db

#Tabla trayectorias
class Users(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    taxi_id = db.Column(db.Integer, db.ForeignKey('taxis.id'))
    date = db.Column(db.DateTime)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def convert_to_dict(self):
        return {
            "id": self.id,
            "taxiId": self.taxi_id,
            "date": self.date,
            "latitude": self.latitude,
            "longitude": self.longitude
        }

def get_filtered_trajectories(taxi_id, date_str):
    query = db.session.query(Trajectories)
    
    try:
        date = datetime.strptime(date_str, '%d-%m-%Y')  
    except ValueError:
        return None, "Formato de fecha inválido. Usa el formato DD-MM-YYYY" 
    
    # Filtrar por taxi_id y fecha
    # Comparar solo la fecha sin la hora
    trajectories = query.filter(
        Trajectories.taxi_id == taxi_id,
        func.date(Trajectories.date) == date.date()  
    ).all()

    return [trajectory.convert_to_dict() for trajectory in trajectories], None

 