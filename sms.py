from twilio.rest import Client


account_sid = 'AC273e5da71863296812be1acd90a68da6'
auth_token = '42a4f9f5fa45d16d4f33beac1e90160e'
client = Client(account_sid, auth_token)


def send_fire_detection_sms(to_phone_number, from_phone_number, message_body):
    message = client.messages.create(
        body=message_body,
        from_='+17625503911',
        to='+919353418569'
    )
    return message.sid


to_phone_number = '+1234567890'  
from_phone_number = '+0987654321'  
message_body = 'Alert! Fire detected in the monitored area. Please take immediate action.'

message_sid = send_fire_detection_sms(to_phone_number, from_phone_number, message_body)
print(f'Message sent with SID: {message_sid}')
