'''

list = {"Pratyaksh", "Jay", "Akshar", "Utkarsh"}
listToStr = str(list)
filename = 'Listdata.txt'

with open(filename , "w") as file:
    file.write(listToStr)

with open(filename , "r") as file:
    readFile = file.read()
    readFile = readFile[1:len(readFile)-1].replace(" ","").split(",")
    print(f"read data is {readFile}\n its type is{type(readFile)}")

'''

import pickle

data = {"name": "Pratyaksh" , "age": 22 , "occupation": "Student"}

with open("data.pickle" , "wb") as file:
    pickle.dump(data , file)
print("Data has been serialized and saved to data.pickle")

with open("data.pickle" , "rb") as file:
    loaded_data = pickle.load(file)
print("Deserialized data:", loaded_data)
