import logging
from pipeline import SummarizationPipeline
import yaml
import torch

def setup_logging(config_path="configs/default.yaml"):
    with open(config_path) as f:
        config = yaml.safe_load(f)
    logging.basicConfig(
        level=config["logging"]["level"],
        format=config["logging"]["format"]
    )

def main():
    setup_logging()
    print(f"Using device: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'CPU'}")
    pipeline = SummarizationPipeline()
    results = pipeline.run()
    
    for i, res in enumerate(results):
        print(f"\nSample {i+1}:")
        print(f"Dialogue: {res['dialogue']}")
        print(f"Reference: {res['reference']}")
        print(f"Generated: {res['generated']}")
        print("Scores:")
        for metric, score_dict in res['scores'].items():
            fmeasure = score_dict['fmeasure']
            print(f"  {metric}: {fmeasure:.2f}")

if __name__ == "__main__":
    main()