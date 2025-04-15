import json
import py7zr
from datasets import DatasetDict, Dataset
import logging

class DataLoader:
    def __init__(self, data_path="data/corpus.7z"):
        """Initialize with path to data"""
        self.data_path = data_path
        self.logger = logging.getLogger(__name__)

    def load(self) -> DatasetDict:
        """Load and return dataset"""
        try:
            with py7zr.SevenZipFile(self.data_path, 'r') as archive:
                files = archive.readall()
                return DatasetDict({
                    'train': Dataset.from_list(json.loads(files['train.json'].read())),
                    'test': Dataset.from_list(json.loads(files['test.json'].read()))
                })
        except FileNotFoundError:
            self.logger.error(f"File not found: {self.data_path}")
            raise
        except json.JSONDecodeError:
            self.logger.error("Invalid JSON in dataset")
            raise
        except Exception as e:
            self.logger.error(f"Unexpected error: {e}")
            raise