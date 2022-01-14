from constants import BONJOUR



def get_weekly_progress(user):
    nombre_videos = 12
    return nombre_videos



user = input("Entrer votre nom d'utilisateur : ")
progression = get_weekly_progress(user)

message_de_bienvenue = BONJOUR.format(prenom=user, nombre_videos=progression)

print(message_de_bienvenue)

    