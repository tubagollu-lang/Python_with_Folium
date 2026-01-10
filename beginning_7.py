import folium
from folium.plugins import MousePosition
ulucami = [40.1839, 29.0619]
m = folium.Map(location =ulucami, zoom_start=16)
folium.Marker(ulucami, popup="Merkez", icon=folium.Icon(color="black")).add_to(m)
folium.Circle(location=ulucami,radius=300,color="gray",fill=True,fill_color="red",fill_opacity=0.3,popup="300 metre etki alanı").add_to(m)
formatter = "function(num) {return L.Util.formatNum(num, 5);};"
MousePosition(position='topright',separator=' | ',empty_string='NaN',lng_first=False,num_digits=20,prefix='Koordinat:',lat_formatter=formatter,lng_formatter=formatter,).add_to(m)

m.save("ulucami_koordinatli.html")
