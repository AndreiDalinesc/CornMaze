import geopandas as gpd
import folium
import json
import random as r

from shapely.geometry import Polygon

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
     list1 = []
     list1.append(i[0] * sx + tx)
     list1.append(i[1] * sy + ty)
     list.append(list1)

#trasform SVG coordonates for route point in GPS coordoantes
gps_dict = dict()

for i in rd.adj_list.keys():
    i_key = (i[0] * sx + tx,i[1] * sy + ty)
    gps_dict[i_key] = []
    for j in rd.adj_list[i]:
        gps_dict[i_key].append([j[0] * sx + tx, j[1] * sy + ty])

polya = Polygon(coordinates)
polyb = Polygon(list)

# write a GeoJSON with SVG point
new_shape = gc.construct_GeoJSON_Polygon(list)

pointFeatures = []
for i in gps_dict.keys():
    pointFeatures.append(gc.construct_GeoJSON_Point(i))

# create the map
map = folium.Map()

#add point on the map
folium.GeoJson(geoJSON).add_to(map)
folium.GeoJson(new_shape).add_to(map)

visited = []
for i in gps_dict.keys():
    folium.Marker(location=i).add_to(map)
    for j in gps_dict[i]:
        if j not in visited:
            folium.PolyLine(locations=[i,j],color='red').add_to(map)
    visited.append(i)

#show map in the browser
map.show_in_browser()