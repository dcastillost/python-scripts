import smtplib
import datetime as dt
import random

from user_info import EMAIL, PASSWORD

#Using smtplib
SUBJECT = 'TEST MAIL'
TO = 'dcastillo.st@gmail.com'
TEXT = 'Here is a message from python.'
MESSAGE = f'Subject:{SUBJECT}\n\n{TEXT}'

def send_mail(recipient=TO, message=MESSAGE):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=recipient, msg=message)
    # connection.close()

def format_message(subject=SUBJECT, body=TEXT):
    return f'Subject:{subject}\n\n{body}'

# Using the datetime library
now = dt.datetime.now()
weekday = now.weekday()

if weekday == 5:
    with open('quotes.txt', 'r', encoding='utf8') as f:
        all_quotes = f.readlines()
        quote = random.choice(all_quotes)
        for ix, char in enumerate('“”–'):
            new_char = '\"\"-'
            quote = quote.replace(char, new_char[ix])
        quote = quote.encode("utf-8").decode('ascii', 'ignore')
        send_mail(message=format_message(subject='today\'s motivation', 
                                         body=quote))
    
    print(quote)