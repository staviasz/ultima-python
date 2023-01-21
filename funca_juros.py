from decorator import decorator_imprimir

@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    resultado = capital * (taxa/100) * tempo 
    return resultado

print(juros_simples(1000,5,6))