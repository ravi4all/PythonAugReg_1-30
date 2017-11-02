import pickle

a = [1,2,3,4,5]

##data = pickle.dumps(a)
##print(data)

##wb - Write Bytes
file = open('obj_1.pickle', 'wb')

data = pickle.dump(a,file)

file.close()
