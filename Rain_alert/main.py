import requests
from twilio.rest import Client
import os


api_key = os.environ("API_KEY")
account_sid = os.environ("ACCOUNT_SID")
auth_token = os.environ("AUTH_TOKEN")


parameters = {
    'lat': '21.247208',
    'lon': '75.303146',
    'appid': api_key,
    'cnt': 4,
}
# cnt is the no of timeperiod needed, since the api being used is of 5 days 3 hours each, 4 means for next 12 hours

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
will_rain = False
for day_period in range(0, 4):
    weather_code = data['list'][day_period]['weather'][0]['id']
    # in weathermap documentation 'id' 's value determines the weather, less than 800 indicates the sky is not clear
    if int(weather_code) < 800:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Carry an Umbrella today",
        from_="+15033601589",
        to="+91 88559 50757"
    )
    print(message.status)