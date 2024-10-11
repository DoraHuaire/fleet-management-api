from src.models.trajectories_models import Trajectories

def get_filtered_trajectories(taxiId, date):
    query = Trajectories.query
     # Filtrar por taxiId si se proporciona
    if taxiId:
        query = query.filter(Trajectories.taxi_id == taxiId)
        
    # Filtrar por fecha si se proporciona    
    if date:
        query = query.filter(Trajectories.date == date)
        
    trajectories = query.all()
    return [trajectory.convert_to_dictionary() for trajectory in trajectories]