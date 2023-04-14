L= int(input("veuillez saisir le nombre de lignes:"))
C= int(input("Veuillez saisir le nombre de colonnes:"))
for i in range(1, L+1):
    for J in range(1, C+1):
        if J ==1 or J==C:
            print ("| ", end="")
        elif i==1 or i==L:
            print ("- ", end="")
        else:
            print("  ",end="")
    print()

