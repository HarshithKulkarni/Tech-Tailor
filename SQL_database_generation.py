from iter_count import count
from firebase import firebase
import sqlite3



name = []
email = []
gender  = []
phone = []



def create_sql():
	print("SQL Database creating...")
	conn = sqlite3.connect("Database.db")
	print("SQL Database Created Successfully!!")
	c = conn.cursor()
	c.execute('''CREATE TABLE `1` (`Name`	REAL,`Email`	REAL,`Gender`	REAL,`Phone Number`	REAL)''')
	return (conn,c)


def import_and_write(conn,c):

	print("Importing Data From Firebase...")
	fb = firebase.FirebaseApplication('https://image-db-d8b91.firebaseio.com/')
	print("Uploading Data To SQL...")
	for i in range(1,(count)):
		name = fb.get('/Tech-Tailor/{}'.format(i),'Name')
		email  = fb.get('/Tech-Tailor/{}'.format(i),'Email')
		gender = fb.get('/Tech-Tailor/{}'.format(i),'Gender')
		phone = fb.get('/Tech-Tailor/{}'.format(i),'Phone Number')
		c.execute('''INSERT INTO `1` VALUES(?,?,?,?)''',(name,email,gender,phone))
		conn.commit()
		#print(name)
		#print(email)
		#print(gender)
		#print(phone)
	print("Data Uploaded to SQL Successfully!!")


if(__name__=="__main__"):
	

	file = open("count.txt","r")
	Saved_Count = file.read()
	Saved_Count = int(Saved_Count)
	if(Saved_Count == (count-1)):
		print("same!!")
	else:
		print("Not same!!")
	conn , c = create_sql()	
	import_and_write(conn,c)
