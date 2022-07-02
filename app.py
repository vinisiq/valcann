import os
import time
import shutil
import logging
from datetime import timedelta
from datetime import datetime
from shutil import copyfile



def listar_arquivos(diretorio):

    log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'

    logging.basicConfig(filename='backupsFrom.log',
                    # w -> sobrescreve o arquivo a cada log
                    # a -> não sobrescreve o arquivo
                    filemode='w',
                    level=logging.DEBUG,
                    format=log_format)

    logger = logging.getLogger('root')
    os.chdir(diretorio)

    print('\n|----------------------------------------------------------|')
    print('|              INICIANDO LISTAGEM DE ARQUIVOS              |')
    print('|----------------------------------------------------------|\n')

    for arquivos in os.listdir():
            nome = os.path.basename(arquivos)
            tamanho = os.path.getsize(arquivos)
            data_criacao = time.ctime(os.path.getctime(arquivos))
            data_alteracao = time.ctime(os.path.getmtime(arquivos))
            logger.info(f'{nome}; Tamanho: {tamanho}KB; Data de Criacao: {data_criacao} ; Ultima alteracao: {data_alteracao} \n')

            print("Nome: {}".format(nome))
            print("Tamanho: {} KB".format(tamanho))
            print("Data de criação: {}".format(data_criacao))
            print("Data de última alteração: {}\n".format(data_alteracao))

os.chdir('\\home\\valcann\\')

def remover_arquivos(diretorio):
    
    print('\n|----------------------------------------------------------|')
    print('|              INICIANDO REMOÇÃO DE ARQUIVOS               |')
    print('|----------------------------------------------------------|\n')

    for arquivos in os.listdir():
         nome = os.path.basename(arquivos)
         data_criacao = os.path.getctime(arquivos)
         data_criacao = datetime.fromtimestamp(data_criacao)
         ultima_data = data_criacao + timedelta(days=+3) 

        
         if ultima_data < datetime.today():
             print(f'O arquivo {arquivos} foi excluído, pois tem mais de 3 dias desde a sua criação.\n')
             os.remove(arquivos)
         else:
             print(f'Este arquivo > {arquivos} < ainda não ultrapassou 3 dias desde de criação.\n')
    
    os.chdir(diretorio)

os.chdir('\\home\\valcann\\')

def copiar_arquivos(diretorio_padrao):
    
    diretorio_padrao = os.getcwd()
    
    log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'

    logging.basicConfig(filename='backupsTo.log',
                    # w -> sobrescreve o arquivo a cada log
                    # a -> não sobrescreve o arquivo
                    filemode='w',
                    level=logging.INFO,
                    format=log_format)

    logger = logging.getLogger('root')


    print('\n|----------------------------------------------------------|')
    print('|        INICIANDO CÓPIA DE ARQUIVOS PARA "backupsTo"      |')
    print('|----------------------------------------------------------|\n')
    for arquivos in os.listdir(os.chdir('backupsFrom')):
        nome = os.path.basename(arquivos)
        tamanho = os.path.getsize(arquivos)
        data_criacao = os.path.getctime(arquivos)
        data_alteracao = time.ctime(os.path.getmtime(arquivos))
        data_criacao = datetime.fromtimestamp(data_criacao)
        ultima_data = data_criacao + timedelta(days=+3)
        
        if ultima_data >= datetime.today():
            shutil.copyfile(f'{diretorio_padrao}\\backupsFrom\\{arquivos}', f'{diretorio_padrao}\\backupsTo\\{arquivos}')
            print(f'{arquivos} foi enviado para pasta backupsTo com sucesso\n')
            os.chdir(diretorio_padrao)
            logger.info(f'{nome}; Tamanho: {tamanho}KB; Data de Criacao: {data_criacao} ; Ultima alteracao: {data_alteracao} \n')         
            os.chdir('backupsFrom')    

        else:
             print(f'O arquivo {arquivos} tem mais de 3 dias e foi/será excluído.\n')
             os.chdir(diretorio_padrao)
             logger.info(f'{nome}; Tamanho: {tamanho}KB; Data de Criacao: {data_criacao} ; Ultima alteracao: {data_alteracao} \n')
             os.chdir('backupsFrom') 

# Comandos para início:

listar_arquivos('backupsFrom')

remover_arquivos('backupsFrom')

copiar_arquivos('valcann')




        
        
      

