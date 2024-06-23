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
print(sx, sy, tx, ty)
#test = r.choice(coordinates)
test = [21.15736485981648, 45.3956439517378]
print("test",test)

list = [ ]
for i in rd.limit_point:
     list1 = []
     list1.append(i[0] * sx + tx)
     list1.append(i[1] * sy + ty)
     list.append(list1)


print("list", list)
print("poly", coordinates)

polya = Polygon(coordinates)
polyb = Polygon(list)

print(polya.contains(polyb))

#Show polygon coordonates
# for point in coordinates:
#      print(point)


# write a GeoJSON with SVG point
#rd.limit_point = cm.resiveSvg(rd.limit_point,0.7)

new_shape = gc.construct_GeoJSON_Polygon(list)

# create the map
map = folium.Map()

#add point on the map
folium.GeoJson(geoJSON).add_to(map)
folium.GeoJson(new_shape).add_to(map)

#show map in the browser
map.show_in_browser()