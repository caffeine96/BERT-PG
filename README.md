# BERT-PG
A Pointer Generator with a BERT encoder

## Data Source
As a toy set, we consider DUC2003 summarization dataset as train, DUC2004 summarization dataset as development and Gigaword data as prediction dataset.<br>
The train and dev dataset are pre-processed into text files with each line containing tab separated input and summaries.<br>
**Note:** For the model to run, preprocess your training data into this format.<br>
Data Link- https://github.com/harvardnlp/sent-summary

## Requirements
Install requirements by-<br>
``pip install -r requirements.txt``

## References
1. See, Abigail, Peter J. Liu, and Christopher D. Manning. "Get to the point: Summarization with pointer-generator networks." arXiv preprint arXiv:1704.04368 (2017).
2. Devlin, Jacob, et al. "Bert: Pre-training of deep bidirectional transformers for language understanding." arXiv preprint arXiv:1810.04805 (2018).


### Status
Not ready to use
