from flask import Flask, render_template, request, jsonify
from api_requests import get_week_ago_earthquakes, get_selected_point_earthquakes
from utils import get_coordinates


app = Flask(__name__)


@app.route('/')
def show_map():
    lat, lng, zoom = 31.8974, 54.3569, 5
    earthquakes = get_week_ago_earthquakes(limit=1000)
    coordinates = get_coordinates(earthquakes)

    return render_template("map.html", lat=lat, lng=lng, zoom=zoom, coordinates=coordinates)


@app.route('/get-earthquake', methods=["POST"])
def get_earthquake():
    coordinate = request.json
    earthquakes = get_selected_point_earthquakes(coordinate["lat"], coordinate["lng"])
    coordinates = get_coordinates(earthquakes)
    return jsonify({"Ok": 1, "points": coordinates})


if __name__ == '__main__':
    app.run()
