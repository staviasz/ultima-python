# 1° Existem várias situações no fluxo de trabalho com Git onde podemos encontrar conflitos durante o merge de branchs. Na grande maioria dos casos, poucas alterações no código podem resolver estes conflitos, sendo então necessário atualizar a branch em questão. Qual a sequência de passos deve ser seguida após um comando git merge falhar devido a conflitos?

### git revert
    - retorna a um commit anterior (antes do conflito) 
### git pull 
    - Atualiza a branch 
### git push
    - para atualiza o repositorio com as atualizações feitas sem gerar conflitos

# 2° Luizinho estava trabalhando em uma melhoria em seu código utilizando a branch feature/ABC123  quando colegas de trabalho lhe informaram de um bug em produção que precisa ser corrigido o quanto antes. O bug em questão estava no arquivo hello.py na branch main do repositório. Qual sequência de comandos git, Luizinho deve executar para corrigir o bug e voltar ao seu trabalho? Lembre-se que a empresa em que Luizinho trabalha segue à risca o GitFlow.

### git checkout branch main
    - retorna para a main
### git checkout -b hotfix
    - cria a branch hotfix para a resolução do bug
### git merge 
    - junta a hotfix na branch main e na branch develope 
### git checkout branch feature/ABC123
    - retorna para o trabalho que estava sendo desenvolvido anteriormente

# 3° No fluxo de trabalho de software a principal forma de sincronização de códigos é por meio de ferramentas de versionamento. A mais popular delas é amplamente difundida e é conhecida como git. Tendo em vista os temas abordados em aula, descreva a funcionalidade e exemplifique os comando git pull e git push 

### git pull 
    - Esse comando traz os arquivos do repositorio remoto cujo não estão na maquina local,
    servindo para manter os arquyivos em que estamos trabalhando sempre atualizado com os ultimos commit

### git push
    - Esse comando leva as atuaslizações que fazemos no codigo em nossa maquina local e envia para o repositorio remoto

# 4° Realize uma pesquisa sobre as diversas plataformas de versionamento com git, escolha duas e realize um comparativo com o GitHub avaliando as semelhanças, diferenças, vantagens e desvantagens para o desenvolvimento de software.

[Comparação entre github, gitlab e bitbucket](https://itforum.com.br/noticias/github-vs-bitbucket-vs-gitlab-uma-batalha-epica-pelo-mindshare-desenvolvedor/)

# 5° Criei um programa que calcule o peso ideal de uma pessoa. Para isso utilize as fórmulas da tabela. Sua aplicação deve identificar se a pessoa é Homem ou Mulher e então fazer o cálculo apropriado. Deve ser impresso se a pessoa é homem ou mulher, juntamente com o peso ideal calculado.
    - Para Homens: (72.7 * altura) – 58
    - Para Mulheres: (62.1 * altura) – 44.7 
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



# 6° Um nutricionista está precisando de uma ajuda para calcular o IMC de seus pacientes. Para calcular o IMC ele passou a seguinte fórmula: IMC = peso / ( altura )². Crie um programa que faça o cálculo do IMC de uma pessoa (ele deve ser impresso na tela) e classifique o IMC dessa pessoa de acordo com a tabela (também deverá ser impresso):

        Valor do IMC                Classificação

        Abaixo de 18,5              Pessoa abaixo do peso
        Entre 18,5 e 25             Pessoa com peso normal
        Entre 25 e 30               Pessoa acima do peso
        Acima de 30                 Pessoa obesa

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

# 7° Uma loja de móveis está com dificuldades de calcular algumas condições de pagamento de seus móveis. Eles possuem algumas regras e o seu trabalho é implementar uma aplicação que faça os cálculos de acordo com as regras, O programa deve ter uma variável com o valor de etiqueta do produto, uma variável com forma de pagamento e uma com o preço final após a aplicação de uma das regras.
        Regras
        À vista em dinheiro, recebe 15% de desconto
        À vista no cartão de crédito, recebe 10% de desconto
        Em duas vezes, preço normal de etiqueta sem juros
        Mais de duas vezes, preço normal de etiqueta mais juros de 10%

    valor_produto = float(input('Digite  o valor do produto: '))
    forma_pagamento = str(input('O pagamento será em dinheiro ou cartão: '))
    
    if forma_pagamento == 'dinheiro':
        valor_final = valor_produto - valor_produto * 0.15
        print(f'Pagando á vista em dinheiro há um desconto de 15% resultando no valor final de: {valor_final}')
    else:
        parcela = int(input('Quantas parcelas: '))
        if parcela == 1:
            valor_final = valor_produto - valor_produto * 0.10
            print(f'Pagando á vista no catão há um desconto de 10% resultando no valor final de: {valor_final}')
        elif parcela == 2:
            valor_final = valor_produto
            print(f'Pagando em 2x no cartão o valor final é: R${valor_final:.2f}, com a parcela de: R${valor_final/parcela:.2f}')
        else:
            valor_final = valor_produto + valor_produto * 0.10
            print(f'Pagando acima de 2x catão há um juros de 10% resultando no valor final de: R${valor_final:.2f}, com a parcela de: R${valor_final/parcela:.2f}')

# 8° Alguns alunos de uma universidade criaram uma “criptografia” para se comunicarem entre eles durante o tempo que estão longe da universidade. Essa criptografia é baseada em códigos que, quando convertidos, formam as letras de uma palavra. Esses números são informados em uma lista de caracteres e são separados pela string ‘-1’ conforme o exemplo: ['7','9', '-1', '7','3','-1'] Nessa sequência teríamos o número 79 representando um caractere e o número 73 representando outro caractere da mensagem. Para saber a letra será necessário percorrer essa lista e ir concatenando os números antes de identificar um separador (‘-1’) para então identificar qual letra o código numérico representa.

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

### resoluçõe dos exemplos da questão acima
    - a mensagem cripto é:  ['8', '5', '-1', '7', '6', '-1', '8', '4', '-1', '7', '3', '-1', '7', '7', '-1', '6', '5', '-1']
    a mensagem descripto é:  ULTIMA

    - a mensagem cripto é:  ['7', '9', '-1', '7', '3', '-1']
    a mensagem descripto é:  OI


# 9° Extra: A Cifra de César foi uma das primeiras técnicas de criptografia criadas pela humanidade. Essa técnica consiste em aplicar um deslocamento de caracteres em uma mensagem, por exemplo, se aplicarmos o deslocamento de 3 caracteres, A palavra “OI” aplicando o deslocamento de 3 caracteres em cada um dos caracteres ficaria como “RL”. Sua tarefa é criar uma aplicação que possa descriptografar a seguinte frase (não aplicamos deslocamento para o caractere espaço): “HVWRX HPSROJDGR FRP R FXUVR GH SBWKRQ”. Considere que o deslocamento de caracteres usado foi 3 caracteres.
        A letra ‘A’ fica como letra ‘D’;
        A letra “I” fica como letra “L”;
        A letra “Z” fica como letra “C”
        E assim por diante.

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

### resolução do exemplo 
    -a mensagem cripto é:  HVWRX HPSROJDGR FRP R FXUVR GH SBWKRQ
    a mensagem descripto é:  ESTOU EMPOLGADO COM O CURSO DE P?THON