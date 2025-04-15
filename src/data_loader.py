import json
import py7zr
from datasets import DatasetDict, Dataset
import logging

#reference: https://huggingface.co/datasets/Samsung/samsum/blob/main/samsum.py
#https://stackoverflow.com/questions/32797851/how-to-read-contents-of-7z-file-using-python

class DataLoader:
    def __init__(self, data_path="data/corpus.7z"):
        """Initialize with path to data"""
        self.data_path = data_path
        self.logger = logging.getLogger(__name__)

    def load(self) -> DatasetDict:
        #Loading and return dataset#
        #reads the archive file and DatasetDict is memory efficient 
        #can use "datasets.load_dataset()" for large datasets
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
