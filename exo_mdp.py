

mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_cour = "votre mot de passe est trop court"


if len(mdp) < 1:
    print(mdp_trop_cour.upper())

elif mdp.isdigit():
    print("Votre mot de passe ne contient que des nombres")

elif len(mdp) < 8:
    print(mdp_trop_cour.capitalize())

else:
    print("Incription Terminé")






