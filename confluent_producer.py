from confluent_kafka import Producer
from dotenv import load_dotenv
import requests
import json
import time
import os
load_dotenv()  # Load environment variables from .env fil

API_KEY = os.getenv("OPEN_WEATHER_API_KEY")  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
TOPIC = os.getenv("KAFKA_TOPIC") # Replace with your Kafka topic nam

producer_conf = {
    'bootstrap.servers': os.getenv("KAFKA_BOOTSTRAP_SERVERS"),  # Replace with your Kafka bootstrap server
    'security.protocol': 'SASL_SSL',
    'sasl.mechanism': 'PLAIN',
    'sasl.username': os.getenv("CONFLUENT_API_KEY"),  #
    'sasl.password': os.getenv("CONFLUENT_API_SECRET"),  # Replace with your Confluent Cloud API key and secret
    'client.id': os.getenv("KAFKA_CLIENT_ID")  # Replace with your client ID
}
producer = Producer(producer_conf)

cities = [
    ("Nairobi", "KE"),
    ("Johannesburg", "ZA"),
    ("Minneapolis", "US"),
    ("Perth", "AU"),
    ("Osaka", "JP"),
    ("Seoul", "KR"),
    ("Atlanta", "US")
]

def fetch_weather(city, country):
    params = {
        "q": f"{city},{country}",
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            "city": city,
            "country": country,
            "timestamp": int(time.time()),
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
    else:
        print(f"Error fetching weather for {city}: {response.json().get('message')}")
        return None

while True:
    for city, country in cities:
        weather = fetch_weather(city, country)
        if weather:
            producer.produce(TOPIC, json.dumps(weather).encode('utf-8'))
            producer.flush()
            print("Produced:", weather)
    time.sleep(5)
