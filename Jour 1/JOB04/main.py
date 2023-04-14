import string
print (string.ascii_lowercase)
print (string.ascii_uppercase)
print (string.ascii_lowercase [::-1])
ma_string="je suis une string"
print(ma_string)

num1=40
num2=2
s=num1+num2
print ("la somme est",s)

num1=3
num2=14
p=num1*num2
print ("le produit est",p)

ch = "e"
print("indices où e est présent : ", [i+1 for i, ltr in enumerate(s) if ltr == ch])