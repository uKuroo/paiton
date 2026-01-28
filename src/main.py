import time
from pathlib import Path
import shutil

import config.setup as setup
import config.data as data

def main():
  try:
    config_file = Path('src/config/config.json')
    if not config_file.exists():
      setup.initial_config()

    if(setup.load_config()):
      run_file_organizer()
  except (KeyboardInterrupt):
    print("Programa encerrado pelo usuário...")
    
def run_file_organizer():
  print("Iniciando organizador de arquivos...")
  directory = Path(data.OBSERVED_FOLDER)
  if(directory.exists()):
    while(True):
      files = [file for file in directory.iterdir() if file.is_file()]

      for file in files:
        nomeArquivo = file.name
        pastaDestino = data.BASE_EXTENSION_FOLDER
        
        prefix = file.name.split("_")[0]
        if(data.PREFIX_FOLDERS.get(prefix) != None):
          pastaDestino += data.PREFIX_FOLDERS[prefix]
          nomeArquivo = file.name[len(prefix)+1:]
        else:
          pastaDestino += "Outros/"

        sufix = data.EXTENSIONS_FOLDERS.get(file.suffix)
        if( sufix != None):
          pastaDestino += sufix
      
          Path(pastaDestino).mkdir(parents=True, exist_ok=True)

          pastaDestino += nomeArquivo

          pastaFinal = Path(pastaDestino)
          shutil.move(file, pastaFinal)
          
          message = f'Arquivo {file.name} movido para {pastaFinal}'
          print(message)
          
          message = f'[{time.strftime("%d/%m/%Y %H:%M:%S")}]: ' + message
          
          Path("src/log").mkdir(parents=True, exist_ok=True)
          with open("src/log/file_history.log", "a") as log_file:
            log_file.write(message + "\n")

      time.sleep(5)
  else:
    print(f'Diretório "{directory}" inexistente')
    
if __name__ == "__main__":
  main()