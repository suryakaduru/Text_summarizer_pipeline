from data_loader import DataLoader
from model import SummarizationModel
from evaluator import Evaluator
import logging
import yaml

class SummarizationPipeline:
    def __init__(self, config_path="configs/default.yaml"):
        """Initialize all components"""
        self.logger = logging.getLogger(__name__)
        self.config_path = config_path
        self.loader = DataLoader()
        self.model = SummarizationModel(config_path)
        self.evaluator = Evaluator(config_path)

    def run(self) -> list:
        """Run full pipeline"""
        try:
            dataset = self.loader.load()
            max_samples = self._get_config()["data"]["max_samples"]
            
            results = []
            for i in range(min(max_samples, len(dataset['train']))):
                sample = dataset['train'][i]
                result = self._process_sample(sample)
                results.append(result)
            
            return results
        except Exception as e:
            self.logger.error(f"Pipeline failed: {e}")
            return []

    def _get_config(self):
        """Helper to load config"""
        with open(self.config_path) as f:
            return yaml.safe_load(f)

    def _process_sample(self, sample) -> dict:
        """Process single dialogue"""
        gen_summary = self.model.summarize(sample['dialogue'])
        scores = self.evaluator.evaluate(sample['summary'], gen_summary)
        
        return {
            'dialogue': sample['dialogue'],
            'reference': sample['summary'],
            'generated': gen_summary,
            'scores': scores
        }
