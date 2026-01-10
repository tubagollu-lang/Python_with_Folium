import folium
sehrekustu = [40.1886, 29.0620]
ulucami = [40.1839, 29.0619]
m = folium.Map(location =sehrekustu, zoom_start=16, tiles="CartoDB dark_matter")
folium.Marker(sehrekustu,popup="Meydan", icon = folium.Icon(color="cyan" , icon="user")).add_to(m)
folium.Marker(ulucami, popup="Ulu Cami", icon=folium.Icon(color="lightgray", icon="info_sign")).add_to(m)

folium.PolyLine(locations=[sehrekustu,ulucami],color="yellow" ,weight=5,opacity=0.7).add_to(m)
m.save("bursa_dark_mode.html")
