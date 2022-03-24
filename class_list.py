class PrefectsList:
	name = ['Corey','Tim', 'forlan', 'navin', 'Johns']
	def __init__(self, Firstname, Lastname, Class, Pre_post, Department):
		self.Firstname = Firstname
		self.Lastname = Lastname
		self.Class = Class
		self.Pre_post = Pre_post
		self.Department = Department
	def get_name(self, candidate_name):
		return f' Name of candidate is {self.Firstname}-{self.Lastname}'
	def get_prefect_post(self, candidtae_name):
		return self.Pre_post
	def get_class(self, candidate_name):
		return self.Class
	def get_department(self, candidate_name):
		return self.Department
name = ['Corey','Tim', 'forlan', 'navin', 'Johns']
surnmae = ['Schafer', 'Cook', 'Gates', 'Reddy', 'jeff']
Class = ['SS2A', 'SS1D', 'SS2C', 'SS3D', 'SS2B']
posts = ['Head boy', 'time-keeper', 'labour-prefect', 'social-prefect', 'Health-prefect']
Departments = ['Science', 'Hummanities', 'Arts', 'Commercial', 'Transport']

cand_name = 'kenny'
if cand_name in name:
	p = name.index(cand_name)
	Jakande_prefects_2021 = PrefectsList(name[p], surnmae[p], Class[p], posts[p], Departments[p])
	print(Jakande_prefects_2021.get_prefect_post(cand_name))
else:
	print("Name not found, try entering the student's first name")


				
