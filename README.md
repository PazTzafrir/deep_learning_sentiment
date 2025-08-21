## Deep Learning Sentiment Analysis with Model Compression

This repository implements end-to-end sentiment analysis using BERT and RoBERTa. It includes EDA, Hugging Face training with hyperparameter tuning, and three compression techniques—distillation, pruning, and quantization—to reduce model size and latency while preserving accuracy. Out-of-time (OOT) splits are provided for robust evaluation, and final distilled artifacts are saved for reuse in the compression notebooks.

### Notebooks
- `EDA.ipynb`
- `HF_model_HPtuning_bert.ipynb`
- `HF_model_HPtuning_roberta.ipynb`
- `full_code_HPtuning_model_bert.ipynb`
- `full_code_HPtuning_model_roberta.ipynb`
- `compression_distilation_bert.ipynb`
- `compression_distilation_roberta.ipynb`
- `compression_pruning_bert.ipynb`
- `compression_pruning_roberta.ipynb`
- `compression_quantization_bert.ipynb`
- `compression_quantization_roberta.ipynb`

### How to run the notebooks
1. Create an environment and install dependencies (Python 3.10+):
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install torch transformers datasets accelerate evaluate scikit-learn pandas numpy matplotlib seaborn jupyter
# For quantization notebooks you may also need:
# pip install optimum onnxruntime
```
2. Launch Jupyter and open any notebook:
```bash
jupyter lab
```
=======
### Model artifacts for compression (uniform loading across all 6 notebooks) All compression notebooks load a Hugging Face model directory the same way.
=======

3. Download from Google Drive and place locally:
- **BERTweet** —
  - Drive folder: `<DRIVE_URL/model_bert.pt`>`
- **RoBERTa** — 
  - Drive folder: `<DRIVE_URL/model_roberta.pt>`

Reletive local directories:
`Full model/bert/best_bert_model_so_far/model_bert.pt` and `HuggingFace/roberta/best_roberta_model_so_far/model_roberta.pt` 


3. Ensure the data files `OOT_train.csv`, `OOT_val.csv`, and `OOT_test.csv` remain at the repository root (or update paths in the notebooks accordingly). Then run cells top to bottom.

