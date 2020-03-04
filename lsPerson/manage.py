from person import Person


class Manage(Person):
    def __init__(self,name,pay):
        Person.__init__(self,name,'mngr',pay)

    def giveraise(self,procent,bonus = 10 ):

        self.pay += (self.pay + procent)//100 
        self.pay += (self.pay + bonus)//100
      

if __name__ == '__main__':

    yana = Manage('Yana kddk',300)
    yana.giveraise(10)

    print(yana.pay)

