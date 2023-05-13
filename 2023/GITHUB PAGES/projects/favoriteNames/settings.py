
class Settings:

	def __init__(self):
		self.active = False
		self.fav_names_location = "data/fav_names.json"
		self.users_location = "data/users.json"

		self.fav_names = None 
		self.users = None

		self.menu = """
*APLIKASI FAVAPP*
1. VIEW	ALL NAME AND FAVORITE
2. FIND THE NAME WITH FAVORITE BY NAME
3. ADD NEW NAME AND FAVORITE
4. UPDATE NAME AND FAVORITE
5. REMOVE NAME AND FAVORITE
Q. EXIT
"""