import folium
m = folium.Map(location=[41.0082,28.9784], zoom_start=13)
folium.Marker(location =[41.0256, 28.9741],popup ="Galata Kulesi", tooltip="Tıkla!", icon =folium.Icon(color="red", icon="info-sign")).add_to(m)
m.save("İsaretli_harita.html")
