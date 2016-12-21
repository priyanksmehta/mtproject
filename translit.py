from maps import CONSONANTS, VOWELS
import re
class Transliterate:

	def __init__(self):
		self.schwa = 'a'

	#necessary?
	def _modify_schwa(self, inp, add = True):
		if add:
			inp += self.schwa
		else:
			inp = inp[:-1]

	def romanize(self, hindi_text):
		english_text = ''
		for letter in hindi_text:
			if letter in CONSONANTS.keys():
				english_text += CONSONANTS[letter]
				english_text += self.schwa
			elif letter in VOWELS.keys():
				english_text = english_text[:-1]
				english_text += VOWELS[letter]
			elif letter == ' ':
				continue
			else:
				english_text = english_text[:-1]
		if english_text[-1] == 'a':
			return english_text[:-1]
		else:
			return english_text
