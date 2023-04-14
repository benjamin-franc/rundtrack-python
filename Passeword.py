import re
import json
from hashlib import sha256
import os

while True:
    password = input("Veuillez choisir un mot de passe : ")

    if len(password) < 8:
        print("Le mot de passe doit contenir au moins 8 caractères.")
    elif not re.search("[a-z]", password):
        print("Le mot de passe doit contenir au moins une lettre minuscule.")
    elif not re.search("[A-Z]", password):
        print("Le mot de passe doit contenir au moins une lettre majuscule.")
    elif not re.search("[0-9]", password):
        print("Le mot de passe doit contenir au moins un chiffre.")
    elif not re.search("[!@#$%^&*]", password):
        print("Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")
    else:
        chemin = os.path.expanduser("/Users/benjaminfranc/Desktop/Python/Password/mdp_list.json")
        if not os.path.exists(os.path.dirname(chemin)):
            os.makedirs(os.path.dirname(chemin))

        with open(chemin, "r") as f:
            for line in f:
                data = json.loads(line)
                existing_password = data["password"]
                if sha256(password.encode()).hexdigest() == existing_password:
                    print("Le mot de passe est déjà enregistré.")
                    break
            else:
                with open(chemin, "a") as f:
                    crypt_password = sha256(password.encode()).hexdigest()
                    json.dump({"password": crypt_password}, f)
                    f.write('\n')
                    print("Le mot de passe est valide.")
                    print(crypt_password)
                    break