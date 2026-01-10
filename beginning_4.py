import folium
sehrekustu = [40.1886, 29.0620]
ulucami = [40.1839, 29.0619]
m = folium.Map(location =sehrekustu, zoom_start=16)
folium.Marker(sehrekustu,popup="Meydan", icon = folium.Icon(color="blue")).add_to(m)
folium.Marker(ulucami, popup="Ulu Cami", icon=folium.Icon(color="green")).add_to(m)

folium.PolyLine(locations=[sehrekustu,ulucami],color="red" ,weight=5,opacity=0.7).add_to(m)
m.save("bursa_rota.html")
