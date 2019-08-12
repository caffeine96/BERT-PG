###############################################################################
# LSTM Decoder Network 			   											  #	
# The decoder is the same as mentioned in-									  #
# "Get To The Point: Summarization with Pointer-Generator Networks"			  #
# Link - https://arxiv.org/pdf/1704.04368.pdf								  #
#																			  #
# The architecture uses attention and copy mechanism while decoding			  #
# Also to penalize repeated decoding coverage loss is calculated			  #
###############################################################################

import torch
import torch.nn as nn
import torch.nn.functional as F


def LSTMDecoder(nn.Module):
	def __init__(self,in_dim,out_dim,vocab):
		""" Constructor
		Input: in_dim	- Dimension of input vector
			   out_dim	- Dimension of output vector
			   vocab	- Vocabulary of the embedding
		"""
		super(LSTMDecoder, self).__init__()
		self.fc1 = nn.Linear(in_dim,out_dim)
		self.fc2 = nn.Linear(out_dim,vocab)
		self.soft_max = torch.nn.Softmax(dim=2)


	def forward(self, inp):
		""" Function for forward pass
		Input:	inp 	- Input to the network of dimension in_dim
		Output: output 	- Output of the network with dimension vocab
		"""
		
		return output
