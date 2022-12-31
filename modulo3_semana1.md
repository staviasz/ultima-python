# Cenário1: 
# Você trabalha em uma equipe que deseja utilizar o git em seus projetos, vocês já possuem um repositório criado e precisam configurar o repositório (configurações do projeto, bibliotecas, documentação e etc) para começarem a trabalhar.

## git init
    
    - Inicializa o git na pasta onde ficarão os arquivos

## git status
    
    - Verifica os arquivos que foram reconecidos pelo git (adicões ou modificações)

## git add "nome do arquivo" 

    - Adiciona o arquivo ao stage

## git commit -m "descrição"

    - Confirma o versionamento, com uma "descrição resumida" do que foi adicionado ou modificado

## git clone + ssh key

    - Cria um link entre o repositório da local e o repositório remoto (ex: Github)

## git push

    - Envia os arquivos do repositório local para o repositório remoto

## Configurando permissoes no repositório remoto 

    - Para criar equipes adiciona-se os membros na mesma 
      dando-lhes determinadas permissoes (atravez da opção "manager access"):
        - Leitura 
        - Triagem
        - Escrita
    - Terminado esse processo todos os membros com pemissão de escrita podem 
      clonar os arquivos do repositorio remoto e trabalhar em sua maquina
      (atravez do comando "git pull")

# Cenário2: 
# Você e seus colegas de equipe estão trabalhando em cima do mesmo conjunto de arquivos. Você precisa de uma atualização no seu repositório que algum de seus colegas acabou de finalizar e fez o merge para a branch main.

## git pull 
    
    - O git buscará as diferenças entre os arquivos presentes no localhost
      e no repositório remoto encontrando-as ele trará as modificações para
      o meu espaço local

# Cenário3:
# Após um dia de trabalho você finalizou a codificação de uma tarefa e precisa unir o seu código com a main branch.

## git merge
    
    - Após terminar um código verificar possíveis falhas
      une a branch em que o código está armazenado a branch main

# Cenário4:
# A sua equipe estava tendo muitos problemas com o versionamento do código e decidiu pensar em uma estratégia para poder organizar melhor o código através de “versões candidatas” para produção. Para isso foi decidido criar uma nova branch com o padrão de nome “rc_v150” (abreviação para “Release Candidate Version 1.5.0”) para a primeira versão a ser usada nesta nova estratégia.

    - Analisa todos os pull requests depois faz merge com a main

## git rebase
   
    - Revisa faseadamente todos os conflitos existentes 

## git tag "nome_da_tag" 
   
    - Após ter sido resolvido todos os conflitos "rotula" a main 
      com uma tag

# Cenário5:
# Após analisar um problema no código, você fez uma proposta do que precisa ser alterado para que o bug seja resolvido. Para realizar a correção, será necessário criar uma branch, codificar a correção e enviar o código para que outras pessoas do time possam avaliá-lo.

## git checkout -b "nome_branch"

    - Esse comando cria e muda de branch em sequência
      para que possa executar mudanças no código sem 
      afetar a main

## git push -u origin main
    
    - Dessa forma criamos um pull request para que o 
      código desenvolvido seja avaliado por revisores
      e então seja efetuado o merge 