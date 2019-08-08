###############################################
# Demo program to run BERT Pointer Generator  #
###############################################

from utils import parse_args
from bertpg_model import BERTPG

def main(kwargs):
	if kwargs["mode"] == "train":
		model = BERTPG(kwargs)
		model.train()
	elif kwargs["mode"] == "predict":
		model = BERTPG(kwargs)

if __name__ == "__main__":
	main(parse_args())