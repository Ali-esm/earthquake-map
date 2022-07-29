import requests
from datetime import datetime, timedelta


def get_week_ago_earthquakes(limit=100):
    """
    to get earthquakes in past 7 days
    """
    start_time = str(datetime.now().date() - timedelta(days=7))
    payload = {
        "format": "geojson",
        "starttime": start_time,
        "limit": str(limit)
    }

    url = f"https://earthquake.usgs.gov/fdsnws/event/1/query"
    res = requests.get(url, params=payload)
    return res.json()


def get_selected_point_earthquakes(lat, lng, km=1000, limit=100):
    """
    to get earthquakes in specific lat & lng in a circle with 1000km radius and
    minimum magnitude of 3 richter
    """
    start_time = str(datetime.now().date() - timedelta(days=30))

    payload = {
        "latitude": lat,
        "longitude": lng,
        "format": "geojson",
        "starttime": start_time,
        "limit": str(limit),
        "minmagnitude": 3,
        "maxradiuskm": km,
    }
    url = f"https://earthquake.usgs.gov/fdsnws/event/1/query"
    res = requests.get(url, params=payload)
    return res.json()
