import os
import re
import urllib.request as request
import zipfile 
from src.textSummarizer.logging import logger
from src.textSummarizer.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"file is downloaded")
        else:
            logger.info(f"File already exists")
        
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            for member in zip_ref.infolist():
                sanitized_name = member.filename.replace(':', '_')
                # Normalize to OS path separators
                target_path = os.path.normpath(os.path.join(unzip_path, sanitized_name))

                if member.is_dir():
                    os.makedirs(target_path, exist_ok=True)
                else:
                    os.makedirs(os.path.dirname(target_path), exist_ok=True)
                    with zip_ref.open(member) as source, open(target_path, 'wb') as target:
                        target.write(source.read())

        logger.info("Extraction complete")