import pickle

with open("obj_1.pickle", 'rb') as file:
    data = pickle.load(file)
    print("Data : ",data)
