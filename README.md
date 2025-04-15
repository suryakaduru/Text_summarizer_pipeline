#  Modular Text Summarization Pipeline

A modular and extensible text summarization application powered by a self-hosted Large Language Model (LLM). This project enables efficient data loading, summarization, evaluation, and analysis in a streamlined pipeline.

---

##  Overview

This project aims to build a modular text summarization system with the following components:

- **Data Loader**: Loads and prepares the dataset.
- **Model**: Loads and configures the summarization model.
- **Pipeline**: Orchestrates data flow and executes summarization.
- **Evaluator**: Evaluates summaries using metrics like ROUGE.
- **Main Runner**: CLI script to run the complete pipeline.

---

##  Project Structure

```
text_summarization_pipeline/
├── configs/
│   └── default.yaml             # Configuration file for the pipeline
├── data/
│   └── corpus.7z                # Dataset archive (e.g., SAMSum)
├── src/
│   ├── data_loader.py           # Loads and preprocesses data
│   ├── model.py                 # Summarization model configuration
│   ├── pipeline.py              # Coordinates the summarization steps
│   ├── evaluator.py             # Evaluation and metrics analysis
│   └── main.py                  # Main CLI script to run the pipeline
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

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Download and Prepare Dataset**

- Download the dataset  [sumsum](https://huggingface.co/datasets/Samsung/samsum/tree/main) from hugging face and place it inside the `data/` directory.
- Ensure the dataset is named correctly (e.g., `corpus.7z`).
- Download the model as well from hugging face to run it locally from here [bart-large-cnn-samsum](https://huggingface.co/philschmid/bart-large-cnn-samsum/tree/main) and place it like this
```
- models/
    └── distilbart/
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
python src/main.py
```

This script will:
- Load and preprocess the dataset
- Run the summarization model
- Evaluate generated summaries using ROUGE
---

##  Testing

Run test cases with:

```bash
python tests/test.py
```

The test script will:
- Load a subset of the dataset
- Generate summaries
- Evaluate using ROUGE
- Save results to `test_results.csv`


```
Disclaimer and notes:
“This project uses a pre-trained "philschmid/bart-large-cnn-samsum model" for zero-shot summarization without fine-tuning. All outputs were generated using the model as-is, focusing on pipeline structure, evaluation, and analysis.”
Some parts of this code modules were generated or refined with the assistance of AI tools such as ChatGPT and DeepSeek. 
These tools were used to understand model configurations, evaluation metrics (ROUGE), and to structure the summarization pipeline effectively.
```



> “This project uses a pre-trained "philschmid/bart-large-cnn-samsum model" for zero-shot summarization without fine-tuning. All outputs were generated using the model as-is, focusing on pipeline structure, evaluation, and analysis.”

