##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

##################### IMPORTS ######################
import datetime as dt
import pandas as pd
import smtplib
import random

from user_info import EMAIL, PASSWORD

##################### CONSTANTS ######################
BIRTHDAYS_DB = 'birthdays.csv'
letter_paths = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
SUBJECT = 'Happy Birthday'
TO = 'dcastillo.st@gmail.com'
TEXT = 'Here is a message from python.'
MESSAGE = f'Subject:{SUBJECT}\n\n{TEXT}'

##################### FUNCTIONS ######################
def get_todays_bdays(df):
    return df[(df['month'] == now.month)
        & (df['day'] == now.day)].index.tolist()

def pick_letter(name):
    letter_path = random.choice(letter_paths)
    try:
        with open('letter_templates/' + letter_path, 'r') as f:
            letter = f.read()
    except FileNotFoundError:
        letter = f'Happy birthday, {name}'
    else:
        letter = letter.replace('[NAME]', name)
    finally:
        return letter

def format_message(subject=SUBJECT, body=TEXT):
    return f'Subject:{subject}\n\n{body}'

def send_mail(recipient=TO, message=MESSAGE):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=recipient, msg=message)


birthdays = pd.read_csv(BIRTHDAYS_DB)
now = dt.datetime.now()
bday_list = get_todays_bdays(birthdays)

if bday_list:
    for bday in bday_list:
        name = birthdays["name"].loc[bday]
        email = birthdays["email"].loc[bday]
        letter = pick_letter(name)
        subject = 'Happy Birthday!'
        message = format_message(subject=subject, body=letter)
        send_mail(recipient=email, message=message)
        print(message)



