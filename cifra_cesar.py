mensagem = str(input('Digite a mensagem: '))
mensagem_criptografada = ''

for char in mensagem:
    if char != ' ':
        cifra_cesar = chr(ord(char) + 3)
        mensagem_criptografada += cifra_cesar
    else:
        mensagem_criptografada += ' '
print('a mensagem cripto é: ',mensagem_criptografada)

mensagem_descriptografada = ''
for char in mensagem_criptografada:
    if char != ' ':
        cifra_cesar = chr(ord(char) - 3)
        mensagem_descriptografada += cifra_cesar
    else:
        mensagem_descriptografada += ' '
print('a mensagem descripto é: ',mensagem_descriptografada)