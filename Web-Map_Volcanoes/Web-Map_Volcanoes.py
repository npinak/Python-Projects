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
fgv = folium.FeatureGroup(name = "Volcanoes") 

# Adding markers
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=folium.Popup(iframe), fill_color= color_producer(el) ,color ='grey', fill_opacity=0.7 ))


# Adding population data

fgp = folium.FeatureGroup(name = "Population") 
fgp.add_child(folium.GeoJson(data =open('/Users/pinaknayak/Documents/Github/Python-Projects/Web-Map_Volcanoes/Webmap_datasources/world 3.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 90000000 else 'red'}))

# Adding a control panel for the layers


map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())

map.save("Map1.html")