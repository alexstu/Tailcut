"""The program is designed to get obtained data with reads from a certain
 ".fastq" file and rewrite it, having cut poly(A) tails or poly(T) starts. 
The amount of nucleotides to cut can be variated"""

import sys
import math

"""File names and global variables will be used in the program;
READ_LENGTH is a length of reads in data file;
CRITIAL_PROCENTAGE is a procent of mistakes in tail YET ACCEPTABLE;
MIN_TAIL_LENGTH is a minimum length of suffix/prefix YET CAN BE CONSIDERED a tail;
TAIL_TYPE = "A"/"T" """


file_name_data = '/home/aemilius/Work/Tryp/Datastock/unmapped8to10.fastq'

file_name_cut = '/home/aemilius/Work/Tryp/Bench/out8to10_10%_tail_T_cut_len6.fastq'
file_name_uncut = '/home/aemilius/Work/Tryp/Bench/out8to10_10%_tail_T_UNcut_len6.fastq'


READ_LENGTH = 101
CRITIAL_PROCENTAGE = 0.10
MIN_TAIL_LENGTH = 6
TAIL_TYPE = "T"


"""Arsenal section"""""""""""""""""""""""""""""""""""""""""""""""""""


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



def get_read(read):

    read.name = fd_data.readline()[:-1]
    read.seq = fd_data.readline()[:-1]
    read.plus = fd_data.readline()[:-1]
    read.qual = fd_data.readline()[:-1]

    return read


def put_read_cut(read):
    
    fd_cut.write(read.name + "\n")
    fd_cut.write(read.seq + "\n")
    fd_cut.write(read.plus + "\n")
    fd_cut.write(read.qual + "\n")

    return 0


def put_read_uncut(read):
    
    fd_uncut.write(read.name + "\n")
    fd_uncut.write(read.seq + "\n")
    fd_uncut.write(read.plus + "\n")
    fd_uncut.write(read.qual + "\n")

    return 0


def get_T_tail(read):

    result = Tail(0, "T", 0)
    critical_X_amount = math.ceil(READ_LENGTH * CRITIAL_PROCENTAGE)

    global_amount_N = 0
    local_amount_X = 0.0
    local_amount_T = 0.0
    score_T_line = []

    for i in range (len(read.seq)):

        global_amount_N = global_amount_N + 1

        if (read.seq[i] == "T"):
            local_amount_T = local_amount_T + 1
        else:
            local_amount_X = local_amount_X + 1

        if (local_amount_X > critical_X_amount):
            i = i - 2
            break

        '''print read.seq[: i + 1], read.seq[i], local_amount_X, i'''

        score_T_line.append(local_amount_T/global_amount_N)

    while (i != 0):
        if (read.seq[i] != "T"):

            i = i - 1
            score_T_line.pop()
            global_amount_N = global_amount_N - 1
            local_amount_X = local_amount_X - 1

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
    critical_X_amount = math.ceil(READ_LENGTH * CRITIAL_PROCENTAGE)
    string = read.seq[::-1]
    '''print string'''

    global_amount_N = 0
    local_amount_X = 0.0
    local_amount_A = 0.0
    score_A_line = []

    for i in range (len(string)):

        global_amount_N = global_amount_N + 1

        if (string[i] == "A"):
            local_amount_A = local_amount_A + 1
        else:
            local_amount_X = local_amount_X + 1

        if (local_amount_X > critical_X_amount):
            i = i - 2
            break

        '''print string[: i + 1], string[i], local_amount_X, i'''

        score_A_line.append(local_amount_A/global_amount_N)

    while (i != 0):
        if (string[i] != "A"):

            i = i - 1
            score_A_line.pop()
            global_amount_N = global_amount_N - 1
            local_amount_X = local_amount_X - 1

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


def cut_tail(read, typ):

    if (typ == "T"):
        tail_T = get_T_tail(read)
        if (tail_T.index >= MIN_TAIL_LENGTH - 1):
            read.seq = read.seq[tail_T.index + 1 : ]
            read.qual = read.qual[tail_T.index + 1 : ]


    if (typ == "A"):
        tail_A = get_A_tail(read)
        '''print read.name, tail_A.index, tail_A.score, read.seq[ : tail_A.index]'''
        if ((len(read.seq) - tail_A.index) >= MIN_TAIL_LENGTH - 1):
            print read.name
            read.seq = read.seq[ : tail_A.index]
            read.qual = read.qual[ : tail_A.index]

    return read
"""Opening files"""""""""""""""""""""""""""""""""""""""""""""""""""""""""


fd_data = open(file_name_data, "rb")
fd_cut = open(file_name_cut, "wb")
fd_uncut = open(file_name_uncut, "wb")


"""Main body"""""""""""""""""""""""""""""""""""""""""""""""""""""""""


curent_read = Read("", "", "", "")


while(True):

    curent_read = get_read(curent_read)
    if (curent_read.qual == ""):
        break

    curent_read = cut_tail(curent_read, TAIL_TYPE)

    if (len(curent_read.seq) == READ_LENGTH):
        put_read_uncut(curent_read)
    else:
        put_read_cut(curent_read)


"""Closing files"""""""""""""""""""""""""""""""""""""""""""""""""""""""""


fd_data.close()
fd_cut.close()
fd_uncut.close()


"""Terminating"""""""""""""""""""""""""""""""""""""""""""""""""""""""""


print "End\t", file_name_cut, "\t", file_name_uncut







