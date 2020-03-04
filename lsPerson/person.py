from art_display  import AerDisplay


class Person(AerDisplay):
    def __init__(self,name,job,pay):
        self.job = job
        self.name = name
        self.pay = pay

    def lastname(self):
        return f'{self.name.split()[1]}'
    
    def giveraise(self,procent):

        self.pay += (self.pay + procent)//100

    
        

if __name__ == "__main__":


    bob = Person('Bob Petrovich','Developer',3300)
    bob.giveraise(10)
    print(bob)
