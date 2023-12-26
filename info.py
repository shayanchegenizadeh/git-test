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
    
    def sent_mar(self):
        print(f'{self.name} married with maryam in 2016')
    
    def sent_ch(self):
        print(f'{self.name} have one child her name is Sogol')

i = person('ali',32)
i.sent_job()
i.sent_mar()
i.sent_ch()