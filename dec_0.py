# CS-6903-Project-1

import string
import numpy as np
from collections import Counter

message_candidates = [
'cabooses meltdowns bigmouth makework flippest neutralizers gipped mule antithetical imperials carom masochism stair retsina dullness adeste corsage saraband promenaders gestational mansuetude fig redress pregame borshts pardoner reforges refutations calendal moaning doggerel dendrology governs ribonucleic circumscriptions reassimilating machinize rebuilding mezcal fluoresced antepenults blacksmith constance furores chroniclers overlie hoers jabbing resigner quartics polishers mallow hovelling ch', 
'biorhythmic personalizing abjure greets rewashed thruput kashmir chores fiendishly combatting alliums lolly milder postpaid larry annuli codgers apostatizing scrim carillon rust grimly lignifying lycanthrope samisen founds millimeters pentagon humidification checkup hilts agonise crumbs rejected kangaroo forenoons grazable acidy duellist potent recyclability capture memorized psalmed meters decline deduced after oversolicitousness demoralizers ologist conscript cronyisms melodized girdles nonago', 
'hermitage rejoices oxgall bloodstone fisticuff huguenot janitress assailed eggcup jerseyites fetas leipzig copiers pushiness fesse precociously modules navigates gaiters caldrons lisp humbly datum recite haphazardly dispassion calculability circularization intangibles impressionist jaggy ascribable overseen copses devolvement permutationists potations linesmen hematic fowler pridefully inversive malthus remainders multiplex petty hymnaries cubby donne ohioans avenues reverts glide photos antiaci', 
'leonardo oxygenate cascade fashion fortifiers annelids co intimates cads expanse rusting quashing julienne hydrothermal defunctive permeation sabines hurries precalculates discourteously fooling pestles pellucid circlers hampshirites punchiest extremist cottonwood dadoes identifiers retail gyrations dusked opportunities ictus misjudge neighborly aulder larges predestinate bandstand angling billet drawbridge pantomimes propelled leaned gerontologists candying ingestive museum chlorites maryland s', 
'undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics foetor subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis'
]

alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def convert_to_numbers(message):

	m = list(message)
	L = len(m)

	for i in range(L): # change all the letters to numbers 1-26
		if m[i] == ' ': # change spaces to 0
			m[i] = 0 
		else:
			m[i] = string.ascii_lowercase.index(m[i]) + 1
	return m

def frequency_analysis(m):

	#print(message)
	L = len(m)

	freq = [key for key, value in Counter(m).most_common()] # gives the list sorted in reverse order by frequency
	short_freq = freq[:6] # just take the top six 
	#print(short_freq)

	# ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
	# 5 20 1 15 9 14 19 8 18 4 12 3 21 13 23 6 7 25 16 2 22 11 10 24 17 26 
	english_freq = [5, 20, 1, 15, 9, 14, 19, 8, 18, 4, 12, 3, 21, 13, 23, 6, 7, 25, 16, 2, 22, 11, 10, 24, 17, 26]
	etaoin_freq = [5, 20, 1, 15, 9, 14]

	# Replace all instances of the first six numbers in freq with the numbers in etaoin_freq
	for i in range(L):
		if m[i] == short_freq[0]:
			m[i] = etaoin_freq[0]
		elif m[i] == short_freq[1]:
			m[i] = etaoin_freq[1]
		elif m[i] == short_freq[2]:
			m[i] = etaoin_freq[2]
		elif m[i] == short_freq[3]:
			m[i] = etaoin_freq[3]
		elif m[i] == short_freq[4]:
			m[i] = etaoin_freq[4]
		elif m[i] == short_freq[5]:
			m[i] = etaoin_freq[5]

	return m

def count_matches(t, L, c):

	substrings = [0]*t
	# Divide the ciphertext into t substrings
	for i in range(t):
		substrings[i] = c[slice(i, L, t)]	
	#print(substrings[0])
	#print(substrings)

	# Do frequency analysis on each substring
	updated_substrings = [0]*t
	for i in range(t):
		updated_substrings[i] = frequency_analysis(substrings[i])
	#print(updated_substrings)

	# Now reassemble the substrings into a single message
	new_text = [None]*L
	for i in range(t):
		new_text[i::t] = updated_substrings[i]
	#print(new_text)

	# Convert messages to numbers to compare
	m = []
	for message in message_candidates:
		m.append(convert_to_numbers(message))
	#print(m)
	#print(m[0])

	# Count how many matches we get with each message
	message_matches = [0]*5
	for i in range(5):
		matches_ctr = 0
		for j in range(500): # messages are all length 500
			if m[i][j] == new_text[j]:
				matches_ctr += 1
		message_matches[i] = matches_ctr
	#print(message_matches)

	# Return the array of message_matches
	return message_matches



def main():

	ciphertext = input("Enter the ciphertext: ")
	c = convert_to_numbers(ciphertext)
	L = len(c)

	# Try to find the key length by shifting the ciphertext 
	num_matches = [0]*25

	for i in range(1, 25): # Try out every possible shift (key length must be between 1 and 24)
		shifted_c = [0]*i + c 

		matching = 0
		for j in range(L): # Count all the matches between the orig and the shifted ciphertext
			if c[j] == shifted_c[j]:
				matching += 1

		num_matches[i] = matching

	# Now that the num_matches array is filled, 
	# get the index with the most matches.
	# That's the most likely key length value
	# We'll do that by creating an array that sorts the indices by the values, max to min
	# So the index with the most matches is at key_lengths[0],
	# the index with second most matches is at key_lengths[1], etc.
	key_lengths = np.flip(np.argsort(num_matches))
	#print(key_lengths)

	# First try the most likely key length 
	# This approach works well as long as key is between 7-11 letters (inclusive)
	
	t = key_lengths[0] # the most likely key length
	
	# Return the message with the most matches
	message_matches = count_matches(t, L, c)
	top_message = np.flip(np.argsort(message_matches))[0] # Gets the index of the message with the most matches

	# Trying multiple key lengths

	#t_candidates = key_lengths[:5] # Try the top five key lengths
	#m = [] # initialize array to hold the message_matches arrays in 

	# Do frequency analysis for each key length tried
	#for t in t_candidates:
	#	m.append(count_matches(t, L, c))
	
	#print(m)
	# Get the index of the max value in m
	# np.argmax gets us the index of the highest number in the array,
	# since it's zero-indexed we add 1
	# then we mod by 5 to tell us which of the 5 messages it was 
	#top_message = (np.argmax(m) + 1) % 5
	
	print("My plaintext guess is:", message_candidates[top_message])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
