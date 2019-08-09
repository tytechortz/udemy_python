import folium
map = folium.Map(location=[40, -104], zoom_start=6)

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")

