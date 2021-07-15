import folium
import pandas as pd 

data = pd.read_csv("/Users/pinaknayak/Documents/Github/Python-Projects/Web-Map_Volcanoes/Webmap_datasources/Volcanoes.txt")

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif elevation >= 1000 and elevation <= 3000:
        return "orange"
    else:
        return "red"


map = folium.Map(location = [38.58,-99.09], zoom_start=6, tiles = "Stamen Terrain")

lon = list(data['LON'])
lat = list(data['LAT'])
elev = list(data['ELEV'])
name = list(data["NAME"])

# Code to google search a volcano when you click on it's pop up
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

# Can add multiple features to a feature group 
fg = folium.FeatureGroup(name = "My Map") 

# Adding markers
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = color_producer(el))))
 
map.add_child(fg)


map.save("Map1.html")