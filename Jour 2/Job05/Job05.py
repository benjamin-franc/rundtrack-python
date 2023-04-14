def calcule (num1,operator, num2):
    if operator =="+":
        return num1 + num2
    elif operator == "%":
        return num1 % num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    else:
        print("erreur")

print(calcule (20,"+",30))
print(calcule (20,"%",30))
print(calcule (20,"-",30))
print(calcule (20,"*",30))



