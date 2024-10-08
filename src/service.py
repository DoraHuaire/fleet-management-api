from models import Taxis, Trajectories

def get_filtered_taxis(plate, page, limit):
    query = Taxis.query
    if plate:
        query = query.filter(Taxis.plate.ilike(f"%{plate}%"))
    
    taxis = query.paginate(page=page, per_page=limit).items
    return [taxi.convert_to_dictionary() for taxi in taxis]

def get_filtered_trajectories(taxiId, date):
    query = Trajectories.query
    if date:
        query = query.filter(Trajectories.date.ilike(f"%{date}%"))
        
    trajectories = Trajectories.query.all()
    return [trajectory.convert_to_dictionary() for trajectory in trajectories]