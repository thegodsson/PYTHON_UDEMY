import json

with open("/home/vagrant/data.json", "r") as f:
    donnees = json.load(f)
    print(donnees)
    print(type(donnees))

donnees.append(4)

with open("/home/vagrant/data.json", "w") as f:
    json.dump(donnees, f, indent=4)


    