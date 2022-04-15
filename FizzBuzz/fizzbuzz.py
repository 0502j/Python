def fizzbuzz(numero):
    if numero % 15 == 0:
        return 'fizzbuzz'
    elif numero % 5 == 0:
        return 'buzz'
    elif numero % 3 == 0:
        return 'fizz'

    return numero


for number in list(range(1, 101)):
    print(fizzbuzz(number))
