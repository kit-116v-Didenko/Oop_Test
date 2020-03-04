from manage import Manage
from person import Person


class Deportament:
    def __init__(self,*args):
        self.args = args


    def showAll(self):
        for obj in self.args:
            print(obj)

    def giveRaise(self,procent):
        for obj in self.args:
            obj.giveraise(procent)





if __name__ == "__main__":

    d1 = Person('Nikita Didenko','Developers',3000)
    d2 = Person('Andrey Didenko','Developers',300)
    d3 = Person('Elena Didenko','Developers',200)
    d4 = Manage('Katy Didenko',100)
    my_Family = Deportament(d1,d2,d3,d4)
    my_Family.giveRaise(10)
    my_Family.showAll()
    
