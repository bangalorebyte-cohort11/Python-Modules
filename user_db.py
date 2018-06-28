""" Create a user database (login, password, and last login timestamp) class (see problems 7-5 and 9-12) that manages a system requiring users to log in before access to resources is allowed. This database class manages its users, loading any previously saved user information on instantiation and providing accessor functions to add or update database information. If updated, the database will save the new information to disk as part of its deallocation (see __del__())."""
#data to be stored
# - username
# - password
# - last_login
import time
import sys
from datetime import datetime



db = {}
db 

class User_db:
	def __init__(self,username,password,last_login):
		self.username = username
		self.password = password
		self.last_login = last_login
	# def update(self,username,password):




	def print_hello():
		print("hello")

	def show_user_credential(self):
		print("Username:",self.username)
		print("password:",self.password)
		print("login time:",self.last_login)

	def new_user(self):
		username = input("Hi,please enter your desired username: ")
		while True:
			if (username) in db:
				prompt = 'name taken, try another: '
				continue
			else:
				break 
		password = input('password: ')
		db[username] = password
		db['last_login'] = str(datetime.now())
		print("Done, the time now is",str(datetime.now()))
		User_db.show_menu(self)
	def old_user(self):
		username = input('username: ')
		password = input('password: ')
		passwd = db.get(username) # db[username]
		if passwd == password:
			print ('welcome back', username)
		else:
			print ('login incorrect')

	def delete_user(self):
		delete = input("Which username would you like to delete:")
		del db[delete]
		print("name deleted")
		print(db)

	def update_password(self):
		user = input("which password would you like to update?")
		print("Cool! User found!")
		update = input("Please enter new password:")
		db[user] = update

	def show_menu(self):
		prompt = input('(N)ew User Login\n(E)xisting User Login\n(Q)uit\n (D)elete User \nEnter choice: ')
		if prompt == 'n' :
			User_db.new_user(self)
		if prompt == 'e':
			User_db.old_user(self)
		if prompt == 'd':
			User_db.delete_user(self)
		if prompt == 'q':
			sys.exit()

uday = User_db("Uday","password",datetime.now())
uday.show_menu()
uday.show_user_credential()
print(db)


