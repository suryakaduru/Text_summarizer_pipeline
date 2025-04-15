# evaluator.py
from rouge_score import rouge_scorer
import logging
import yaml

#https://github.com/huggingface/evaluate/blob/main/metrics/rouge/rouge.py
# Used DeepSeek to understand how to extract f-measure from ROUGE metrics cleanly.


class Evaluator:
    def __init__(self, config_path="configs/default.yaml"):
        """Initialize with metrics from config"""
        self.logger = logging.getLogger(__name__)
        with open(config_path) as f:
            config = yaml.safe_load(f)
        self.metrics = config["evaluation"]["metrics"]
        self.scorer = rouge_scorer.RougeScorer(
            self.metrics,
            use_stemmer=True
        )

    #https://github.com/pltrdy/rouge
    def evaluate(self, reference: str, hypothesis: str) -> dict:
        """Calculate and return scores"""
        try:
            scores = self.scorer.score(reference, hypothesis)
            return {metric: {"fmeasure": scores[metric].fmeasure} for metric in self.metrics}
        except Exception as e:
            self.logger.error(f"Evaluation failed: {e}")
            return {metric: {"fmeasure": 0.0} for metric in self.metrics}
