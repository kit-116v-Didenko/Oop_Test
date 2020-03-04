from deportament import Deportament
from manage import Manage
from person import Person




bob = Person('Bob Smit','dev',3000)
lot = Person('Lot Smit','dev',3000)
gut = Manage('Gut Smit',300)

develop = Deportament(bob,lot,gut)

import shelve

db = shelve.open('Person_Develop')

for obj in bob,lot,gut:
    db[obj.name] = obj

db.close()



if __name__ == "__main__":
    db = shelve.open('Person_Develop')

    print(db['Bob Smit'])
    def vglub(element,count = 3):
        
        print('.'*count,element)
        count +=3
        for key in element.__bases__:
            vglub(key,count)
    def instance(clas):
        vglub(clas.__class__)

    instance(db['Bob Smit'])