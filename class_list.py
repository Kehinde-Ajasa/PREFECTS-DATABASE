class PrefectsList:
    def __init__(self, Firstname, Lastname, Class, Pre_post, Department):
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.Class = Class
        self.Pre_post = Pre_post
        self.Department = Department

    def get_name(self, candidate_name):
        return f' Name of candidate is {self.Firstname}-{self.Lastname}'

    def get_prefect_post(self, candidtae_name):
        return f'The post {self.Firstname}-{self.Lastname} is running for is {self.Pre_post}'

    def get_class(self, candidate_name):
        return f'The class {self.Firstname}-{self.Lastname} belongs to is {self.Class}'

    def get_department(self, candidate_name):
        return f'The Department {self.Firstname}-{self.Lastname} belongs to is {self.Department}'


name = ['corey', 'tim', 'forlan', 'navin', 'johns', 'flemming', 'patience', 'gustavo', 'layla', 'olivia']
surname = ['schafer', 'cook', 'gates', 'reddy', 'jeff', 'alex', 'vera', 'alberto', 'lane', 'baker']
Class = ['SS2A', 'SS1D', 'SS2C', 'SS3D', 'SS2B', 'SS1A', 'SS3E', 'SS2D', 'SS3A', 'SS1F']
posts = ['Head boy', 'time-keeper', 'labour-prefect', 'social-prefect', 'Health-prefect', 'Laboratory-prefect',
         'Asst.Head-Girl', 'Sports-prefect', 'Social-prefect', 'Head-girl']
Departments = ['Science', 'Hummanities', 'Arts', 'Commercial', 'Transport', 'Science', 'Arts', 'Science', 'Commercial',
               'Commercial']

cand_name = input('Enter name of candidate you would like to check information on: ')
info_type = input('what type of information do you want on this candidate: ').lower()
if cand_name.lower() in name:
    p = name.index(cand_name.lower())
    Jakande_prefects_2021 = PrefectsList(name[p], surname[p], Class[p], posts[p], Departments[p])
    # Using index to find the position of the candidate name in the list of names
    if info_type == 'department':
        print(Jakande_prefects_2021.get_department(cand_name))
    elif info_type == 'post':
        print(Jakande_prefects_2021.get_prefect_post(cand_name))
    elif info_type == 'class':
        print(Jakande_prefects_2021.get_class(cand_name))
    else:
        print('Sorry we dont have any database on that yet we are working on our end to get it to you'
              '\nTry checking the spelling of the information type')
elif cand_name.lower() in surname:
    p = surname.index(cand_name.lower())
    Jakande_prefects_2021 = PrefectsList(name[p], surname[p], Class[p], posts[p], Departments[p])
    print(Jakande_prefects_2021.get_department(cand_name))
else:
    print("Name not found, try entering the student's first name")
