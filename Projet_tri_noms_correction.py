with open("/home/vagrant/prenoms.txt", "r") as f:
    lines = f.read().splitlines()

prenoms = []
for line in lines:
    prenoms.extend(line.split())
print(prenoms)
print("######################")

prenoms_final = [prenom.strip(",. ") for prenom in prenoms]
print(prenoms_final)


with open("/home/vagrant/prenoms_final_corigé.txt", "w") as f:
   f.write("\n".join(sorted(prenoms_final)))