####################################
# BERT Pointer Generator Class 	   #
####################################


class BERTPG():
	def __init__(self,kwargs):
		self.mode = kwargs["mode"]
		self.max_len_in = kwargs["max_len_in"]
		self.max_len_out = kwargs["max_len_out"]

	