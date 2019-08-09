import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])

map = folium.Map(location=[40, -104], zoom_start=6)

fg = folium.FeatureGroup(name="My Map")

for lat, lon in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lat, lon], popup="Hi", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")

