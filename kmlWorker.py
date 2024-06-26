import geopandas as gpd
import folium
import json
import random as r

from shapely.geometry import Polygon, Point
from shapely.ops import nearest_points

import geoFileConstructor as gc
import coordSystemMod as cm
import svgReader as rd

kmlFile = "input\\RegularShap.kml"
geoFile = "input\\geoFile.json"

#conversion from KML file to GeoJson
gdf = gpd.read_file(kmlFile, driver='KML')
geoString = gdf.to_json()
geoJSON = json.loads(geoString)

#Get the polygon vertex
coordinates = geoJSON["features"][0]["geometry"]["coordinates"][0]

for point in coordinates:
     point.pop(2)

map_xmax = map_xmin = coordinates[0][0]
map_ymax = map_ymin = coordinates[0][1]

for i in range(1,len(coordinates)):
   if coordinates[i][0] > map_xmax:
       map_xmax = coordinates[i][0]
   elif coordinates[i][0] < map_xmin:
       map_xmin = coordinates[i][0]
   if coordinates[i][1] > map_ymax:
       map_ymax = coordinates[i][1]
   elif coordinates[i][1] < map_ymin:
       map_ymin = coordinates[i][1]

#using for change the system coordonates
map_diff = [map_xmax - map_xmin, map_ymax - map_ymin, map_xmin, map_ymin]

#change system parameters
sx, sy, tx, ty = cm.changeParameters(map_diff,rd.img_diff)

#trasform SVG coordonates for limits point in GPS coordoantes
list = [ ]
for i in rd.limit_point:
     list.append([i[0] * sx + tx, i[1] * sy + ty])


#trasform SVG coordonates for route point in GPS coordoantes
gps_dict = dict()

for i in rd.adj_list.keys():
    i_key = (i[0] * sx + tx,i[1] * sy + ty)
    gps_dict[i_key] = []
    for j in rd.adj_list[i]:
        gps_dict[i_key].append([j[0] * sx + tx, j[1] * sy + ty])


polya = Polygon(coordinates)
polyb = Polygon(list)

# Calculate the centroid of the polygon
centroid = polya.centroid
centroid_x, centroid_y = centroid.x, centroid.y

scale_factor = 1.0
tolerance = 1e-6
max_iterations = 1000
iteration = 0

rescale_coord = dict()
points = [Point(coord) for coord in gps_dict.keys()]

while True:
    all_inside = True
    for point in points:
        scaled_x, scaled_y = cm.scale_point(point.x, point.y, centroid_x, centroid_y, scale_factor)
        if not polya.contains(Point(scaled_x, scaled_y)):
            all_inside = False
            break

    if all_inside or iteration >= max_iterations:
        break

    scale_factor *= 0.99
    iteration += 1

# Apply final scaling to points
transformed_points = [Point(cm.scale_point(point.x, point.y, centroid_x, centroid_y, scale_factor)) for point in points]

transformed_dict = dict()
dict_k = [x for x in gps_dict.keys()]

for i in range(len(dict_k)):
    transformed_dict[dict_k[i]] = [transformed_points[i].x, transformed_points[i].y]

new_gps_dict = dict()

for i in gps_dict.keys():
    new_gps_dict[tuple(transformed_dict[i])] = []
    for j in gps_dict[i]:
        new_gps_dict[tuple(transformed_dict[i])].append(transformed_dict[tuple(j)])

# write a GeoJSON with SVG point
new_shape = gc.construct_GeoJSON_Polygon(list)

# create the map
map = folium.Map(location=[map_ymin,map_xmin], zoom_start=15)

#add point on the map
folium.GeoJson(geoJSON).add_to(map)
#folium.GeoJson(new_shape).add_to(map)

visited = []
for i in new_gps_dict.keys():
    folium.Marker(location=(i[1],i[0])).add_to(map)
    for j in new_gps_dict[i]:
        if j not in visited:
            folium.PolyLine(locations=[[i[1],i[0]],[j[1],j[0]]],color='red').add_to(map)
    visited.append(i)

#show map in the browser
map.show_in_browser()