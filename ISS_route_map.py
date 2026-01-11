import folium, requests, time

iss_rotasi = []
for i in range(3):
    url = "http://api.open-notify.org/iss-now.json"
    cevap = requests.get(url)
    veri = cevap.json()
    
    enlem = float(veri['iss_position']['latitude'])
    boylam = float(veri['iss_position']['longitude'])
    iss_rotasi.append([enlem,boylam])
    print(f"{i + 1}. Ölçüm Alındı: {enlem}, {boylam}")
    time.sleep(10)
    
print(f"ISS Şu an burada: Enlem {enlem}, Boylam {boylam}")

m = folium.Map(location=iss_rotasi[-1], zoom_start=3, tiles="CartoDB dark_matter")
folium.Marker(iss_rotasi[0],popup="Başlangıç",tooltip="ISS (Uluslararası Uzay İstasyonu)",icon=folium.Icon(color="green")).add_to(m)
folium.Marker(iss_rotasi[-1],popup="Bitiş (Şuan)", tooltip="ISS (Uluslararası Uzay İstasyonu)",icon=folium.Icon(color="red",icon = "rocket",prefix="fa")).add_to(m)

folium.Circle(location=[enlem, boylam],radius=500000,  color="yellow",fill=True,fill_opacity=0.2
).add_to(m)

folium.PolyLine(locations =iss_rotasi,color="cyan",weight=5,opacity=0.8).add_to(m)

m.save("iss_rota_haritası.html")

print("Harita oluşturuldu: iss_canli_konum.html")
