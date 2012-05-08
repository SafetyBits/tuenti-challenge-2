#!/usr/bin/python
# I recommend using "PyPy" instead, it's a lot faster on algorithmic code

import sys, multiprocessing


def is_malware(d, safe_list, malware_list):
	distance_malware = len(d['syscalls']) # max distance, like infinity
	distance_safe = len(d['syscalls']) # max distance, like infinity
	# We'll just search if the closest pattern is a known virus or a known safe program.
	# The closest pattern is the minnimum "sum of square differences"
	for safe in safe_list:
		distance = 0
		for d_sys, s_sys in zip(d['relative_syscalls'], safe['relative_syscalls']):
			distance += (d_sys - s_sys) ** 2
		if distance < distance_safe:
			distance_safe = distance
	for malware in malware_list:
		distance = 0
		for d_sys, m_sys in zip(d['relative_syscalls'], malware['relative_syscalls']):
			distance += (d_sys - m_sys) ** 2
		if distance < distance_malware:
			distance_malware = distance
	#print distance_malware, distance_safe
	return distance_malware < distance_safe


def parse_input():
	data = dict()
	input_dump = open("input.txt", "w")
	
	line = sys.stdin.readline()
	input_dump.write(line)
	data['n_known'] = int(line)
	data['safe'] = []
	data['malware'] = []
	line = sys.stdin.readline()
	input_dump.write(line)
	data['n_unknown'] = int(line)
	data['unknown'] = []
	line = sys.stdin.readline()
	input_dump.write(line)
	data['n_syscalls'] = int(line)
	
	for line in sys.stdin:
		input_dump.write(line)
		d = dict()
		syscalls = line.split()
		
		which = "unknown"
		if syscalls[0] == "S":
			syscalls.pop(0)
			which = "safe"
		elif syscalls[0] == "M":
			syscalls.pop(0)
			which = "malware"
		
		d['syscalls'] = map(int, syscalls)
		
		d['total_syscalls'] = sum(d['syscalls'])
		d['relative_syscalls'] = map(lambda x: x/float(d['total_syscalls']), d['syscalls'])

		data[which].append(d)
	input_dump.close()
	return data


if __name__ == '__main__':
	data = parse_input()
	r = 0
	for n, d in enumerate(data['unknown']):
		if is_malware(d, data['safe'], data['malware']):
			r += d['total_syscalls']
	print(str(r))
