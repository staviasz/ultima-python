peso = float(input('Qual o peso do paciente: '))
altura = float(input('Qual a altura do paciente: '))

imc = peso/altura**2

if imc < 18.5:
    classe_imc = 'abaixo do peso'
elif 18.5 <= imc < 25:
    classe_imc = 'peso normal'
elif 25 <= imc < 30:
    classe_imc = 'acima do peso'
else:
    classe_imc = 'obeso'

print(f'O IMC é {imc:.1f}, este paciente se encontra {classe_imc}')