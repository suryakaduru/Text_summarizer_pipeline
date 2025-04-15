# 📝 Modular Text Summarization Pipeline

A modular and extensible text summarization application powered by a self-hosted Large Language Model (LLM). This project enables efficient data loading, summarization, evaluation, and analysis in a streamlined pipeline.

---

## 📌 Overview

This project aims to build a modular text summarization system with the following components:

- **Data Loader**: Loads and prepares the dataset.
- **Model**: Loads and configures the summarization model.
- **Pipeline**: Orchestrates data flow and executes summarization.
- **Evaluator**: Evaluates summaries using metrics like ROUGE.
- **Main Runner**: CLI script to run the complete pipeline.

---

## 🗂️ Project Structure

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

## ⚙️ Setup Instructions

### ✅ Prerequisites

- Python 3.8 or higher
- Git
- Pip

### 🧭 Steps

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

- Download the dataset (e.g., SAMSum) and place it inside the `data/` directory.
- Ensure the dataset is named correctly (e.g., `corpus.7z`).

4. **Configure the Pipeline**

- Edit `configs/default.yaml` to set paths, model settings, logging preferences, etc.

---

## 🚀 Running the Pipeline

Run the full summarization pipeline:

```bash
python src/main.py
```

This script will:
- Load and preprocess the dataset
- Run the summarization model
- Evaluate generated summaries using ROUGE
- Log and store results

---

## ✅ Testing

Run test cases with:

```bash
python tests/test.py
```

The test script will:
- Load a subset of the dataset
- Generate summaries
- Evaluate using ROUGE
- Save results to `test_results.csv`

---

## 📊 Insights

### 🔍 Analysis of Results

- **ROUGE Scores**: Measure similarity between generated and reference summaries.
- **Dialogue Complexity**: Number of speakers and length of dialogue affect summarization quality.

### ⚠️ Observations

- **Challenging Samples**: Multi-speaker or long dialogues are harder to summarize.
- **Common Issues**: Missed key points, irrelevant outputs.

---

## 🔧 Preprocessing & Postprocessing

- **Preprocessing**: Tokenization, normalization, stop-word removal.
- **Postprocessing**: Filtering filler phrases, grammar correction.

---

## ⚠️ Limitations & Improvements

### Limitations

- Performance may vary based on dataset and model choice.
- Dataset size may limit generalization capabilities.

### Future Improvements

- Fine-tune on domain-specific data.
- Add hyperparameter tuning modules.
- Incorporate advanced metrics like **BERTScore**.

---

## 🌟 Optional Enhancements

- **🔁 Hyperparameter Tuning**: Add grid/random search for better performance.
- **📈 Visualization**: Create performance dashboards.
- **🧠 Fine-tuning**: Adapt model to your custom dataset.

---

Feel free to contribute or customize the pipeline to suit your needs. This modular structure makes it easy to extend and experiment with different summarization models and evaluation techniques.
