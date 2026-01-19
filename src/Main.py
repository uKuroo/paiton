import time
from pathlib import Path
import shutil

import Config

pasta = Path(Config.OBSERVED_FOLDER)
if(pasta.exists()):

    while(True):

        arquivos = [arquivo for arquivo in pasta.iterdir() if arquivo.is_file()]

        for arquivo in arquivos:
            nomeArquivo = arquivo.name
            pastaDestino = Config.BASE_EXTENSION_FOLDER
            
            prefix = arquivo.name.split("_")[0]

            if(Config.PREFIX_FOLDERS.get(prefix) != None):
                pastaDestino += Config.PREFIX_FOLDERS[prefix]
                nomeArquivo = arquivo.name[len(prefix)+1:]
            else:
                pastaDestino += "Outros/"

            sufix = Config.EXTENSIONS_FOLDERS.get(arquivo.suffix)
            if( sufix != None):
                pastaDestino += sufix
            
                Path(pastaDestino).mkdir(parents=True, exist_ok=True)

                pastaDestino += nomeArquivo

                pastaFinal = Path(pastaDestino)
                shutil.move(arquivo, pastaFinal)
                
                message = f'Arquivo {arquivo.name} movido para {pastaFinal}'
                print(message)
                
                message = f'[{time.strftime("%d/%m/%Y %H:%M:%S")}]: ' + message
                with open("file_history.log", "a") as log_file:
                    log_file.write(message + "\n")

        time.sleep(5)
else:
    print(f'Diretório "{pasta}" inexistente')