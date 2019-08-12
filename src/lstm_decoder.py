###############################################################################
# LSTM Decoder Network 			   											  #	
# The decoder is the same as mentioned in-									  #
# "Get To The Point: Summarization with Pointer-Generator Networks"			  #
# Link - https://arxiv.org/pdf/1704.04368.pdf								  #
#																			  #
# The architecture uses attention and copy mechanism while decoding			  #
# Also to penalize repeated decoding coverage loss is calculated			  #
# We use the same terminology as in paper to avoid confusion				  #
###############################################################################

import torch
import torch.nn as nn
import torch.nn.functional as F


def LSTMDecoder(nn.Module):
	def __init__(self,in_dim,out_dim,vocab,max_len_in):
		""" Constructor
		Input: in_dim	- Dimension of input vector
			   out_dim	- Dimension of output vector
			   vocab	- Vocabulary of the embedding
		"""
		super(LSTMDecoder, self).__init__()
		# For attention calculation
		self.w_h 	= nn.Linear(in_dim,out_dim)
		self.w_s 	= nn.Linear(in_dim,out_dim)
		self.v 		= nn.Linear(out_dim,max_len_in)

		self.soft_max = torch.nn.Softmax(dim=2)


	def forward(self, x, s, h):
		""" Function for forward pass
		All the terminologies are as mentioned in the paper.
		Input:	x	- Input to the decoder at the time step
				s 	- Decoder state at time step
				h 	- Encoder input embedding
		Output: output 	- Output of the network with dimension vocab
		"""
		
		# Calculating attention . 
		e = self.v(nn.Tanh(self.w_h(h) + self.w_s(s)))	# Equation (1)
		a = self.soft_max(e)							# Equation (2)

		


		return output
