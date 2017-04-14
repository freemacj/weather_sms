import json
import urllib.request as request
from config import api_key, zip_code, account_sid, auth_token, phone_number, twilio_number
from twilio.rest import TwilioRestClient

import datetime
d_date = datetime.datetime.now()
reg_format_time = d_date.strftime("%I:%M %p")

fileName = "http://api.wunderground.com/api/" + api_key + "/geolookup/conditions/q/PA/" + zip_code + ".json"
f = request.urlopen(fileName)
json_string = f.read().decode('utf-8')
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
city = parsed_json['location']['city']
state = parsed_json['location']['state']
weather = parsed_json['current_observation']['weather']
temperature_string = parsed_json['current_observation']['temperature_string']
feelslike_string = parsed_json['current_observation']['feelslike_string']
my_weather = (str(reg_format_time) + ' Weather in ' + city + ', ' + state + ': ' + weather.lower() + '. The temperature is ' + temperature_string + ' but it feels like ' + feelslike_string + '.')
f.close()

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body=my_weather,
    to=phone_number,    # Replace with your phone number
    from_=twilio_number) # Replace with your Twilio number

print(message.sid)
