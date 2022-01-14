from constants import BONJOUR



def get_weekly_progress():
    nombre_videos = 12
    return nombre_videos


if __name__ == "__main__":
    user = input("Entrer votre nom d'utilisateur : ")
    progression = get_weekly_progress()

    message_de_bienvenue = BONJOUR.format(prenom=user, nombre_videos=progression)

    print(message_de_bienvenue)