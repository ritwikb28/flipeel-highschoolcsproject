import twilio
# importing the client from the twilio
from twilio.rest import Client
# Your Account Sid and Auth Token from twilio account
account_sid = "ACbaa1e8c95fbce188363d0564893b7356"
auth_token = "58b80e389304e29eafb203b73c62f43c"
# instantiating the Client
client = Client(account_sid, auth_token)
# sending message
message = client.messages.create(body='Hi there! How are you?', from_= "+919582229752", to= "+919958469795")
# printing the sid after success
print(message.sid)