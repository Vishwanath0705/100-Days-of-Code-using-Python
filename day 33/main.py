import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 17.439930
MY_LONG = 78.498276

MY_EMAIL = "vishwanath072005@gmail.com"
MY_PASSWORD = "grsv2811"
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5<=iss_latitude<=MY_LAT+5 and MY_LONG-5<=iss_longitude<=MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat" : MY_LAT,
        "lng" : MY_LONG,
        "formatted" : 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)

    time_now = datetime.now().hour
    if time_now>=sunset or time_now<=sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL,MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg="Subject:Look up!!\n\nThe ISS is above you.Look up")