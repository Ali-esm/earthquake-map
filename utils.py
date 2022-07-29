def get_coordinates(data:dict):
    locations = []
    for i in range(len(data["features"])):
        locations.append(data["features"][i]["geometry"]["coordinates"])

    return locations
