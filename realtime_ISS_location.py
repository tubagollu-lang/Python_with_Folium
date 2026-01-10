import folium, requests
url = "http://api.open-notify.org/iss-now.json"
cevap = requests.get(url)
veri = cevap.json()
enlem = float(veri['iss_position']['latitude'])
boylam = float(veri['iss_position']['longitude'])

print(f"ISS Şu an burada: Enlem {enlem}, Boylam {boylam}")

m = folium.Map(location=[enlem, boylam], zoom_start=3, tiles="CartoDB dark_matter")
folium.Marker(location=[enlem, boylam],popup=f"ISS Konumu\nEnlem: {enlem}\nBoylam: {boylam}",tooltip="ISS (Uluslararası Uzay İstasyonu)",icon=folium.Icon(color="red", icon="cloud", prefix='fa')
).add_to(m)

folium.Circle(location=[enlem, boylam],radius=500000,  color="yellow",fill=True,fill_opacity=0.2
).add_to(m)

m.save("iss_canli_konum.html")

print("Harita oluşturuldu: iss_canli_konum.html")
