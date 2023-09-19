class User:

    def __init__(self, first_name, last_name):
       self.name = first_name
       self.surName = last_name
    def sayName(self):
        print(self.name)
    def saySurName(self):
        print(self.surName) 
    def sayFullName(self):
        print(self.name, self.surName) 
