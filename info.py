class person():
    def __init__(self,name,age) :
        self.name = name
        self.age = age

    def sent_name(self):
        print(f'his name is {self.name} ')

    def sent_age(self):
        print(f'{self.name} is {self.age}')

i = person('ali',32)
i.sent_name()
i.sent_age()