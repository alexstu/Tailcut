#The program is designed to get obtained data with reads from a certain
# .fastq file and rewrite it having cut poly(A) suffix or poly(T) prefix. 
#The amount of nucleotides to cut can be variated

import sys
import math


################################################################
#File names and global variables will be used in the program;
################################################################


READ_LENGTH = int(sys.argv[1])			#	length of reads in data file; integer
MIN_TAIL_LENGTH = int(sys.argv[2])		#	minimum length of suffix/prefix YET CAN BE CONSIDERED a tail; integer
CRITIAL_PROCENTAGE = float(sys.argv[3])	#	procent of mistakes in tail YET ACCEPTABLE; [0;1]
TAIL_TYPE = sys.argv[4]					#	operational mode; "A"/"T"

file_name_data = sys.argv[5]

file_name_cut = sys.argv[6]
file_name_uncut = sys.argv[7]


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
	typ = ""
	score = 0.0
	def __init__(self, index, typ, score):
		self.index = index
		self.typ  = typ
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

	result = Tail(0, "T", 0)
	critical_S_amount = math.ceil(READ_LENGTH * CRITIAL_PROCENTAGE)

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


def get_A_tail(read):

	result = Tail(0, "A", 0)
  	critical_S_amount = math.ceil(READ_LENGTH * CRITIAL_PROCENTAGE)
	string = read.seq[::-1]
	#print string

	global_amount_W = 0
	local_amount_S = 0.0
	local_amount_A = 0.0
	score_A_line = []

	for i in range (len(string)):

		global_amount_W = global_amount_W + 1

		if (string[i] == "A"):
			local_amount_A = local_amount_A + 1
		else:
			local_amount_S = local_amount_S + 1

		if (local_amount_S > critical_S_amount):
			i = i - 2
			break

		#print string[: i + 1], string[i], local_amount_S, i

		score_A_line.append(local_amount_A/global_amount_W)

	while (i != 0):
		if (string[i] != "A"):

			i = i - 1
			score_A_line.pop()
			global_amount_W = global_amount_W - 1
			local_amount_S = local_amount_S - 1

		else:
			break

	while (i != 0):
		if (score_A_line[i] >= 1 - CRITIAL_PROCENTAGE):
			break
		else:
			i = i - 1

	result.score = score_A_line[i]
	result.index = len(string) - i - 1
	if (i < MIN_TAIL_LENGTH - 1):
		result.score = 0
		result.index = len(string)

	return result


def cut_tail(read):

	result = Read("", "", "", "")

	if (TAIL_TYPE == "T"):
		tail_T = get_T_tail(read)
		if (tail_T.index >= MIN_TAIL_LENGTH - 1):
			result.name = read.name
			result.plus = read.plus
			result.seq = read.seq[tail_T.index + 1 : ]
			result.qual = read.qual[tail_T.index + 1 : ]


	if (TAIL_TYPE == "A"):
		tail_A = get_A_tail(read)
		#print read.name, tail_A.index, tail_A.score, read.seq[ : tail_A.index]
		if ((len(read.seq) - tail_A.index) >= MIN_TAIL_LENGTH - 1):
			print read.name
			result.name = read.name
			result.plus = read.plus
			result.seq = read.seq[ : tail_A.index]
			result.qual = read.qual[ : tail_A.index]

	return result



def get_tail(read):

	result = Read("", "", "", "")

	if (TAIL_TYPE == "T"):
		tail_T = get_T_tail(read)
		if (tail_T.index >= MIN_TAIL_LENGTH - 1):
			result.name = read.name
			result.plus = read.plus
			result.seq = read.seq[ : tail_T.index + 1]
			result.qual = read.qual[ : tail_T.index + 1]


	if (TAIL_TYPE == "A"):
		tail_A = get_A_tail(read)
		print read.name, tail_A.index, tail_A.score, read.seq[ : tail_A.index]
		if ((len(read.seq) - tail_A.index) >= MIN_TAIL_LENGTH - 1):
			print read.name
			read.seq = read.seq[ : tail_A.index]
			read.qual = read.qual[ : tail_A.index]

	return result


################################################################
#Opening files
################################################################

fd_data = open(file_name_data, "rb")
fd_cut = open(file_name_cut, "wb")
fd_uncut = open(file_name_uncut, "wb")


################################################################
#Main body
################################################################

curent_read = Read("", "", "", "")
tail_read = Read("", "", "", "")
cut_read = Read("", "", "", "")


while(True):

	curent_read = get_read(fd_data)
	if (curent_read.qual == ""):
		break

	cut_read = cut_tail(curent_read)

	#print list(tail_read.seq), len(tail_read.seq)
	#print cut_read.name, list(cut_read.seq), len(cut_read.seq)#, "\n"

	if (len(cut_read.seq) == 0):
		put_read_uncut(curent_read, fd_uncut)
	else:
		if (len(cut_read.seq) != 0):
			put_read_cut(cut_read, fd_cut)


################################################################
#Closing files
################################################################

fd_data.close()
fd_cut.close()
fd_uncut.close()


################################################################
#Terminating
################################################################

print "End\t", file_name_cut, "\t", file_name_uncut







