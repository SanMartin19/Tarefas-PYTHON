num = ant = suc = 0

num = int(input("Digite um número: "))
ant = num - 1 
suc = num + 1

# operações que o print() aceita

print(str("O numero sugerido foi:"),num, str('seu antecessor é: '),ant, str("e seu sucessor é:"),suc)
print('O numero sugerido foi:',str(num), 'seu antecessor é: ',str(ant),'e seu sucessor é:',str(suc))
print('O numero sugerido foi:',num, 'seu antecessor é: ',ant, 'e seu sucessor é:',suc)
print(f'O numero sugerido foi: {num} seu antecessor é:  {ant} e seu sucessor é: {suc}')  
