hello = "bonjour", "Benjamin"
print(hello[::-1])

#ou 

hello = ["bonjour", "Benjamin", "comment", "vas","-","tu"]
retour = hello[0]
hello[0] = hello[-1]
hello[-1]= retour
print (hello)
