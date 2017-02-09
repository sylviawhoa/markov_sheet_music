#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
import random
import datetime
import glob
import markov
import pickle

corpus = []
song = []

"Generate sheet music for a new song from a corpus of existing songs in abc format"


# get the list of filenames (abc files downloaded from http://www.norbeck.nu/abc/)
getdirs = []
dirs = ["hn201612/i/*.abc", "hn201612/s/*.abc"]
for dir1 in dirs:
	for filename in glob.iglob(dir1):
		getdirs += [filename]

# ex_filename = "hn201612/i/hnsong1.abc"
# parsing on file to extract songs and add them to corpus
for filename in getdirs:
	with open(filename) as f:
		lines = f.readlines()
		last = len(lines)
		for index, line in enumerate(lines):
			if (line.find("|") < 0 and index - 1 == last):
				# if the next line does not have pipes add song to corpus and then set song variable empty again
				corpus.append(song)
				song = []

			else:
				if line.find("|") > -1:
					# a line should be split on "|" and copied to the corpus if it has pipes
					sline = line.split("|")
					# add the list of measures to the song
					song += [x.strip("\r\n") for x in sline if len(x.strip("\r\n")) > 0]
					last = index

print "Training on {} songs...".format(len(corpus))

# MARKOV PART
# n-gram length for markov model
n = 1

model = markov.generate_model_from_token_lists(corpus, n)


# save pickle
with open('abc_markov.pickle', 'wb') as handle:
	pickle.dump(model, handle)


def nextword(word):
	return markov.generate(model, 3, seed=word, max_iterations=1)


def writesong(songlength, first):
	song = [first]
	for i in range(songlength):
		song += nextword(str(song[-1]))
	return song

# choose a random song length from list of song lengths in corpus
lengthofsong = random.choice([len(x) for x in corpus if len(x) > 10])
print "Song length will be {}".format(lengthofsong)


firstnote = markov.generate(model, n, max_iterations=3)[0]
# print "first note: {}".format(firstnote)

print "Here is the song in abc format:"
song = writesong(lengthofsong, firstnote)
dob = datetime.datetime.now().strftime('%H:%M')
print song

# make song file
songname = "my_songs/markov_song_{}.abc".format(dob)
print "\n\nYou can find the song in {}".format(songname)
lastpart = lengthofsong - lengthofsong%4

# hack to include dictionary at the beginning of every abc file
# will add a more sophisticated way to generate the values in the future
title = "Markov Song {}".format(dob)
songbeginning = ['X:1','T:' + title, 'R:song', 'C:Sylvia Naples', 'Z:id:hn-song-111', 'M:3/4', 'L:1/8', 'Q:1/4=120', 'K:G'
]
songbeginning = [x+"\n" for x in songbeginning]

# convert song to abc format and write to file
newsong = open(songname, 'w')
newsong.writelines(songbeginning)
for i in range(lastpart):
	newsong.write(" | ".join(song[i:i+3]) + "\n")
newsong.write(" | ".join(song[lastpart:lengthofsong]))


# to get a pdf of the file go to http://www.sessionlist.com/abctopdf
# will update to generate pdf as part of the code



