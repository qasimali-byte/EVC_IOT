import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


def listener(event):
    print(event.event_type)  # can be 'put' or 'patch'
    print(event.path)  # relative to the reference, it seems
    print(event.data)  # new data at /reference/event.path. None if deleted


json_path = r'E:\Projectz\FYP\FreshOnes\Python\PastLocations\fyp-healthapp-project-firebase-adminsdk-40qfo-f8fc938674.json'
my_app_name = 'fyp-healthapp-project'
xyz = {'databaseURL': 'https://{}.firebaseio.com'.format(my_app_name),
       'storageBucket': '{}.appspot.com'.format(my_app_name)}

cred = credentials.Certificate(json_path)
obj = firebase_admin.initialize_app(cred, xyz, name=my_app_name)

db.reference('PatientMonitoring', app=obj).listen(listener)