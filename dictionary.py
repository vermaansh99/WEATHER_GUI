import json

data = {'fname':"Sumit",'lname':"Kumar"}
isDone = {'isOpen':"False"}

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)


with open('example.json','w') as confirm:
    json.dump(isDone,confirm)