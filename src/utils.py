##########################################################
# File containing all general utilities for the  project #
##########################################################

import argparse

def parse_args():
	""" Function that returns command line arguments in the form of
	dictionary 			
	"""
	parser = argparse.ArgumentParser() #Creating a parser object
	parser.add_argument(
						"--mode",default="train",
						choices=("train","predict"),
						help="Mode in which you want to use the model"
						)

	args = parser.parse_args()  #Parsing arguments
	
	# Returning arguments in the form of Python dictionary
	return vars(args)


if __name__ == "__main__":
	kwargs = parse_args()