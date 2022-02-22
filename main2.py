def printDict(dictionary):
    keys=[]
    values=[]
    for key, value in dictionary.items():
        keys.append(key)
        values.append(value)
    print(keys)
    print(values)

dict1 = {
    "name":"Hardhik",
    "class":"10th",
    "section":"B"
}

printDict(dict1)