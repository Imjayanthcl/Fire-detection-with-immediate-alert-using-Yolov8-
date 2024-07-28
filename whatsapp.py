from twilio.rest import Client
from geopy.geocoders import Nominatim
import geocoder


account_sid = 'AC273e5da71863296812be1acd90a68da6'
auth_token = '42a4f9f5fa45d16d4f33beac1e90160e'
client = Client(account_sid, auth_token)
message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=r"fire detected in monitored area go fast",
        to='whatsapp:+919353418569'
            )

def get_ip_location():
    try:
       
        g = geocoder.ip('me')
        if g.ok:
            ip = g.ip
            latitude = g.latlng[0]
            longitude = g.latlng[1]
            return ip, latitude, longitude
        else:
            print("Geocoder failed to get location.")
            return None, None, None
    except Exception as e:
        print(f"Error getting IP location: {e}")
        return None, None, None


def get_address(latitude, longitude):
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.reverse(f"{latitude}, {longitude}", exactly_one=True)
        return location.address
    except Exception as e:
        print(f"Error getting address: {e}")
        return None

if __name__ == "__main__":
    ip, latitude, longitude = get_ip_location()
    if ip:
        print(f"IP Address: {ip}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
        
        
        address = get_address(latitude, longitude)
        if address:
            print(f"Address: {address}")
            
            
            google_maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
            print(f"Google Maps Link: {google_maps_link}")
            
            
            message_body = f"Fire detected "
            
            
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body=message_body,
                to='whatsapp:+919353418569'
            )
            print(f"WhatsApp message sent with SID: {message.sid}")
            
        else:
            print("Could not get the address.")
    else:
        print("Could not get the location.")
