import tweepy
import tkinter
import numpy as np
from time import sleep
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

bibel = 'bibel.txt'
dracula = 'dracula.txt'
milton = 'milton.txt'
pride = 'prideandp.txt'
rummet = 'rummet.txt'
shakespeare = 'shakespeare.txt'

source = open(rummet, encoding='UTF-8').read()
corpus = source.split()

def make_pairs(text):
	for i in range(len(text) - 1):
		yield (corpus[i], text[i+1])
		
def create_text(corpus):
	pairs = make_pairs(corpus)
	dictionary = {}
	
	for word_1, word_2 in pairs:
		if word_1 in dictionary.keys():
			dictionary[word_1].append(word_2)
		else:
			dictionary[word_1] = [word_2]
	
	first_word = np.random.choice(corpus)
	while first_word.islower():
		first_word = np.random.choice(corpus)
		
	chain = [first_word]
	n_words = 40
	
	for i in range(n_words):
		chain.append(np.random.choice(dictionary[chain[-1]]))
	
	return ' '.join(chain)
	
def get_valid_tweet(corpus):
	str = create_text(corpus)
	while len(str) > 280:
		str = create_text(corpus)
		
	print(len(str))
	return str
	
def tweet():
	counter = 0
	while counter < 3:
		str = get_valid_tweet(corpus)
		print(str)
		counter += 1
		
		api.update_status(status=str)
		sleep(60)


tweet()
	
api.update_status(status=get_valid_tweet(corpus))
