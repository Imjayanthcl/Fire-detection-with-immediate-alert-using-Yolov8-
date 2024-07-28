from twilio.rest import Client

account_sid = 'AC273e5da71863296812be1acd90a68da6'
auth_token = '42a4f9f5fa45d16d4f33beac1e90160e'
client = Client(account_sid, auth_token)

def make_fire_detection_call(to_phone_number, from_phone_number, message_url):
    call = client.calls.create(
        url=message_url,
        from_='+17625503911',
        to='+919353418569'
    )
    return call.sid

to_phone_number = '+1234567890'  
from_phone_number = '+0987654321'  
message_url = 'https://handler.twilio.com/twiml/EHb25d86b3a729a10744720fd9b19553f7'  
call_sid = make_fire_detection_call(to_phone_number, from_phone_number, message_url)
print(f'Voice call initiated with SID: {call_sid}')
