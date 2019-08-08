###############################################################################
# Feed Forward Network 			   											  #
# Two layer network with ReLU activation at first and softmax at second layer #
###############################################################################

import torch
import torch.nn as nn
import torch.nn.functional as F


def FeedForward(nn.Module):
	def __init__(self,in_dim,out_dim,vocab):
		""" Constructor
		Input: in_dim	- Dimension of input vector
			   out_dim	- Dimension of output vector
			   vocab	- Vocabulary of the embedding
		"""
		super(FeedForward, self).__init__()
		self.fc1 = nn.Linear(in_dim,out_dim)
		self.fc2 = nn.Linear(out_dim,vocab)
		self.soft_max = torch.nn.Softmax(dim=2)


	def forward(self, inp):
		""" Function for forward pass
		Input:	inp 	- Input to the network of dimension in_dim
		Output: output 	- Output of the network with dimension vocab
		"""
		out_intermediate = F.relu(self.fc1(inp))
		output =self.soft_max(self.fc2(out_intermediate))
		return output
