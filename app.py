import os
import time
import logging
from datetime import timedelta
from datetime import datetime


log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'

logging.basicConfig(filename='backupsFrom.log',
                    # w -> sobrescreve o arquivo a cada log
                    # a -> não sobrescreve o arquivo
                    filemode='w',
                    level=logging.DEBUG,
                    format=log_format)

logger = logging.getLogger('vinicius')


def logs(nome:str, tamanho:str, data_criacao:str, data_alteracao:str) -> str:

    logger.info(f'Nome: {nome}; Tamanho: {tamanho} KB; Data de Criacao: {data_criacao} ; Ultima alteracao: {data_alteracao} \n')


def listar_arquivos(diretorio):
    os.chdir(diretorio)

    for arquivos in os.listdir():
            nome = os.path.basename(arquivos)
            tamanho = os.path.getsize(arquivos)
            data_criacao = time.ctime(os.path.getctime(arquivos))
            data_alteracao = time.ctime(os.path.getmtime(arquivos))
            logs(nome, tamanho, data_criacao, data_alteracao)
            print('')
            print("Nome: {}".format(nome))
            print("Tamanho: {} KB".format(tamanho))
            print("Data de criação: {}".format(data_criacao))
            print("Data de última alteração: {}".format(data_alteracao))
            print('')


def removedor_arquivos(diretorio):
    os.chdir(diretorio)
    
    for arquivos in os.listdir():
        data_criacao = os.path.getctime(arquivos)
        data_criacao = datetime.fromtimestamp(data_criacao)
        novo = data_criacao + timedelta(days=+3)   
        if data_criacao > novo:
            #Escrever a lógica da exclusão dos arquivos aqui
            print(f'O arquivo {arquivos} foi excluído, pois tem mais de 3 dias desde a sua criação.')
            os.remove(arquivos)
        else:
            print(f'Este arquivo > {arquivos} < ainda não ultrapassou 3 dias desde de criação.')

diretorio = input('Digite o nome/caminho do diretório que deseja realizar a automatização de backup: ')
removedor_arquivos(diretorio)
# listar_arquivos("backupsFrom")



        



        
        
      

