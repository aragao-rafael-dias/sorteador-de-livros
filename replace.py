with open('lista.json', 'r') as f:
    json_data = f.read()

json_data = json_data.replace(';', ',') 


with open('lista.json', 'w') as f:
    f.write(json_data)



