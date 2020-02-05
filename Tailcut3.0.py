


import os
import argparse
import numpy as np




parser = argparse.ArgumentParser() 

parser.add_argument("-i", "--input", type=str,
                    help="path (relative or full) to .fastq file with reads")
parser.add_argument("-o", "--output", type=str,
                    help="path (relative or full) to .fastq file with reads")







class Read(oblect):
	name = ""
	seq = ""
	plus = ""
	qual = ""
	def __init__(self, name, seq, plus, qual):
		self.name = name
		self.seq = seq
		self.plus = plus
		self.qual = qual


class Tail(object):
	index = 0
	score = 0.0
	def __init__(self, index, score):
		self.index = index
		self.score = score


class Store(object):
    def __init__(self, f):
        self.f = f
        self.store = None

    def __call__(self, *args):
    	if not self.store:
        	self.store = self.f(*args)
        	return self.store
        else:
        	return f(*args)


class PathCorrector(object):

	__doc__ = """ 
	This class is used to take user input and convert it into acceptible format. 
	It is following Singleton pattern, for storing input path and more secure usage
	
		path - str, (default - None):
	 		path to file (or directory in case of output mode)
	 	mode - str, "I" or "O", (default - "I"):
	 		which path is provided - with input reads of for output reads 
	 ***********************IMPORTANT!***********************
	 If no path for output reads provided, modified reads will be saved in the
	 same directory as input reads with name "output.fastq"
	 if the name of input file doesn`t end with .fastq, it is considered as user input 
	 mistake and file extension in user input will be changed; if no such file found, an error will
	 be generated.
	 GL, HF
	 """
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


    def make_input_path(self, path=None):
    	""
    	if path[-6:] == ".fastq" and path[-7] != "/":
	 			pass
	 		elif path[-7] == "/":
	 			raise ValueError("Error in 'PathCorrector' instance generated, 'make_input_path' method: input file name shouldn`t be ``.")
	 		elif path[-1] == "/":
	 			raise ValueError("Error in 'PathCorrector' instance generated, 'make_input_path' method: input path should be a path to file, not directory.")
	 		elif path[-1] != "/":
	 			path = 	path[:path.rfind(".")] +  ".fastq"
	 		else:
	 			raise ValueError(f"Error in 'PathCorrector' instance generated, 'make_input_path' method: some bad shit happened. \nIt was caused by path: {path}")

	 		if os.path.isfile(path):
	 			self.input_path = path
	 			return path
	 		else:
	 			raise FileNotFoundError("File with raw reads not found, please check the input")


    def make_output_path(self, path=None):
    	if path:
		 		if os.path.isdir(path):
		 			return path + "output.fastq"
		 		elif os.path.isfile(path): 
		 		# TODO: An error must be written here
		 			return path
		 		else:
		 			if path[-1] == "/":
		 				tmp_dir = path[:path[:-1].rfind("/")]
		 			else:
		 				tmp_dir = path[:path.rfind("/")]

		 			if os.path.isdir(tmp_dir):
		 				os.mkdir(path)
		 				return path + "output.fastq"
		 			else:

		 				raise ValueError("Error in 'PathCorrector' instance generated, 'make_output_path' method: directory not found, and error occupied \nwhile trying to create it.")
		else:
			if hasattr(self, "input_path"):
				return self.input_path[:self.input_path.rfind("/")] + ".output.fastq"
			else:
				return "output.fastq"



@
	 		if os.path.isfile(path):
	 			return pathStore
def make_filename(path=None, mode="I"):
	__doc__ = """ 
	This function takes user input and makes it acceptable for the program. 
	Arguments:
		path - str, (default - None):
	 		path to file (or directory in case of output mode)
	 	mode - str, "I" or "O", (default - "I"):
	 		which path is provided - with input reads of for output reads 
	 ***********************IMPORTANT!***********************
	 If no path for output reads provided, modified reads will be saved in the
	 same directory as input reads with name "output.fastq"
	 if the name of input file doesn`t end with .fastq, it is considered as user input 
	 mistake and file extension in user input will be changed; if no such file found, an error will
	 be generated.
	 GL, HF
	 """

	 if isinstance(path, str):
	 	if mode == "I":
	 		if path[-6:] == ".fastq" and path[-7] != "/":
	 			pass
	 		elif path[-7] == "/":
	 			raise ValueError("Error in 'make_directory' funcion generated, mode='I': input file name shouldn`t be ``.")
	 		elif path[-1] == "/":
	 			raise ValueError("Error in 'make_directory' funcion generated, mode='I': input path should be a path to file, not directory.")
	 		elif path[-1] != "/":
	 			path = 	path[:path.rfind(".")] +  ".fastq"
	 		else:
	 			raise ValueError(f"Error in 'make_directory' funcion generated, mode='I': some bad shit happened. \nIt was caused by path: {path}")

	 		else:
	 			raise FileNotFoundError("File with raw reads not found, please check the input")
	 	elif mode == "O":
	 		if path:
		 		if os.path.isdir(path):
		 			return path + "output.fastq"
		 		elif os.path.isfile(path): 
		 		# TODO: An error must be written here
		 			return path
		 		else:
		 			if path[-1] == "/":
		 				tmp_dir = path[:path[:-1].rfind("/")]
		 			else:
		 				tmp_dir = path[:path.rfind("/")]

		 			if os.path.isdir(tmp_dir):
		 				os.mkdir(path)
		 				return path + ""
		 			else:

		 				raise ValueError("Error in 'make_directory' funcion generated, mode='O': directory not found, and error occupied \nwhile trying to create it.")

	 	else:
	 		raise ValueError("Error in 'make_directory' funcion generated: mode must be in ['O', 'I'] list.")
	 else:
	 	raise TypeError("Error in 'make_directory' funcion generated: path must be of 'str' type!")










if ___name__ == "__main__":
	args = parser.parse_args()