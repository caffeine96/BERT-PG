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
		self.data_path = kwargs["data_path"]
		self.output_dir = kwargs["output_dir"]
		self.enable_save = kwargs["enable_save"]

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


				

	def train():
		""" Function to train the pointer generator
		"""

		# Saving the hyperparameters when training
		if self.enable_save == True:
			out_file = open(self.output_dir+"hyperparameters.txt","w")
			out_file.write(kwargs)	

