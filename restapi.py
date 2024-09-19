import requests
import folium

# Maak de API-request naar de OpenStreetMap Nominatim API
url = "https://nominatim.openstreetmap.org/search?format=json&q=Roermond"
headers = {'Accept': 'application/json'}

try:
    response = requests.get(url, headers=headers)

    # Controleer of de response succesvol is
    if response.status_code == 200:
        try:
            # Parse de JSON-response
            data = response.json()

            # Controleer of er resultaten zijn
            if data:
                latitude = float(data[0]['lat'])
                longitude = float(data[0]['lon'])

                # Maak een kaart met de coördinaten van Roermond
                map_osm = folium.Map(location=[latitude, longitude], zoom_start=12)

                # Voeg een marker toe op de locatie
                folium.Marker([latitude, longitude], popup="Roermond").add_to(map_osm)

                # Sla de kaart op als een HTML-bestand
                map_osm.save("map_with_marker.html")
                print("Kaart met marker opgeslagen als 'map_with_marker.html'.")
            else:
                print("Geen locatie gevonden.")
        except requests.exceptions.JSONDecodeError:
            print("Fout bij het decoderen van de JSON-response.")
    else:
        print(f"Request mislukt met statuscode: {response.status_code}")
        print("Response tekst:", response.text)

except requests.RequestException as e:
    print(f"Er is een fout opgetreden tijdens de API-request: {e}")
