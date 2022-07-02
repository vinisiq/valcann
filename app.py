import os
import time
import shutil
from datetime import timedelta
from datetime import datetime
from loguru import logger


def listar_arquivos(diretorio):

    logger.add('backupsFrom.log')

    os.chdir(diretorio)


    print('\n|----------------------------------------------------------|')
    print('|              INICIANDO LISTAGEM DE ARQUIVOS              |')
    print('|----------------------------------------------------------|\n')

    for arquivos in os.listdir():
            nome = os.path.basename(arquivos)
            tamanho = os.path.getsize(arquivos)
            data_criacao = time.ctime(os.path.getctime(arquivos))
            data_alteracao = time.ctime(os.path.getmtime(arquivos))

            logger.info(f'\n Nome: {nome};\n Tamanho: {tamanho}KB;\n Data de Criacao: {data_criacao};\n Ultima alteracao: {data_alteracao} \n')

    os.chdir('C:\home\\valcann')


def remover_arquivos(diretorio):
    
    logger.add('removedFiles.log')
    print('\n|----------------------------------------------------------|')
    print('|              INICIANDO REMOÇÃO DE ARQUIVOS               |')
    print('|----------------------------------------------------------|\n')

    for arquivos in os.listdir():
        nome = os.path.basename(arquivos)
        data_criacao = os.path.getctime(arquivos)
        data_criacao = datetime.fromtimestamp(data_criacao)
        ultima_data = data_criacao + timedelta(days=+3) 

        if ultima_data < datetime.today():
            logger.info(f'\n O arquivo {nome} foi excluído, pois tem mais de 3 dias desde a sua criação.\n')
            os.remove(arquivos)
        else:
            logger.error(f'\n {nome} ainda não ultrapassou 3 dias desde sua criação.\n')


def copiar_arquivos(diretorio_padrao):
    diretorio_padrao = os.getcwd()
    backupsTo = os.path.join(diretorio_padrao,'backupsTo')
    logger.add("backupsTo.log")
    
    if not os.path.isdir(backupsTo):
        os.mkdir('backupsTo')
    
    print('\n|----------------------------------------------------------|')
    print('|        INICIANDO CÓPIA DE ARQUIVOS PARA "backupsTo"      |')
    print('|----------------------------------------------------------|\n')
    
    for arquivos in os.listdir(os.chdir('backupsFrom')):
        nome = os.path.basename(arquivos)
        data_criacao = os.path.getctime(arquivos)
        data_criacao = datetime.fromtimestamp(data_criacao)
        ultima_data = data_criacao + timedelta(days=+3)
        
        if ultima_data >= datetime.today():
            shutil.copyfile(f'{diretorio_padrao}\\backupsFrom\\{arquivos}', f'{diretorio_padrao}\\backupsTo\\{arquivos}')
            logger.info(f'\n Arquivo {nome} copiado para backupsTo com sucesso!\n')         
        else:
            logger.error(f'\n O arquivo {nome} deveria ter sido excluído anteriormente, já que passa de 3 dias.\n')

    os.chdir('C:\home\\valcann')


listar_arquivos('backupsFrom')
remover_arquivos('backupsFrom')
copiar_arquivos('valcann')

