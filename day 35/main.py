import requests
from twilio.rest import Client

OWN_END = "https://api.openweathermap.org/data/2.5/weather"
api_key = "519c7d6ca9c732bb1350e354bf398f37"


weather_params = {
    "lat": 17.439930,
    "lng": 78.498276,
    "appid": api_key,
}

response = requests.get(OWN_END,params=weather_params)



will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER"
    )
    print(message.status)