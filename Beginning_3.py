import folium
sehrekustu_konumu = [40.1886, 29.0620]
ulu_cami_konumu = [40.1839, 29.0619]

m = folium.Map(location = sehrekustu_konumu, zoom_start=15)
folium.Marker(location =ulu_cami_konumu,popup="Bursa Ulu Cami",tooltip="Buraya Tıkla!",icon=folium.Icon(color="green",icon="info_sign")).add_to(m)
folium.Marker(location =sehrekustu_konumu,popup="Şehreküstü Meydanı" , icon =folium.Icon(color="red",icon="user")).add_to(m)

m.save("bursa_haritasi.html")
