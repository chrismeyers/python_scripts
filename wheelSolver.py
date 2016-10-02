#! /usr/bin/env python3

"""
Wheel of Fortune solver.
"""

import sys
import re
import curses

def parse_puzzle():
	puzzle_words = puzzle.split(" ")
	matched_words = []

	for word in puzzle_words:
		temp_words = []
		re_word = word.replace("-", "[a-z]")

		'''
		# Added words to enable1.txt
		#       1 a
		#   71841 i
		#  100986 o
		if len(word) == 1:
			if word != "-":
				temp_words.append(word)
				matched_words.append(temp_words)
			else:
				temp_words.append("a")
				temp_words.append("i")
				temp_words.append("o")
				matched_words.append(temp_words)
		else:'''
		for w in all_words:
			if len(w) == len(word):
				found = re.match(re_word, w)
				if found is not None:
					temp_words.append(found.group())
		matched_words.append(temp_words)

	return matched_words


def print_matches(matches):
	indent_char = ">"
	i = 1

	for words in matches:
		indent = indent_char * i
		for word in words:
			print(indent + " " + word)
		i += 1


def display_usage():
	print("Enter a puzzle.")

if __name__ == '__main__':
	puzzle = ""
	if len(sys.argv) >= 2:
		if len(sys.argv) == 2:
			# Enter puzzle string
			puzzle = sys.argv[1]
			words_file = '/Users/chris/Documents/Development/dailyprogrammer/resource/enable1.txt'
			with open(words_file, 'r') as f:
				all_words = {line for line in f.read().splitlines()}
			print_matches(parse_puzzle())
		else:
			# Interactive mode
			for i in range(1, len(sys.argv)):
				puzzle += "-" * int(sys.argv[i])
				if i != len(sys.argv) - 1:
					puzzle += " "
			print(puzzle)
	else:
		display_usage()
