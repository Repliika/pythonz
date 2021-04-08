
#collection of happy quotes

happy_quotes = {
    "You choose to make the best of the rest of the day"
    "Change happens the moment you decide"
    "Remember to laugh"
    "Yesterday is Yesterday"
    "Don't forget to breath"
    "Happiness is not something ready made. It comes from your own actions"
    "Remember to study"
    "People who wonder if the glass is half empty or full miss the point. The glass is refillable"
}

study_reminder = {
    "Don't forget to read notes! make it muscle memory"
}

#import modules
#credentials is where to input sensitive user info

import schedule, random, time
from credentials import *
from twilio.rest import Client


phone = phone_number
twilio_phone= twilio_number 


#send a random happy quote
def morning_message(quote_list=happy_quotes):
    account = account_sid
    account_token = auth_token
    quote = quote_list[random.randint(0, len(quote_list)-1)]
    
    client = Client(account_sid, auth_token)
    client.messages.create(to=phone_number, from_= twilio_number, body = quote)

#send reminder message
def reminder_message(quote=study_reminder):
    account = account_sid
    account_token = auth_token
    
    
    client = Client(account_sid, auth_token)
    client.messages.create(to=phone_number, from_= twilio_number, body = quote)



 
#schedule messages throughout the day


schedule.every().day.at("09:00").do(morning_message, happy_quotes)
schedule.every().day.at("17:00").do(reminder_message, study_reminder)


while True:
    schedule.run_pending()
    time.sleep(10)