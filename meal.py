#Meal Class
#Since meals are selected randomly, I will update each recipie when it is gets selected
#Instead of putting in every recipie

def recipie():
	def __init__(self):
		self.title = '' # Name of Dish
		self.weight = None ## Rating 0-10, 10 being the best
		self.ingredients = [] ## To Cross reference what I own to see what I need 
		self.page = None ## Page in cookbook for faster future reference
		self.difficulty = None ##  

	def rate(number):
		try:
			self.weight = int(number)
		except:
			print("'%s' is not a valid rating input!") % (number)

	def setDifficulty(number):
		try:
			self.difficulty = int(number)
		except:
			print("'%s' is not a valid difficulty input!") % (number)

	def setIngredients():
		print('Please answer the prompts, enter nothing to stop')
		ingredient = input('Enter an ingredient: ')
		amount = input('Enter the amount of that ingredient: ')
		self.ingredients.append([ingredient,amount])
		while ingredient != '':
			ingredient = input('Enter an ingredient: ')
			amount = input('Enter the amount of that ingredient: ')
			self.ingredients.append([ingredient,amount])

	def setTitle(title):
		self.title = title

	def setPage(page):
		try:
			self.page = int(page)
		except:
			print("'%s' is not a valid page number!") % (page)
	