import pyrebase

config = {
	
	"apiKey": "AIzaSyAhusK8H900iMxt7k-IRqyIgmJASQkzhIc",
    "authDomain": "image-db-d8b91.firebaseapp.com",
    "databaseURL": "https://image-db-d8b91.firebaseio.com",
    "projectId": "image-db-d8b91",
    "storageBucket": "image-db-d8b91.appspot.com",
    "messagingSenderId": "442834729478"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
count = 0
for i in (db.child("Tech-Tailor").get().each()):
    count+=1
