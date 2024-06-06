import geopandas as gpd
import folium

kmlFile = "input\\RegularShap.kml"
geoFile = "input\\geoFile.json"

#conversion from KML file to GeoJson
gdf = gpd.read_file(kmlFile)
gdf.to_file(geoFile, driver='GeoJSON')

geoData = gpd.read_file(geoFile)

map = folium.Map()

folium.GeoJson(geoData).add_to(map)

map.show_in_browser()