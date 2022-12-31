while True:
    while True:
        sexo = str(input('''Digite o sexo: ''')).strip().upper()[0]
        if sexo != 'M' and sexo != 'F':
            print('Valor invalido, tente de novo')
        else:
            break
    while True:
        try:
            altura = float(input('Digite a altura: '))
        except (ValueError, TypeError):
                print('Valor invalido, tente de novo')
        else:
            break
    if sexo == 'M':
        sexo = 'masculino'
        peso_ideal = (72.2 * altura) - 58
        break

    else:
        sexo = 'feminino'
        peso_ideal = (62.1 * altura) - 44.7
        break

print(f'O peso ideal de uma pessoa do sexo {sexo} com a altura de {altura} é {peso_ideal:.2f}')