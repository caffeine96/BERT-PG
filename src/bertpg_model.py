####################################
# BERT Pointer Generator Class 	   #
####################################
import torch
import torch.nn as nn
from pytorch_transformers import *

class BERTPG():
	def __init__(self,kwargs):
		self.mode = kwargs["mode"]
		self.max_len_in = kwargs["max_len_in"]
		self.max_len_out = kwargs["max_len_out"]

		# Device to map the tensors
		self.device = torch.device(
			"cuda" if torch.cuda.is_available() else "cpu"
			)

		# Initializing the BERT Tokenizer and Model
		self.bert_tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
		self.bert_encoder = BertModel.from_pretrained("bert-base-uncased")
		# To use multiple GPUs
		self.bert_encoder = nn.DataParallel(self.bert_encoder)
		self.bert_encoder = self.bert_encoder.to(device)

		
		