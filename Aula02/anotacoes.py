"""
________________________________ // ________________________________
Desafio1: capturar os nome que começam com a letra M do arquivo registros.bin a partir do pratica_lista_tupla.py


for r in registros:
    if r[0].startswith("M"):
        print(r[0])

________________________________ // ________________________________
Desafio2: pegar as duplas que tem o endereço de SP partir do pratica_lista_tupla.py

for r in registros:
    if r[1].endswith("SP"):
        print(r[1])
________________________________ // ________________________________
Alternativa para o desafio 2

estadoSP = []
for registro in registros:
    if registro[1].endswith('SP'):
        estadoSP.append(registro)
print(estadoSP)
________________________________ // ________________________________
Desafio 3: Remover itens duplicados da lista de compras

lista_compra = []
lista_compra.append('Arroz')
lista_compra.append('Feijão')
lista_compra.append('Macarrão')
lista_compra.append('Alface')
lista_compra.append('Coca-cola')
lista_compra.append('Arroz')

reorganizado = []
for produto in lista_compra:
    if produto not in reorganizado:
        reorganizado.append(produto)


________________________________ // ________________________________
Anotações gerais - lista de compras

lista_compra2 = ['arroz', 'abóbora']
lista_compra2.append("maçã")
conjunto = set(lista_compra)
conjunto2 = set(lista_compra2)


completo = conjunto.union(conjunto2)

tupla_gerada = tuple(completo)

________________________________ // ________________________________
Anotações gerais - números

numeros = set(range(1,10))
numeros2 = set(range(5,15))


numeros2.intersection(numeros)
numeros.union(numeros2)
numeros.difference(numeros2)
numeros.symmetric_difference(numeros2)

numeros3=set(range(5,7))
numeros.union(numeros2.intersection(numeros3))

________________________________ // ________________________________
Dicionários

a = dict(one=1, two=2, three=3)
a['one']

lista_telefonica = dict()
lista_telefonica['Jamile'] = ('Jamile', '00-0-00099999')
lista_telefonica['Fatec'] = ('Fatec', '00-0-31092999')


lista_telefonica.keys()

lista_telefonica.values()

lista_telefonica['Jamile']

try:
    lista_telefonica['jamile']
except KeyError:
    print('Não encontrado!')

lista_telefonica.get('jamile', 'Não encontrado') #não encontrado
lista_telefonica.get('Jamile', 'Não encontrado') #retorna a tupla certa


"""
