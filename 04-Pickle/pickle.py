import pickle

data = [{"id" : 101, "name" : "Ram", "age" : 20}]

with open("pickle_1.pickle", 'wb') as file:
    pickle.dump(data, file)
    print("Object Stored...")
