import time
from pathlib import Path
import shutil

import Config

pasta = Path(Config.OBSERVED_FOLDER)
if(pasta.exists()):

    while(True):
        print("Executou")

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

        time.sleep(5)
else:
    print(f'Diretório "{pasta}" inexistente')