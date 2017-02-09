import sys
import markov
import random
import pickle

"make the markov model"

file_name = sys.argv[1]

# n-gram length for markov model
n = 1

# build model
model = {}

lines = []
for line in open(file_name, 'r'):
	line = line.strip()
	words = line.split(' ')
	upper_words = []
	for word in words:
		upper_word = word.upper()
		# filter out non alpha but leave apostrophes
		for char in upper_word:
			if not char.isalpha() and char is not "'":
				upper_word = upper_word.replace(char, "")
		upper_words.append(upper_word)
	lines.append(upper_words)



model = markov.generate_model_from_token_lists(lines, n)

# save pickle
with open('abc_markov.pickle', 'wb') as handle:
	pickle.dump(model, handle)

print random.choice(model.keys())

# print model
print markov.generate(model, n, max_iterations=3)

def nextword(word):
	return markov.generate(model, n, seed=word, max_iterations=1)