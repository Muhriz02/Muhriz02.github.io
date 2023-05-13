from os import system
import json
from getpass import getpass

from settings import Settings
from user import User
from fav_name import Fav_name

class FavApp:

	def __init__(self):
		self.settings = Settings()
		#self.active = True

	def load_data(self):
		try:
			with open(self.settings.fav_names_location, 'r') as file:
				self.settings.fav_names = json.load(file)
		except:
			self.settings.fav_names = {}

		try:		
			with open(self.settings.users_location, 'r') as file:
				self.settings.users = json.load(file)
		except:
			self.settings.users = {}
		#print(self.settings.contacts , self.settings.users)

	def clear_screen(self):
		try:
			system("cls")
		except:
			system("clear")

	def logger(self):
		self.clear_screen()
		self.login_attempts = 0 
		while self.login_attempts < 3:
			print("\nPlease Login")
			username = input("Username\t: ")
			password = getpass("Password\t: ")

			if username in self.settings.users:
				if self.settings.users[username]["password"] == password:
					self.user = User(username,
						first=self.settings.users[username]['first'],
						last=self.settings.users[username]["last"],
						password="")
					return True
			else:
				print("Login Failed")
			self.login_attempts += 1

		return False

	def show_menus(self):
		self.clear_screen()
		print(self.settings.menu)

	def find_fav_name(self, name):
		fav_names = self.settings.fav_names 
		if name in fav_names:
			print("Name found!")
			print(f"Name: {name}")
			print(f"Favorite Food/Drink/country: {fav_names[name]['fav_food']}/{fav_names[name]['fav_drink']}/{fav_names[name]['fav_country']}")
			return True
		else:
			print("Name doesn't exists")

	def save_data(self):
		with open(self.settings.fav_names_location, 'w') as file:
			json.dump(self.settings.fav_names, file)
					
	def check_option_user(self, char):
		if char ==  'q':
			self.settings.active = False
		elif char == "1":

			self.clear_screen()
			#print(self.settings.contacts)
			fav_names = self.settings.fav_names
			print(f"Name\t\tFavorite Food/drink/country")

			for name, fav_name in fav_names.items():
				print(f"{name}\t\t{fav_name['fav_food']}/{fav_name['fav_drink']}/{fav_name['fav_country']}")

			input("Press Enter to Return.")

		elif char == "2":
			
			self.clear_screen()
			name = input("Enter name : ")

			self.find_fav_name(name)

			input("Press Enter to Return")

		elif char == "3":
			
			self.clear_screen()
			name = input("Name : ")
			fav_food = input("Favorite food : ")
			fav_drink = input("Favorite Drink : ")
			fav_country = input("Favorite Country : ")

			fav_name = Fav_name(fav_food, fav_drink, name, fav_country)
			self.settings.fav_names[fav_name.name] = {
				"fav_food" : fav_name.fav_food,
				"fav_drink" : fav_name.fav_drink,
				"fav_country" : fav_name.fav_country
			}

			self.save_data()

			print("Name saved.")
			input("Press Enter to Return.")

		elif char == "4":

			self.clear_screen()
			name = input("Name : ")

			if self.find_fav_name(name):
				print("Edit\n1. Name, 2. Favorite Food, 3. Favorite Drink, 4. Favorite Country")
				option = input("Which data do you want to edit / update ? (1/2/3/4)")
				if option == "1":
					
					old_fav_name = self.settings.fav_names[name]
					new_name = input("New name : ")

					self.settings.fav_names[new_name] = {
						"fav_food" : old_fav_name["fav_food"],
						"fav_drink" : old_fav_name["fav_drink"],
						"fav_country" : old_fav_name["fav_country"]
					}

					del self.settings.fav_names[name]
					self.save_data()
					print("New name saved.")

				if option == "2":
					
					new_fav_food = input("New Favorite Food : ")
					self.settings.fav_names[name]["fav_food"] = new_fav_food
					self.save_data()
					print("New Favorite Food saved.")

				if option == "3":
					
					new_fav_drink = input("New Favorite Drink : ")
					self.settings.fav_names[name]["fav_drink"] = new_fav_drink
					self.save_data()
					print("New Favorite Drink saved.")

				if option == "4":
					
					new_fav_country = input("New Favorite Country : ")
					self.settings.fav_names[name]["fav_country"] = new_fav_country
					self.save_data()
					print("New Favorite Country saved.")

		elif char == "5":
			
			self.clear_screen()
			name = input("Name : ")

			if self.find_fav_name(name):
				confirm = input("Are you sure delete this name and favorite ? (y/n)")
				if confirm.lower() == "y":
					del self.settings.fav_names[name]
					
					self.save_data()
					print("Name and favorite deleted.")


			input("Press Enter to Return.")

	def run(self):
		self.load_data()
		self.settings.active = self.logger()

		while self.settings.active:
			self.show_menus()
			self.check_option_user(input("option: ").lower())

		
if __name__ == '__main__':
	app = FavApp()
	app.run()