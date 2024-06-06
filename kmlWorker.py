import simplekml
from pykml import parser
import geojson
import subprocess
import geopandas as gpd
from shapely.geometry import Point, Polygon
import pandas as pd
import folium
import kml2geojson


kmlFile = "input\\RegularShap.kml"
geoFile = "input\\geoFile.json"

#conversion from KML file to GeoJson
gdf = gpd.read_file(kmlFile)
gdf.to_file(geoFile, driver='GeoJSON')

geoData = gpd.read_file(geoFile)

map = folium.Map()

folium.GeoJson(geoData).add_to(map)

map.show_in_browser()