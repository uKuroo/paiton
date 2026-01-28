import json

import config.data as data
import os

HOME_DIR = os.path.expanduser("~")

BASE_CONFIG = {
  "OBSERVED_FOLDER": f'{HOME_DIR}/Downloads/',
  "BASE_EXTENSION_FOLDER": f'{HOME_DIR}/Downloads/Arquivos/',
  "PREFIX_FOLDERS": {
    "INF": "Informatica/",
    "PRJ": "Projeto/"
  },
  "EXTENSIONS_FOLDERS": {
    ".jpg": "Imagem/",
    ".jpeg": "Imagem/",
    ".png": "Imagem/",
    ".pdf": "Documento/",
    ".doc": "Documento/",
    ".gif": "GIF/",
    ".mp4": "Video/",
    ".mkv": "Video/",
    ".wmv": "Video/",
    ".mp3": "Audio/",
    ".wav": "Audio/"
  }
}

def initial_config():
  with open('src/config/config.json', 'w', encoding='utf-8') as f:
    print("Criando arquivo de configuração padrão em 'src/config/config.json'")
    json.dump(BASE_CONFIG, f, ensure_ascii=False, indent=2)

def load_config():
  with open('src/config/config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)
    
    missing_keys = [key for key in BASE_CONFIG if key not in config]
    
    if missing_keys:
      print(f"ATENÇÃO: As seguintes chaves estão faltando no config.json: {', '.join(missing_keys)}")
      response = input("Deseja resetar o arquivo de configuração e restaurar os padrões? [s/N]: ").strip().lower()
    
      if response == 's':
        initial_config()
        print("Configuração resetada. Recarregando...")
        return load_config()
      else:
        print("Execução interrompida. Por favor, edite 'src/config/config.json' manualmente.")
        return False

    data.OBSERVED_FOLDER = config.get("OBSERVED_FOLDER", "")
    data.BASE_EXTENSION_FOLDER = config.get("BASE_EXTENSION_FOLDER", "")
    data.PREFIX_FOLDERS = config.get("PREFIX_FOLDERS", {})
    data.EXTENSIONS_FOLDERS = config.get("EXTENSIONS_FOLDERS", {})
  print("Configurações carregadas com sucesso")
  return True