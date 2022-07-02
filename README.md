### Autor: Vinicius Siqueira da Silva
### E-mail: viniciussiqueira.dev@outlook.com


# Problema 1 | Automação de Ambientes Operacionais

Um dos principais desafios para um bom gerenciamento de infraestrutura, é implementar
automação para permitir produtividade aos times de administração de tecnologia, bem como,
minimizar ações humanas nos ambientes dos clientes.

O cliente “Acme Co.” possui um servidor centralizado de backup, o qual recebe arquivos de todos
os demais servidores, move os dados para um volume temporário, para que deste volume os dados
sejam copiados por uma ferramenta de backup externa.

De forma a minimizar o nível de intervenção neste ambiente, você foi convocado a escrever um
script (em Shell Script, Python ou qualquer outra tecnologia que preferir), para automatizar as
seguintes ações:


--    Listar todos arquivos (nome, tamanho, data de criação, data da última modificação) localizados no
        caminho /home/valcann/backupsFrom; 

--    Salvar o resultado no arquivo backupsFrom.log em /home/valcann/;
        
--    Remover todos os arquivos com data de criação superior a 3 (três) dias; 

--    Copiar todos os arquivos os arquivos com data de criação menor ou igual a 3 (três) dias em
        home/valcann/backupsTo;

--    Salvar o resultado no arquivo backupsTo.log em /home/valcann/.

## Considerações sobre a elaboração da resolução da problemática:

   O ínicio da elaboração da solução foi manual para uma melhor abstração do que deveria ser feito, era
necessário entender da melhor forma possível o que era solicitado. Os rascunhos podem ser vistos na 
imagem a seguir.

   ![rascunhos-valcann1](https://user-images.githubusercontent.com/97056856/177014926-ded7af01-5d43-4670-93bc-4912970331b5.jpeg)
   
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

A função listar_arquivos utiliza como parâmetro a indicação da pasta onde será listado os arquivos, neste caso, 
a pasta 'backupsFrom'. No ínicio da função podemos ver a chamada do objeto "logger.add('backupsFrom.log')",que 
cria ou atualiza o log (não duplica o log no caso da função ser chamada mais de uma vez). É necessário que o código 
consiga chegar a pasta backupsFrom para poder fazer a listagem dos arquivos que ali estão, neste caso, foi utilizada
a chamada do objeto os.chdir(diretorio). 

Ademais, a primeira estrutura a ser utilizada foi o "for", que faz um loop dentro de "backupsFrom" por meio do método
os.listdir() trazendo "arquivo" como resultado para os dados dos arquivos da referida pasta. Para imprimir no terminal
o resultado da listagem, foi utilizado o método logger.info('mensagem') para retornar o resultado tanto no terminal quanto
grava-lo no arquivo backupsFrom.log.

Por fim, o método os.chdir() para retornar ao diretório inicial.

#### Função remover_arquivos():

Similiar ao que acontece na função de listar, aqui iniciamos a função adicionando um arquivo de log para identificar quais 
arquivos foram removidos. Apesar disto não estar na proposta da problemática, achei interessante incluir, uma vez que através
do logging do loguro conseguimos tanto imprimir no terminal o resultado quanto no arquivo removedFiles.log. Logo após, iniciamos
um loop que retorna "arquivos" como resultado da busca em uma lista de arquivos da pasta, mesma ideia da outra função já apresen-
tada. 

Além disso, dentro do loop temos variaveis que convertem a data de segundos para dias, horas e meses. A variável data_criacao 
retorna a data em que o arquivo foi criado, já ultima_data retorna a data de criação do arquivo mais 3 dias. O condicional que é 
realizado logo em seguinda utiliza a lógica dessas variáveis para remover os arquivos que têm data superior a 3 dias de criação.

Por conseguinte, o arquivo é removido e seu resultado é imprimido no terminal e também no arquivo removedFiles.log.

#### Função copiar_arquivos:

No início da função existe a possibilidade da criação da pasta backupsTo se a pasta não existir ainda. Fora isso, esta função é similiar a anterior até o momento da sua condicional dentro do loop, que nesta função é para arquivos que têm criação inferior ou igual a 3 dias. 

A cópia do arquivo se dá por meio do módulo shutil, utilizando o objeto copyfile, que copia arquivos e 
manda para o caminho indicado, neste caso, backupsTo. O resultado dos arquivos que foram enviado vai para backupsTo.log. 

#### Local funcional:

Para um melhor aproveitamento da utilização do programa, recomendo que faça o git clone em uma máquina Windows e preferenciamente neste caminho: C:\home\\valcann . É necessário a instalação das bibliotecas contidas no requiriments.txt. 

## Imagens do funcionamento do automatizador de ambientes:

###                                                 Função listar_arquivos
![image](https://user-images.githubusercontent.com/97056856/177018240-905532b2-729f-42ca-a1a2-19c767d26296.png)


###                                                 Função remover_arquivos
![image](https://user-images.githubusercontent.com/97056856/177018247-c9198b43-9793-4e5f-9581-2a585036250c.png)


###                                                 Função copiar_arquivos
![image](https://user-images.githubusercontent.com/97056856/177018262-7e812871-fae6-4517-8249-1c86493175c0.png)


###                                    Estrutura das pastas logo após execução do app.py
![image](https://user-images.githubusercontent.com/97056856/177018321-e6911fb7-99a4-482e-8f14-0ad4efeac134.png)


OBS: A estrutura padrão das pastas é a que está no Finish code commit, no GitHub.


###                                                     backupsFrom.log
![image](https://user-images.githubusercontent.com/97056856/177018460-a3f7c3dd-c3b4-4623-8068-f42a9e5600b6.png)


###                                                     removedFiles.log
![image](https://user-images.githubusercontent.com/97056856/177018412-8d909b32-a5cf-4742-9e58-53729b4b8536.png)


###                                                      backupsTo.log
![image](https://user-images.githubusercontent.com/97056856/177018452-730abd4f-6cc7-4a37-918f-a30c3db26c52.png)







