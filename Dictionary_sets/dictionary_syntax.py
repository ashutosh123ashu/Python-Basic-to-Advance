
# Dictionary contains in the key value pair
#   Properties
#   1. Dictionary is mutable 
#   2. IS un ordered
#   3. can be indexed with key

myDict = {
    "Fast": "In a Quick Manner",
    "Harry": "A Coder",
    "Marks": [1, 2, 5],
    "anotherDict": {'harry': 'Player'}
}

myDict['Marks'][0] = 34

print(myDict[0])  # Dictionary items can not be accessed with index numbers (Dictionary in python is unorderd)
# print(myDict)
# print(myDict["Harry"])
print(myDict["Marks"])
# print(myDict['anotherDict']['harry'])
