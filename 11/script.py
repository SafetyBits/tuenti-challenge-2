#!/usr/bin/python
# I recommend using "PyPy" instead, it's a lot faster on algorithmic code

import sys, multiprocessing
import string
import copy

values = {1:"AEILNORSTU", 2:"DG", 3:"BCMP", 4:"FHVWY", 5:"K", 8:"JX", 10:"QZ"}
letter_values = dict()
for ch in string.ascii_uppercase:
	for k in values.keys():
		if ch in values[k]:
			letter_values[ch] = k
			break
longest_word = 24 # checked it offline
max_score = 56 # checked it offline
words = [[] for _ in xrange(max_score+1)]

# The real algorithm starts here:
def main(d):
	current_score = max_score + 1 # "infinity"
	max_len = len(d['rack']) + 1
	rack = dict()
	for ch in string.ascii_uppercase:
		rack[ch] = d['rack'].count(ch)
	while True:
		# The first valid ocurrence will be the best possible one
		current_score -= 1
		for pos in words[current_score]:
			if pos['len'] > max_len:
				continue # impossible with the number of letters in the rack
			for ch in d['word']:
				rack[ch] += 1 # add the table letter to the rack
				valid = True
				for k, v in pos['letters'].iteritems():
					if rack[k] < v: # not enough letters "k" in rack
						valid = False
						break
				if valid:
					return pos['word'] + " " + str(current_score)
				rack[ch] -= 1 # return the letter to the table
	

def read_words():
	all_words = open("descrambler_wordlist.txt").read().split('\n')
	if len(all_words[-1]) == 0: # last line is just a \n?
		all_words.pop()
	all_words = sorted(all_words) # God bless Python :) (btw, they are already sorted in the file)
	for word in all_words:
		score = 0
		letters = dict()
		for ch in word:
			score += letter_values[ch]
			if not ch in letters:
				letters[ch] = 1
			else:
				letters[ch] += 1
		words[score].append({'len': len(word), 'word': word, 'letters': letters})
		
	#print max(scores), min(scores) # max and min score
	#print max(map(len, all_words)) # longest word


def parse_input():
	# The input is parsed into a list of dictionaries, one for each test case
	data = []
	input_dump = open("input.txt", "w")
	line = sys.stdin.readline()
	input_dump.write(line)
	n = int(line)
	for line in sys.stdin:
		input_dump.write(line)
		d = dict()

		d['rack'], d['word'] = line.split("\n")[0].split()

		data.append(d)
	input_dump.close()
	return data


if __name__ == '__main__':
	data = parse_input()
	read_words()
	# Each test case shares a lot of global data, so no multiprocessing here.
	for n, d in enumerate(data):
		result = main(d)
		print(str(result))
