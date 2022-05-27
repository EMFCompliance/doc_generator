import json

data = {}
array = {}
new_val  = {"HS500": "str"}

with open('/home/v/doc_generator/registry1.json', "r+") as f:
    data = json.load(f)
    for x in data['registry']:
         array.update(x) 
         print(array)
         print(array['documents'])
         data['registry'][1]
         data['registry'][0]['documents'].append(new_val)
         print(data)
         f.seek(0)
         json.dump(data,f, indent =4)



