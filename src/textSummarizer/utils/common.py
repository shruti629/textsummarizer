import os
from box.exceptions import BoxValueError
import yaml
from src.textSummarizer.logging import logger
from ensure import ensure_annotation
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotation
def read_yaml(path_to_yml: Path) -> ConfigBox:
    """ reads yaml file and returns


    Args:
       path_to_yaml (str): path like input

    Raises:
       ValueError: if yaml file is empty
       e: empty file

    Returns:
       ConfigBox: ConfigBox type

    """
    try:
        with open(path_to_yml) as yml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f'yaml file:{path_to_yml} loaded successfully')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml files is empty")
    except Exception as e:
        raise e


@ensure_annotation
def create_directories(path_to_directories: list,verbose=True):
    """ create list of directories

    Args:
      path_to_directories (list): list of path of directories
      ignore_log (bool,optional): ignore if multiple dirs is to be created. 

    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f'created directory at:{path}')
            