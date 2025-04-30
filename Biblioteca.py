def imprimeNome(nome):
    print(f"Nome:{nome}")

def piramide(num):
    for x in range(1, num + 1):
        for y in range(0, x):
            print(x, end=" ")
        print()

def Contavogais(texto):
    cont=0
    for x in range(len(texto)):
        if texto[x]== "a" or texto[x]== "e" or texto[x]== "i" or texto[x]== "o" or texto[x]== "u" or texto[x]== "A" or texto[x]== "E" or texto[x]== "I" or texto[x]== "O" or texto[x]== "U":
            cont=cont+1
        print(cont)