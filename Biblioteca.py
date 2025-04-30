def imprimeNome(nome):
    print(f"Nome:{nome}")

def piramide(num):
    for x in range(1, num + 1):
        for y in range(0, x):
            print(x, end=" ")
        print()
