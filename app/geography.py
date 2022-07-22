from math import radians, sin, asin, cos, sqrt

EARTH_RADIUS = 6371 # https://en.wikipedia.org/wiki/Earth_radius

def calculate_distance(_lat1, _lon1, _lat2, _lon2):
    # https://en.wikipedia.org/wiki/Haversine_formula#Formulation
    
    lat1, lon1, lat2, lon2 = (radians(angle) for angle in (_lat1, _lon1, _lat2, _lon2))
    
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1
    
    theta = asin(sqrt(sin(delta_lat/2)**2 + cos(lat1)*cos(lat2) * sin(delta_lon/2)**2))

    return 2 * EARTH_RADIUS * theta
