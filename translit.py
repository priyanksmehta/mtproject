from maps import CONSONANTS, VOWELS
import re

class Transliterate:

	def __init__(self):
		self.schwa = 'a'

	def romanize(self, hindi_text):
		english_text = []
		for letter in hindi_text.split(' '):
			if letter in CONSONANTS.keys():
				english_text.append(CONSONANTS[letter])
				english_text += self.schwa
			elif letter in VOWELS.keys():
				english_text.pop()
				english_text.append(VOWELS[letter])
			else:
				english_text = english_text[:-1]
		if english_text[-1] == 'a':
			return english_text[:-1]
		else:
			return ''.join(english_text)

#Usage
if __name__ == '__main__':
	test = Transliterate()
	sent = input("Enter Hindi text:\n")
	print(test.romanize(sent))