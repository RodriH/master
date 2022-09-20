t=1
lista_num = [i.rstrip() for i in open('/Users/rodrigohofer/downloads/c-input.in')] 
lista_num.pop(0)
for num in lista_num:
    lista = []
    i = int(num)
    n = 1
    while len(lista) < 10 and n <= 200 and t<=100 and t >= 1:
        new_number = i * n
        aux = list(str(new_number)) 
        last_number = new_number
        for c in aux:
            if c not in lista:
                lista.append(c)
        n += 1

    if len(lista) == 10:
        print(f'Case #{t}: {last_number}')  
    else:
        print(f'Case #{t}: INSOMNIA')  
    t += 1

