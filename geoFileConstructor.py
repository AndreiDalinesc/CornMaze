import json

#make a GeoJSON structure for polygons
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

def construct_GeoJSON_Point(Point):
    geojson = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [Point]
        },
        "properties": {
        }
    }
    return json.dumps(geojson, indent=4)

def construct_GeoJSON_LineString(p1,p2):
    geojson = {
        "type": "Feature",
        "geometry": {
            "type": "LineString",
            "coordinates": [p1, p2]
        },
        "properties": {
        }
    }
    return json.dumps(geojson, indent=4)