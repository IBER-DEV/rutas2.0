from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # km
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c  # km

def estimate_eta_minutes(lat1, lon1, lat2, lon2, avg_speed_kmh=30):
    distance_km = haversine(lat1, lon1, lat2, lon2)
    if avg_speed_kmh <= 0:
        avg_speed_kmh = 20
    time_hours = distance_km / avg_speed_kmh
    return int(time_hours * 60)  # minutes
