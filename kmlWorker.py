import geopandas as gpd
import folium
import json

import geoFileConstructor as gc
import svgReader as rd

kmlFile = "input\\RegularShap.kml"
geoFile = "input\\geoFile.json"

#conversion from KML file to GeoJson
gdf = gpd.read_file(kmlFile, driver='KML')
geoString = gdf.to_json()
geoJSON = json.loads(geoString)

#Get the polygon vertex
coordinates = geoJSON["features"][0]["geometry"]["coordinates"][0]

#Show polygon coordonates
for point in coordinates:
     print(point)


# write a GeoJSON with SVG point
new_shape = gc.construct_GeoJSON_Polygon(rd.limit_point)

# create the map
map = folium.Map()

#add point on the map
folium.GeoJson(geoJSON).add_to(map)
# folium.GeoJson(new_shape).add_to(map)

#show map in the browser
map.show_in_browser()