import random


baseLength = input("saisir la taille de la base du sapin : ")
baseLength = int(baseLength)

isEven = baseLength%2
print(isEven)

def RandomizeSpaceBetween(rowLength):
    row = ""
    for i in range(0, rowLength):
        char = random.random()
        if char > 0.98:
            char = "0"
        elif 0.98 > char and char > 0.96:
            char = "^"
        else:
            char = " "
        row += char
    return row

if isEven == 0:
    incrEven = 1
    incrOdd = 0

elif isEven == 1:
    incrOdd = 1
    incrEven = 0

for i in range(incrEven, int((baseLength + incrOdd)/2) + incrEven):
    
    spaceBetween = ((i - incrEven)*2) - incrOdd
    spaceBefore = int((baseLength/2) - i)

    if i == int(baseLength/2):
        print(baseLength * "*")
    elif i == incrEven:
        print(spaceBefore * " " + "*" + RandomizeSpaceBetween(spaceBetween) + incrEven * "*")
    else:
        print(spaceBefore * " " + "*" + RandomizeSpaceBetween(spaceBetween) + "*")