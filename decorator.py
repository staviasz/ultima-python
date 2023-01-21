def decorator_imprimir(func):
    def inner(capital, taxa, tempo):
        resultado = func(capital, taxa, tempo)
        print(f'CAPITAL: {capital}, TAXA: {taxa}, TEMPO: {tempo}\nRESULTADO: {resultado}')
    return inner