from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer
import logging
import torch
import yaml

# The below summarization logic (pipeline, config-based generation) was partially guided by suggestions from ChatGPT and Deepkseek.
# https://huggingface.co/philschmid/bart-large-cnn-samsum/tree/main : took reference for loading the model

class SummarizationModel:
    def __init__(self, config_path="configs/default.yaml"):
        """Initialize with config file"""
        self.logger = logging.getLogger(__name__)
        self.config = self._load_config(config_path)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = None
        self.tokenizer = None
        self._load_model()

   #ref: https://stackoverflow.com/questions/64115827/how-to-pass-yaml-file-path-to-different-modules-and-load-configuration-based-on
    def _load_config(self, config_path):
        """Load settings from YAML file"""
        try:
            with open(config_path) as f:
                return yaml.safe_load(f)
        except Exception as e:
            self.logger.error(f"Config error: {e}")
            raise

    def _load_model(self):
        """Load model files from local """
        try:
            #https://stackoverflow.com/questions/62472238/autotokenizer-from-pretrained-fails-to-load-locally-saved-pretrained-tokenizer
            model_path = self.config["model"]["local_path"]
            self.tokenizer = AutoTokenizer.from_pretrained(model_path)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(model_path).to(self.device)
            
            self.pipeline = pipeline(
                "summarization",
                model=self.model,
                tokenizer=self.tokenizer,
                device=0 if torch.cuda.is_available() else -1
            )
        except Exception as e:
            self.logger.error(f"Model loading failed: {e}")
            raise

    def summarize(self, text: str) -> str:
        #Generate summary using config settings from YAML file
        #took assistance from deepseek for the params loading
        params = self.config["model"]["generation"]
        try:
            result = self.pipeline(
                text,
                max_length=params["max_length"],
                min_length=params["min_length"],
                no_repeat_ngram_size=params["no_repeat_ngram_size"],
                num_beams=params["num_beams"],
                early_stopping=params["early_stopping"]
            )
            return result[0]['summary_text']
        except Exception as e:
            self.logger.error(f"Summarization failed: {e}")
            return ""  # Return empty string on failure
