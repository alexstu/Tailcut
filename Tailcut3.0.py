#!usr/bin/python

import os
import argparse
import math
import numpy as np





CRITICAL_PROCENTAGE = 0.1

MIN_TAIL_LENGTH = 5



class Read(object):
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



class PathMaker(object):

	__doc__ = """ 
	This class is used to take user input and convert it into acceptible format. 
	It is following Singleton pattern, for storing input path and more secure usage
	
		path - str, (default - None):
	 		path to file (or directory in case of output mode)
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
			cls.instance = super(PathMaker, cls).__new__(cls)
		return cls.instance


	def make_input_path(self, path=None):

		if path[-6:] == ".fastq" and path[-7] != "/":
				pass
		elif path[-7] == "/":
			raise ValueError("Error in 'PathMaker' instance generated, 'make_input_path' method: input file name shouldn`t be ``.")
		elif path[-1] == "/":
			raise ValueError("Error in 'PathMaker' instance generated, 'make_input_path' method: input path should be a path to file, not directory.")
		elif path[-1] != "/":
			path = 	path[:path.rfind(".")] +  ".fastq"
		else:
			raise ValueError(f"Error in 'PathMaker' instance generated, 'make_input_path' method: some bad shit happened. \nIt was caused by path: {path}")

		if os.path.isfile(path):
			self.input_path = path
			return path
		else:
			raise FileNotFoundError("Error in 'PathMaker' instance generated, 'make_input_path' method: file with raw reads not found, please check the input")


	def make_output_path(self, path=None):
		if path:
			if os.path.isdir(path):
		 		return path + "output_cut.fastq", path + "output_uncut.fastq"
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
		 				return path + "output_cut.fastq", path + "output_uncut.fastq"
		 			else:

		 				raise ValueError("Error in 'PathMaker' instance generated, 'make_output_path' method: directory not found, and error occupied \nwhile trying to create it.")
		else:
			if hasattr(self, "input_path"):
				return self.input_path[:self.input_path.rfind("/")] + ".output_cut.fastq", self.input_path[:self.input_path.rfind("/")] + ".output_uncut.fastq"
			else:
				return "output_cut.fastq", "output_uncut.fastq"



def make_read(fd):

	read = Read('','','','')

	read.name = fd.readline()[:-1]
	read.seq = fd.readline()[:-1]
	read.plus = fd.readline()[:-1]
	read.qual = fd.readline()[:-1]

	return read


def put_read(read, fd):
		
	fd.write(read.name + "\n")
	fd.write(read.seq + "\n")
	fd.write(read.plus + "\n")
	fd.write(read.qual + "\n")

	return 0




def get_T_tail(read):

	result = Tail(0, 0)
	critical_S_amount = math.ceil(len(read.seq) * CRITICAL_PROCENTAGE)

	global_amount_W = 0
	local_amount_S = 0.0
	local_amount_T = 0.0
	score_T_line = []
	i = 0
	while i < len(read.seq):

		global_amount_W += 1

		if (read.seq[i] == "T"):
			local_amount_T += 1
		else:
			local_amount_S += 1

		if (local_amount_S > critical_S_amount):
			i -= 1
			break

		#print read.seq[: i + 1], read.seq[i], local_amount_S, i

		score_T_line.append(local_amount_T/global_amount_W)
		i += 1

	if i == len(read.seq):
		i -= 1 
	while (i != 0):
		if (read.seq[i] != "T"):

			i = i - 1
			score_T_line.pop()
			#global_amount_W = global_amount_W - 1
			local_amount_S = local_amount_S - 1

		else:
			break

	while (i != 0):
		#print(CRITICAL_PROCENTAGE)
		if (score_T_line[i] >= 1 - CRITICAL_PROCENTAGE):
			break
		else:
			i = i - 1

	result.score = score_T_line[i]
	result.index = i
	if (i < MIN_TAIL_LENGTH - 1):
		result.score = 0
		result.index = 0

	return result



def unit_compl(letter):

	if (letter == 'A'):
		return 'T'
	if (letter == 'T'):
		return 'A'
	if (letter == 'G'):
		return 'C'
	if (letter == 'C'):
		return 'G'
	if (letter == 'N'):
		return 'N'
	if (letter == 'X'):
		return 'X'


def reverse_compl(read):
	if read.seq == "":
		return ""
	#print(f"rrr#{read.seq}#rrr")
	result = Read("", "", "", "")
	result.name = read.name
	result.plus = read.plus

	for i in range(len(read.seq) - 1, 0, -1):
		#print (f"unit_compl(read.seq[i]):{read.seq[i]}")
		result.seq = result.seq + unit_compl(read.seq[i])
		result.qual = result.qual + read.qual[i]

	return result


def get_best_read(read_1, read_2):

	result = Read("", "", "", "")


	if read_1.seq == '':
		return read_2

	elif read_2.seq == '':
		return read_1

	else:
		if (len(read_1.seq) <= len(read_2.seq)):
			return read_1
		else:
			return read_2




def get_tail(read):

	result = Read("", "", "", "")

	tail_T = get_T_tail(read)
	if (tail_T.index >= MIN_TAIL_LENGTH - 1):
		result.name = read.name
		result.plus = read.plus
		result.seq = read.seq[ : tail_T.index + 1]
		result.qual = read.qual[ : tail_T.index + 1]


	return result






def cut_tail(read):

	result = Read("", "", "", "")

	tail_T = get_T_tail(read)
	if (tail_T.index >= MIN_TAIL_LENGTH - 1):
		result.name = read.name
		result.plus = read.plus
		result.seq = read.seq[tail_T.index + 1 : ]
		result.qual = read.qual[tail_T.index + 1 : ]

	#print '+', result.seq
	return result





def main():
	global MIN_TAIL_LENGTH
	global CRITICAL_PROCENTAGE
	parser = argparse.ArgumentParser() 

	parser.add_argument("-i", "--input", type=str, default=None,
	                    help="path (relative or full) to .fastq file with reads")
	parser.add_argument("-o", "--output", type=str, default=None, 
	                    help="path (relative or full) to directory for output")
	parser.add_argument("-p", "--critical_procentage", type=float, default=0.1, 
	                    help="critical procentage of non-A nucleotides")
	parser.add_argument("-m", "--min_tail_length", type=int, default = MIN_TAIL_LENGTH,
	                    help="Minimal length of tails")

	args = parser.parse_args()

	pathmaker = PathMaker()


	input_path = args.input
	output_path = args.output
	MIN_TAIL_LENGTH = int(args.min_tail_length)
	CRITICAL_PROCENTAGE = float(args.critical_procentage)
	output_path_cut, output_path_uncut = pathmaker.make_output_path(output_path)
	print(CRITICAL_PROCENTAGE)

	input_path = pathmaker.make_input_path(input_path)
	

	nul_dir = os.getcwd()
	fd_data = open(input_path, "r")
	fd_cut = open(output_path_cut, "w")
	fd_length = open(output_path_cut + '.length.txt', "w")


	curent_read = Read("", "", "", "")
	curent_reverse_read = Read("", "", "", "")

	cut_read = Read("", "", "", "")
	cut_reverse_read = Read("", "", "", "")

	result_read = Read("", "", "", "")


	while(True):

		curent_read = make_read(fd_data)
		if (curent_read.qual == ""):
			break
		curent_reverse_read = reverse_compl(curent_read)
		
		cut_read = cut_tail(curent_read)
		cut_reverse_read = cut_tail(curent_reverse_read)


		result_read = get_best_read(cut_read, cut_reverse_read)


		if (len(result_read.seq) != 0):
			put_read(result_read, fd_cut)
			fd_length.write(str(len(result_read.seq)) + '\n')


	fd_data.close()
	fd_cut.close()
	fd_length.close()




if __name__ == "__main__":
	main()