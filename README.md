#  Modular Text Summarization Pipeline

A modular and extensible text summarization application powered by a self-hosted Large Language Model (LLM). This project enables efficient data loading, summarization, evaluation, and analysis in a streamlined pipeline.

## Objective
To build a clean and maintainable summarization pipeline that:

- Uses an open-source LLM (e.g., BART, T5) running locally.
- Handles data loading, model inference, and evaluation modularly.
- Focuses on well-structured Python code with extensibility.
- Analyzes and reflects on model performance and limitations.
---

##  Project Structure

```
text_summarization_pipeline/
├─ configs/
│   └── default.yaml             # Configuration file for the pipeline
├── data/
│   └── corpus.7z                # Dataset archive (e.g., SAMSum)

├── data_loader.py           # Loads and preprocesses data
├── model.py                 # Summarization model configuration
├── pipeline.py              # Coordinates the summarization steps
├── evaluator.py             # Evaluation and metrics analysis
├── main.py                  # Main script to run the pipeline
├── tests/
│   └── test.py                  # Test script with ROUGE-based evaluation
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

##  Setup Instructions

###  Steps

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/text_summarization_pipeline.git
cd text_summarization_pipeline
```

2. **Install Dependencies by creating a new env**
   
```bash
conda create -n summarizer python=3.8 -y
```

```bash
pip install -r requirements.txt
```

3. **Download and Prepare Dataset**

- Download the dataset  [samsum](https://huggingface.co/datasets/Samsung/samsum/tree/main) from hugging face and place it inside the `data/` directory.
- Ensure the dataset is named correctly (e.g., `corpus.7z`).
- Download the model as well from hugging face to run it locally from here [bart-large-cnn-samsum](https://huggingface.co/philschmid/bart-large-cnn-samsum/tree/main) and place it like this
```
- models/
    └── bart-large-cnn-samsum/
        ├── config.json
        ├── pytorch_model.bin
        ├── vocab.json
        └── merges.txt
```
4. **Configure the Pipeline**

- Edit `configs/default.yaml` to set paths, model settings, logging preferences, etc.

---

##  Running the Pipeline

Run the full summarization pipeline:

```bash
python main.py
```

This script will:
- Load and parses the dataset
- Summarizes dialogues using the model
- Evaluate generated summaries using ROUGE
- returns dialouge, reference, generated summary and scores (have a look on sam_res.txt file for output)
---

# Trade-offs and designs

 the below insights were taken from these blogs while researching 
[ROUGE](https://www.traceloop.com/blog/evaluating-model-performance-with-the-rouge-metric-a-comprehensive-guide), [pipeline](https://discuss.huggingface.co/t/pipeline-vs-model-generate/26203)
```
- Pre-trained vs. Fine-tuned: This project uses a pre-trained model with zero-shot inference. While fine-tuning could improve results, the trade-off was speed, simplicity, and hardware constraints.
- Pipeline vs. Raw generate(): We used HuggingFace's pipeline for prototyping and readability. In production, switching to generate() allows more control (e.g., token logging)
- ROUGE as Metric: ROUGE provides quick lexical overlap scoring but lacks semantic understanding. Future work can explore BERTScore or human evaluations.
```
##  Testing (optional to get insights on the dataset)

Run test cases with:

```bash
python tests/test.py
```

The test script will:
- Load a subset of the dataset
- Generate summaries
- gets lowest and highest scores for dialouges in the subset
  


```
Disclaimer and notes:
- This project uses a pre-trained "philschmid/bart-large-cnn-samsum model" for zero-shot summarization without fine-tuning or tranining
- Some parts of this code modules were generated or refined with the assistance of AI tools such as ChatGPT and DeepSeek. 
- These tools were used to understand model configurations, evaluation metrics (ROUGE), and to structure the summarization pipeline effectively.
```


