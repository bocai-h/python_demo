import pickle
dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)

db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'

dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()