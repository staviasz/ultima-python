

mensagem = str(input('Digite a mensagem: '))
mensagem_criptografada = []

for char in mensagem:
    for i in str(ord(char)):
        mensagem_criptografada.append(i)
    mensagem_criptografada.append('-1')
print('a mensagem cripto é: ',mensagem_criptografada)

descript_mensagem = ''
mensagem_descriptografada = ''
for i in mensagem_criptografada:
    if i != '-1':
        descript_mensagem = descript_mensagem + i
    else:
        mensagem_descriptografada = mensagem_descriptografada + chr(int(descript_mensagem))
        descript_mensagem = ''
print('a mensagem descripto é: ',mensagem_descriptografada)