import pandas as pd
from datetime import datetime, UTC

def clean_weather_data(raw_json: dict):
    """Transforme le JSON brut en DataFrame normalisé."""
    if raw_json is None:
        return None
    
    data = {
        "ville": raw_json.get("name"),
        "pays": raw_json.get("sys", {}).get("country"),
        "date": datetime.fromtimestamp(raw_json.get("dt"), UTC),
        "temperature": raw_json.get("main", {}).get("temp"),
        "humidite": raw_json.get("main", {}).get("humidity"),
        "pression": raw_json.get("main", {}).get("pressure"),
        "condition": raw_json.get("weather", [{}])[0].get("description"),
        "vent_vitesse": raw_json.get("wind", {}).get("speed"),
        "vent_direction": raw_json.get("wind", {}).get("deg"),
        "nuages": raw_json.get("clouds", {}).get("all"),
    }
    
    return pd.DataFrame([data])

if __name__ == "__main__":
    # Exemple avec un JSON récupéré
    from fetch_data import fetch_weather
    raw = fetch_weather("Abidjan")
    df = clean_weather_data(raw)
    print(df)
