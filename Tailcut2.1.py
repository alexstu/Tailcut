#The program is designed to get obtained data with reads from a certain
# .fastq file and rewrite it having cut poly(A) suffix or poly(T) prefix. 
#The amount of nucleotides to cut can be variated

import sys
import subprocess
import string
import os
import math


################################################################
#File names and global variables will be used in the program;
################################################################

data_directory = sys.argv[1]
MIN_TAIL_LENGTH = int(sys.argv[2])		#	minimum length of suffix/prefix YET CAN BE CONSIDERED a tail; integer
CRITIAL_PROCENTAGE = float(sys.argv[3])	#	procent of mistakes in tail YET ACCEPTABLE; [0;1]
file_name_data = sys.argv[4]
file_name_cut = sys.argv[5]



################################################################
#Classes section
################################################################

class Read:
	name = ""
	seq = ""
	plus = ""
	qual = ""
	def __init__(self, name, seq, plus, qual):
		self.name = name
		self.seq = seq
		self.plus = plus
		self.qual = qual


class Tail:
	index = 0
	score = 0.0
	def __init__(self, index, score):
		self.index = index
		self.score = score


################################################################
#Functions section
################################################################


def get_read(fd):

	read = Read('','','','')

	read.name = fd.readline()[:-1]
	read.seq = fd.readline()[:-1]
	read.plus = fd.readline()[:-1]
	read.qual = fd.readline()[:-1]

	return read


def put_read_cut(read, fd):
		
	fd.write(read.name + "\n")
	fd.write(read.seq + "\n")
	fd.write(read.plus + "\n")
	fd.write(read.qual + "\n")

	return 0


def put_read_uncut(read, fd):
		
	fd.write(read.name + "\n")
	fd.write(read.seq + "\n")
	fd.write(read.plus + "\n")
	fd.write(read.qual + "\n")

	return 0


def get_T_tail(read):

	result = Tail(0, 0)
	critical_S_amount = math.ceil(len(read.seq) * CRITIAL_PROCENTAGE)

	global_amount_W = 0
	local_amount_S = 0.0
	local_amount_T = 0.0
	score_T_line = []

	for i in range (len(read.seq)):

		global_amount_W = global_amount_W + 1

		if (read.seq[i] == "T"):
			local_amount_T = local_amount_T + 1
		else:
			local_amount_S = local_amount_S + 1

		if (local_amount_S > critical_S_amount):
			i = i - 2
			break

		#print read.seq[: i + 1], read.seq[i], local_amount_S, i

		score_T_line.append(local_amount_T/global_amount_W)

	while (i != 0):
		if (read.seq[i] != "T"):

			i = i - 1
			score_T_line.pop()
			global_amount_W = global_amount_W - 1
			local_amount_S = local_amount_S - 1

		else:
			break

	while (i != 0):
		if (score_T_line[i] >= 1 - CRITIAL_PROCENTAGE):
			break
		else:
			i = i - 1

	result.score = score_T_line[i]
	result.index = i
	if (i < MIN_TAIL_LENGTH - 1):
		result.score = 0
		result.index = 0

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



def get_tail(read):

	result = Read("", "", "", "")

	tail_T = get_T_tail(read)
	if (tail_T.index >= MIN_TAIL_LENGTH - 1):
		result.name = read.name
		result.plus = read.plus
		result.seq = read.seq[ : tail_T.index + 1]
		result.qual = read.qual[ : tail_T.index + 1]


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

	result = Read("", "", "", "")
	result.name = read.name
	result.plus = read.plus

	for i in range(len(read.seq) - 1, -1, -1):

		result.seq = result.seq + unit_compl(read.seq[i])
		result.qual = result.qual + read.qual[i]

	#print result.seq
	return result


def get_best_read(read_1, read_2):

	result = Read("", "", "", "")


	if (read_1.seq == ''):
		return read_2

	if (read_2.seq == ''):
		return read_1

	if (len(read_1.seq) <= len(read_2.seq)):
		return read_1
	else:
		return read_2

################################################################
#Opening files
################################################################

nul_dir = os.getcwd()
os.chdir(data_directory)
fd_data = open(file_name_data, "rb")
fd_cut = open(file_name_cut, "wb")
fd_length = open(file_name_cut + '.length.txt', "wb")



################################################################
#Main body
################################################################

curent_read = Read("", "", "", "")
curent_reverse_read = Read("", "", "", "")

cut_read = Read("", "", "", "")
cut_reverse_read = Read("", "", "", "")

result_read = Read("", "", "", "")


while(True):

	curent_read = get_read(fd_data)
	if (curent_read.qual == ""):
		break
	curent_reverse_read = reverse_compl(curent_read)
	
	cut_read = cut_tail(curent_read)
	cut_reverse_read = cut_tail(curent_reverse_read)


	result_read = get_best_read(cut_read, cut_reverse_read)


	if (len(result_read.seq) != 0):
		put_read_cut(result_read, fd_cut)
		fd_length.write(str(len(result_read.seq)) + '\n')
	#print cut_read.name, list(cut_read.seq), len(cut_read.seq)#, "\n"




################################################################
#Closing files
################################################################


fd_data.close()
fd_cut.close()
fd_length.close()


################################################################
#Terminating
################################################################

#print "End\t", file_name_cut
os.chdir(nul_dir)














