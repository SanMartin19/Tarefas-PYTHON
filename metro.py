base = altura = metro = 0

base = float(input("Informe o valor da base: "))
altura = float(input("Informe o valor da altura: "))
metro = base * altura

# operações que o print() aceita ...
print(metro, str('metros'))
print(metro, "metros²")
print(f"{metro} metro²")
print(str(metro), "metros²")
