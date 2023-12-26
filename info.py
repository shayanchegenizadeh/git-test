class person():
    def __init__(self,name) :
        self.name = name

    def sent(self):
        print(f'hello {self.name} ')

i = person('ali')
i.sent()
