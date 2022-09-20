def thousands_with_commas(i): 
    i = str(i)
    resp = ''
    aux = 0
    cont = 0
    while aux < len(i):
        if cont == 3:
            resp = ',' + resp
            cont = 0
        resp = i[-(aux+1)] + resp
        aux += 1
        cont += 1
    i = resp
    return str(i)

if __name__ == '__main__':
    assert thousands_with_commas(1234) == '1,234'
    assert thousands_with_commas(123456789) == '123,456,789' 
    assert thousands_with_commas(12) == '12'