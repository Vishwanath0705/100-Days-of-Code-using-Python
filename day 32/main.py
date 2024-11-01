import random
from datetime import datetime
import pandas as pd
import smtplib

USERNAME = "vishwanath072005@gmail.com"
PASSWORD = "umhairisxysxudxv"

now = datetime.now()
today = (now.month,now.day)

data = pd.read_csv("birthdays.csv")
birth_day_dict = {(data_row["month"],data_row["day"]): data_row for (index,data_row) in data.iterrows()}
birthdays = data.to_dict(orient="records")

if today in birth_day_dict:
    birthday_person = birth_day_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as file:
        contents = file.read()
        replaced_contents = contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(USERNAME,PASSWORD)
        connection.sendmail(from_addr=USERNAME,to_addrs=birthday_person["email"],msg=f"Subject : Happy Birthday !!\n\n{contents}")