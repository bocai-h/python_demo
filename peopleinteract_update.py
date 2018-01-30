import pdb
import shelve
from person import Person
fieldnames = ('name', 'age', 'pay', 'job')

db = shelve.open('class-shelve')
while True:
    key = input("\nKey=>? ")
    if not key: break
    if key in db:
        record = db[key]
        print('find a key')
    else:
        record = Person(name='?', age='?')
        print('No such key You init a new record')
       

    for field in fieldnames:
        currval = getattr(record, field)
        print('currval=',currval)
        newtext = input('\t[%s]=%s\n\t\tnew?=>' % (field, currval))
        # pdb.set_trace()
        if newtext:
            setattr(record, field, eval(newtext))
    
    db[key] = record

db.close