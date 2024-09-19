
# OpenStreetMap API Marker Visualisatie

Dit project maakt gebruik van de [OpenStreetMap Nominatim API](https://nominatim.org/release-docs/latest/api/Search/) om locaties te zoeken en de verkregen latitude en longitude te gebruiken om een marker op een kaart te plaatsen met behulp van de [folium](https://python-visualization.github.io/folium/) bibliotheek.

## Inhoud
- [Installatie](#installatie)
- [Gebruik](#gebruik)
- [Functies](#functies)
- [Probleemoplossing](#probleemoplossing)
- [Licentie](#licentie)

## Installatie

1. Clone de repository of download de bestanden naar je lokale machine.

2. Installeer de benodigde Python-pakketten:

    ```bash
    pip install requests folium
    ```

3. Zorg ervoor dat je Python 3.x hebt geïnstalleerd.

## Gebruik

1. Voer het Python-script uit `restapi.py` om een API-aanroep te doen naar de Nominatim API, de coördinaten van een locatie (bijvoorbeeld Roermond) op te halen en deze weer te geven op een kaart.

    ```bash
    python restapi.py
    ```

2. Het script genereert een bestand `map_with_marker.html`, dat je kunt openen in je webbrowser om de kaart met de marker te bekijken.

## Functies

- **API-aanroep**: Het script maakt een `GET`-request naar de Nominatim API om locaties te zoeken.
- **JSON-parsing**: Het script verwerkt de response en haalt de latitude en longitude van de opgezochte locatie op.
- **Kaartweergave**: Het script maakt een kaart met behulp van de `folium`-bibliotheek en plaatst een marker op de opgehaalde coördinaten.
- **Foutafhandeling**: Het script controleert of de API-request succesvol was en geeft nuttige foutmeldingen als er iets misgaat.

## Voorbeeld

Als je de coördinaten van Roermond zoekt, zal het script een kaart zoals deze genereren:

- **Latitude**: 51.19417
- **Longitude**: 5.99333
- Een marker wordt geplaatst op de kaart.

## Probleemoplossing

- Als je een foutmelding krijgt zoals `JSONDecodeError`, controleer dan of de API beschikbaar is en of je de juiste URL hebt gebruikt.
- Zorg ervoor dat je internetverbinding actief is en dat er geen firewall of proxy de toegang tot de API blokkeert.
- Controleer de response statuscode als de API-aanroep mislukt.


