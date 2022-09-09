bordas = '\033[037m-=-\033[m' * 12
print(bordas)
print('{:^35}'.format('CONVERSOR DE MEDIDAS'))
print(bordas)
print()

m = ''

while type(m) != float:
    try:
        m = float(input('Digite o valor em metros: '))
    except:
        print('Por favor digite um valor válido!')


print(bordas)
print('km -> Para converter para quilômetro')
print('hm -> Para converter para hectômetro')
print('dam -> Para converter para decâmetro')
print('dm -> Para converter para milímetro')
print('cm -> Para converter para centímetro')
print('mm -> Para converter para decímetro')
print(bordas)

while True:
    convert = input('Digite a opção desejada: ').strip().lower()
    match convert:
        case 'km':
            print(f'\nO valor em metros corresponde a {m/1000}km')
            break
        case 'hm':
            print(f'\nO valor em metros corresponde a {m/100}hm')
            break
        case 'dam':
            print(f'\nO valor em metros corresponde a {m/10}dam')
            break
        case 'dm':
            print(f'\nO valor em metros corresponde a {m*10}dm')
            break
        case 'cm':
            print(f'\nO valor em metros corresponde a {m*100}dm')
            break
        case 'mm':
            print(f'\nO valor em metros corresponde a {m*1000}dm')
            break
        case _:
            print('Por favor digite uma opção válida!')