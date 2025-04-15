
## Summary of Findings from Working with the Dataset
#### Note: only a small subset(50 summaries) of tranining data was used for evaluation 

### Dataset Characteristics
- The dataset consists of short dialogues and their manually written summaries (~16k).
- Dialogues vary in length and complexity, with some containing multiple speakers and intricate interactions.

### Model Performance
- Performs well on shorter, simpler dialogues.
- Struggles with longer, complex dialogues—often missing key points or generating irrelevant content.
- ROUGE scores show reasonable similarity with reference summaries but have room for improvement.

### Evaluation Metrics
- ROUGE scores measure similarity between generated and reference summaries.
- ROUGE-L is particularly useful for assessing summary quality.

## Limitations Observed

### Data Limitations
- **Size and Diversity**: Dataset is small and lacks variety, affecting generalization.
- **Noisy Data**: Some dialogues have typos, errors, or irrelevant information.

### Model Limitations
- **Pre/Postprocessing**: Lacks steps to clean input or refine output.
- **Generalization**: Struggles with out-of-domain or complex dialogues.
- **Evaluation**: ROUGE doesn’t capture all aspects like coherence or relevance.

## Evaluation Summary

![Screenshot 2025-04-15 120420](https://github.com/user-attachments/assets/409454d2-9c1d-4a6e-a91c-0e3b69e1d7ff)

### Top 3 Best Summaries

| ID | ROUGE-L F1 |
|----|------------|
| 11 | 0.9286     |
| 1  | 0.9000     |
| 0  | 0.8421     |

### Top 3 Worst Summaries

| ID | ROUGE-L F1 |
|----|------------|
| 2  | 0.1395     |
| 5  | 0.1538     |
| 30 | 0.2018     |

## Insights and Recommendations

### Complexity and Length
- Longer dialogues with more speakers are harder to summarize.
- Model performs better on shorter, simpler texts. eg: for the first sequence of text it has score of 0.9

### Consistency
- Performance varies significantly, suggesting need for additional training. (FUTURE WORK)

### Error Analysis
- Common issues include misunderstanding complex interactions and speaker switches.
- human evaluation

