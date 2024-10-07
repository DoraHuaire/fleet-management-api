from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://default:40BMJILWqGYE@ep-patient-hat-a40xhj3v-pooler.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

#Tabla Taxi
class Taxis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String, nullable=False)
    
    def convert_to_dictionary(self):
        return {
            'id': self.id,
            'plate': self.plate
        }

# Define el endpoint /taxis
@app.route('/taxis', methods=['GET'])
def get_taxis():
    plate = request.args.get('plate')
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    
    query = Taxis.query
    
# filtramos por placa
    if plate:
        query = query.filter(Taxis.plate.ilike(f"%{plate}%")) 
        
#paginación    
    taxis = query.paginate(page=page, per_page=limit).items 
    
    taxis_list = [taxi.convert_to_dictionary() for taxi in taxis]
    return jsonify(taxis_list)

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

# Define el endpoint /trajectories
@app.route('/trajectories', methods=['GET'])
def get_trajectories():
    
    trajectories = Trajectories.query.all()
    trajectories_list = [trajectory.convert_to_dictionary() for trajectory in trajectories]
    
    return jsonify(trajectories_list)

if __name__ == '__main__':
    app.run(debug=True)