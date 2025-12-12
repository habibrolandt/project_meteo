import os
import requests
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()
API_KEY = os.getenv("API_KEY")
print("API_KEY chargée:", API_KEY)


def fetch_weather(city: str):
    """Récupère les données météo pour une ville donnée."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=fr"
    response = requests.get(url, timeout=10)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erreur {response.status_code} pour la ville {city}")
        return None

if __name__ == "__main__":
    data = fetch_weather("Abidjan")
    print(data)
