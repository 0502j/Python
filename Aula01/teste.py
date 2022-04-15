from ast import If

"""""
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
# idade = idade*2

print("Oi " + nome + ", sua idade é " + str(idade))

if idade > 18:
  print("/")

else:
    print("//")

for letra in nome:
    print(letra)

for numero in range(10):
     print(numero+1)

print(nome[2:5])


# lista / estrutura de dados
lista = ['Maça', 'Tomate', 'Pizza', 10, 13.4]

for produto in lista:
    print(produto)

lista.append('coca-cola')
lista.insert(1, 'alface')

for produto in lista:
    print(produto)

print(id(lista))
"""

registro = ("Jamile", "Sousa", "estudante","Fatec Araras", "Fatec")

for elemento in registro:
    print(elemento.startswith("F"))