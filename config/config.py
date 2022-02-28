import sys,os
from pathlib import Path
import yaml
import logging 
import logging.config

PROJECT_PATH = Path(__file__).parent.parent.absolute()
CONFIG_PATH = Path(PROJECT_PATH,"config")
SRC_PATH = Path(PROJECT_PATH,"src")
WEBAPP_PATH = Path(PROJECT_PATH,"webapp")
DATA_PATH = Path(PROJECT_PATH,"data")
MODEL_PATH = Path(PROJECT_PATH,"model")
LOGS_PATH = Path(PROJECT_PATH,"logs")

#read yaml file
with open(Path(CONFIG_PATH,'params.yaml'),'r') as file:
  params= yaml.safe_load(file)
  

with open(Path(CONFIG_PATH,'logs_config.yaml'), 'r') as f:
    config = yaml.safe_load(f.read())
    config['handlers']['info']['filename'] = os.path.join(PROJECT_PATH,LOGS_PATH,Path(config['handlers']['info']['filename']))
    config['handlers']['error']['filename'] = os.path.join(PROJECT_PATH,LOGS_PATH,Path(config['handlers']['error']['filename']))
    logging.config.dictConfig(config)

logger = logging.getLogger("root")

logger.debug("config set up complete")
