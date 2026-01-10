import folium
ulucami = [40.1839, 29.0619]
m = folium.Map(location =ulucami, zoom_start=16)
folium.Marker(ulucami, popup="Merkez", icon=folium.Icon(color="black")).add_to(m)

folium.Circle(location=ulucami,radius=300,color="gray",fill=True,fill_color="red",fill_opacity=0.3,popup="300 metre etki alanı").add_to(m)

m.save("ulucami_cember.html")
