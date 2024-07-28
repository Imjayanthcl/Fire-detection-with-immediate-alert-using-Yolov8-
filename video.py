from twilio.rest import Client


account_sid = 'AC273e5da71863296812be1acd90a68da6'
auth_token = '42a4f9f5fa45d16d4f33beac1e90160e'

client = Client(account_sid, auth_token)
room = client.video.rooms.create(unique_name='my-room-name')
print(f"Room SID: {room.sid}")
participant_token = client.tokens.create(identity='participant-identity', video_grants=[{
    'room': room.sid
}])
print(f"Participant Token: {participant_token}")
