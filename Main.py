import time
#Setup a loop to send Temperature values at fixed intervals in seconds
import pyrebase
Config = {
    'apiKey': "AIzaSyCdL3NSUDBQmwJUeKg3JLmrdqJtpYb01BY",
    'databaseURL':'https://evcdemo-e1ca2-default-rtdb.firebaseio.com',
    'authDomain': "evcdemo-e1ca2.firebaseapp.com",
    'projectId': "evcdemo-e1ca2",
    'storageBucket': "evcdemo-e1ca2.appspot.com",
    'messagingSenderId': "49608419769",
    'appId': "1:49608419769:web:2c1b57f139b1f67dae2e68",
    'measurementId': "G-YX6FK8EMC4"
}
firebase=pyrebase.initialize_app(Config)
db=firebase.database()


def stream_handler(message):
    # print(message["event"]) # put
    # print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}


my_stream = db.child("Temperatures").stream(stream_handler)