def marché(type, saison):
    if type == "fruits" and saison == "hiver":
         print("Orange, mandarine et kiwi")
    elif type == "fruits" and saison == "été":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
         print("Carotte, topinambour, endive")
    elif type == "legume" and saison == "été":
        print("Artchaud, aubergine, navet")
    else:
        print("manquant")

marché("fruits", "hiver")
marché("fruit", "été")
marché("legume", "hiver")
marché("legume", "été")
