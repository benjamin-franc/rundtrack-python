def chiffrement_cesar(message, decalage):
    message_chiffre = ""
    for lettre in message:
        if lettre.isupper():
            lettre_chiffree = chr((ord(lettre) - 65 + decalage) % 26 + 65)
        elif lettre.islower():
            lettre_chiffree = chr((ord(lettre) - 97 + decalage) % 26 + 97)
        else:
            lettre_chiffree = lettre
        message_chiffre += lettre_chiffree
    return message_chiffre

message = "j'aime les chiens"
decalage = 3
message_chiffre = chiffrement_cesar(message, decalage)
print(message_chiffre)