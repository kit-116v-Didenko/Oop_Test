class Start:
    def method(self):
        print(f'{self.__class__.__name__} Working')

    def nonMethod(self):
        self.rise()
    def rise(self):
        assert False,'Not method'

class First(Start):
    pass

class Second(Start):
    def method(self):
        print('I go working Second')
        Start().method()
        print('I go close working') 

class Third(Start):
    def rise(self):
        print('go, go ,go !!')

    

if __name__ == '__main__':
    #for obj in First,Second,Third:
      #  obj().method()


    b = Third()
    b.nonMethod()
    c = First()
    #c.nonMethod()
    import os
    print(os.path.dirname(os.path.abspath(__file__)))
    