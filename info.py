class person():
    def __init__(self,name,age) :
        self.name = name
        self.age = age

    def sent_name(self):
        print(f'his name is {self.name} ')

    def sent_age(self):
        print(f'{self.name} is {self.age}')
    
    def sent_city(self):
        print(f'{self.name} is born in london')

    def sent_job(self):
        print(f'{self.name} is mechanic and he is working in company')

    def sent_leave(self):
        print(f'{self.name} leaving in liverpol')

i = person('ali',32)
i.sent_job()
i.sent_leave()