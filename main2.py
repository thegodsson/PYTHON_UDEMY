from constants import bonjour



def get_weekly_progress(user):
    nombre_videos = 12
    return nombre_videos


if __name__ == "__main__":
    user = input("Entrer votre nom d'utilisateur : ")    
    progression = get_weekly_progress(user)    
    message_de_bienvenue = bonjour(prenom=user, nombre_videos=progression)
    