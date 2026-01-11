import folium, requests, time 

iss_rotasi = [] 

print("Daha sağlam bir API ile bağlanılıyor... (Lütfen bekleyin)")

for i in range(5):
    try:
        url = "https://api.wheretheiss.at/v1/satellites/25544"
        cevap = requests.get(url)
        veri = cevap.json()
        
        enlem = float(veri['latitude'])
        boylam = float(veri['longitude'])
        
        iss_rotasi.append([enlem, boylam])
        
        print(f"{i+1}. Veri Çekildi: {enlem}, {boylam}")
        
        time.sleep(3)
        
    except Exception as hata:
        print(f"Bir hata oldu ama devam ediyoruz: {hata}")
        continue

print("Veri toplama bitti, harita çiziliyor...")

if len(iss_rotasi) > 0:
    m = folium.Map(location=iss_rotasi[-1], zoom_start=3, tiles="CartoDB dark_matter")

    folium.PolyLine(iss_rotasi, color="cyan", weight=5, opacity=0.8).add_to(m)

    folium.Marker(iss_rotasi[0], popup="Başlangıç", icon=folium.Icon(color="green")).add_to(m)
    folium.Marker(iss_rotasi[-1], popup="Şimdi", icon=folium.Icon(color="red", icon="rocket", prefix="fa")).add_to(m)

    m.save("iss_rota_haritasi_v2.html")
    print("Başarılı! 'iss_rota_haritasi_v2.html' dosyasına bakabilirsin.")
else:
    print("Maalesef hiç veri çekemedik, internet bağlantını kontrol et.")
