import json

def construct_GeoJSON_Polygon(listPoint):

    if listPoint[0] != listPoint[-1]:
        listPoint.append(listPoint[0])

    geojson = {
        "type": "Feature",
        "geometry": {
            "type": "Polygon",
            "coordinates": [listPoint]
        },
        "properties": {
        }
    }
    return json.dumps(geojson, indent=4)
