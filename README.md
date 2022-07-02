## Autor: Vinicius Siqueira da Silva
## E-mail: viniciussiqueira.dev@outlook.com


# Problema 1 | Automação de Ambientes Operacionais

(OK)    Listar todos arquivos (nome, tamanho, data de criação, data da última modificação) localizados no
        caminho /home/valcann/backupsFrom; 

(OK)    Salvar o resultado no arquivo backupsFrom.log em /home/valcann/;
        
(OK)    Remover todos os arquivos com data de criação superior a 3 (três) dias; 

(OK)    Copiar todos os arquivos os arquivos com data de criação menor ou igual a 3 (três) dias em
        home/valcann/backupsTo;

(OK)    Salvar o resultado no arquivo backupsTo.log em /home/valcann/.

## Considerações sobre a elaboração da resolução da problemática:

    O ínicio da elaboração da solução foi manual para uma melhor abstração do que deveria ser feito, era
necessário entender da melhor forma possível o que era solicitado. Os rascunhos podem ser vistos na imagem a seguir.
                #imagem
    
    Apesar de haver WSL2 Ubuntu 20.04 na minha máquina, optei pela utilização do Windows para execução
da solução, uma vez que tenho no Ubuntu algumas configurações para projetos que estão em andamento. Logo, 
a indicação de divisão da árvore de diretórios(pastas) terá simbologia "\\" no código app.py.

    Primeiramente, escolhi a linguagem Python, na versão 3.10.2, para solução da problemática, pois tenho mais
praticidade com esta. Os módulos(bibliotecas) escolhidos para código foram:

    - os, módulo nativo do python para manipulação de arquivos e pastas;
    - datetime e time, módulos do python para manipulação/conversão de datas e horários;
    - shutil, módulo utilizado para cópia e envio de arquivos na função copia_arquivos;
    - loguru, módulo para criação de logs.

### Explicando as funções:

#### Função listar_arquivos():

    A função listar_arquivos utiliza como parâmetro a indicação da pasta onde será listado os arquivos, neste caso, a pasta 'backupsFrom'. No ínicio da função podemos ver a chamada do objeto "logger.add('backupsFrom.log')", que cria ou atualiza o log (não duplica o log no caso da função ser chamada mais de uma vez). É necessário que o código consiga chegar a pasta backupsFrom para poder fazer a listagem dos arquivos que ali estão, neste caso, foi utilizada a chamada do objeto os.chdir(diretorio). 

    Ademais, a primeira estrutura a ser utilizada foi o "for", que faz um loop dentro de "backupsFrom" por meio do método os.listdir() trazendo "arquivo" como resultado para os dados dos arquivos da referida pasta. Para imprimir no terminal o resultado da listagem, foi utilizado o método logger.info('mensagem') para retornar o resultado tanto no terminal quanto grava-lo no arquivo backupsFrom.log.

#### Função remover_arquivos():

    

