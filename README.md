
#  Weather Data Streaming with Confluent Kafka

This project streams real-time weather data from the OpenWeatherMap API using a Kafka producer and consumes it using a Kafka consumer — both built with Python and powered by Confluent Cloud.

---

##  Table of Contents

* [Project Overview](#project-overview)
* [Prerequisites](#prerequisites)
* [Step 1: Set Up Confluent Cloud](#step-1-set-up-confluent-cloud)
* [Step 2: Get OpenWeatherMap API Key](#step-2-get-openweathermap-api-key)
* [Step 3: Clone and Set Up the Project](#step-3-clone-and-set-up-the-project)
* [Step 4: Configure Environment Variables](#step-4-configure-environment-variables)
* [Step 5: Run the Producer and Consumer](#step-5-run-the-producer-and-consumer)
* [Monitoring](#monitoring)
  

---

##  Project Overview

This project:

* Fetches real-time weather data from cities around the world.
* Sends the data to a Kafka topic using a Python Kafka Producer.
* Receives and prints the weather data using a Kafka Consumer.

---

##  Prerequisites

* Python 3.7+
* Confluent Cloud account
* OpenWeatherMap API key
* Virtual environment (recommended)

---

##  Step 1: Set Up Confluent Cloud

1. Create a free Confluent Cloud account:
    [https://confluent.cloud](https://confluent.cloud)

2. Create an environment:

   * Go to Environments → Add Environment

3. Create a Kafka Cluster:

   * Choose Basic (free tier) 
   * Pick a cloud provider and region
   * Name your cluster

4. Create a Kafka Topic:

   * Navigate to Topics → Create Topic
   * Name it weather-data

5. Create API Key & Secret:

   * Go to Cluster Settings → API Keys
   * Create API key for the cluster
   * Copy the API key, Secret, and Bootstrap Server

---

##  Step 2: Get OpenWeatherMap API Key

1. Sign up at: [https://openweathermap.org/api](https://openweathermap.org/api)
2. Go to API Keys → Copy your key

---

##  Step 3: Clone and Set Up the Project

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/weather-kafka-streaming.git
cd weather-kafka-streaming

# Create and activate virtual environment
python3 -m venv confluentenv
source confluentenv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

##  Step 4: Configure Environment Variables

Instead of hardcoding secrets, store them in a .env file:

.env

```bash
KAFKA_API_KEY=your_confluent_api_key
KAFKA_API_SECRET=your_confluent_secret
KAFKA_BOOTSTRAP_SERVER=your_bootstrap_server
WEATHER_API_KEY=your_openweather_api_key
```






##  Step 5: Run the Producer and Consumer

Open two terminal windows:

 Terminal 1 — Start the Producer

```bash
python confluent_producer.py
```

 Terminal 2 — Start the Consumer

```bash
python confluent_consumer.py
```

Make sure both scripts are in the same directory.

---

##  Monitoring

You can monitor from the Confluent Cloud Dashboard:

* Topic data flow → Topics → weather-data → Messages
* Consumer group metrics → Clients → Consumers

---


