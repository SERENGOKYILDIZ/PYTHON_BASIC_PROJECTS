from config import *
from twilio.rest import Client
import time

account_sid = sid
auth_token = token
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_=Twillo_phone,
    body="Selam yakışıklı",
    to=victim
)

print(message.sid)
