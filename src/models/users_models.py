from database.db import db
from flask import jsonify

#Tabla trayectorias
class Users(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False) 
    rol = db.Column(db.String, nullable=False)

    def convert_to_dictionary(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "rol" : self.rol
        }

def get_filtered_users(page, per_page, limit):
    query = db.session.query(Users)
    users = query.offset((page - 1) * per_page).limit(limit).all()
# convertimos users a diccionarios
    return [user.convert_to_dictionary() for user in users]

def connection_db_create_user(user_data):
    # Obtenemos datos del usuario
    name = user_data.get('name')
    email = user_data.get('email')
    password = user_data.get('password')
    rol = user_data.get('rol')
    
    #Verificamos que los campos necesarios están presentes
    if not all([name, email, password, rol]):
        return jsonify({'error': 'Faltan campos necesarios'}), 400

    # Creamos el nuevo usuario
    new_user = Users(name=name, email=email, password=password, rol=rol)
    db.session.add(new_user)
    db.session.commit()

    # Respondemos con id, name, email y el código 201
    return jsonify({
        'id': new_user.id,
        'name': new_user.name,
        'email': new_user.email
    }), 201