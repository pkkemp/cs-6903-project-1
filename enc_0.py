# CS-6903-Project-1

# This program contains the version of the encryption algorithm where we don't have any random chars.
# Once we figure out how to beat this then we can try the version with the random chars.

import string
import random

message_candidates = [
'cabooses meltdowns bigmouth makework flippest neutralizers gipped mule antithetical imperials carom masochism stair retsina dullness adeste corsage saraband promenaders gestational mansuetude fig redress pregame borshts pardoner reforges refutations calendal moaning doggerel dendrology governs ribonucleic circumscriptions reassimilating machinize rebuilding mezcal fluoresced antepenults blacksmith constance furores chroniclers overlie hoers jabbing resigner quartics polishers mallow hovelling ch', 
'biorhythmic personalizing abjure greets rewashed thruput kashmir chores fiendishly combatting alliums lolly milder postpaid larry annuli codgers apostatizing scrim carillon rust grimly lignifying lycanthrope samisen founds millimeters pentagon humidification checkup hilts agonise crumbs rejected kangaroo forenoons grazable acidy duellist potent recyclability capture memorized psalmed meters decline deduced after oversolicitousness demoralizers ologist conscript cronyisms melodized girdles nonago', 
'hermitage rejoices oxgall bloodstone fisticuff huguenot janitress assailed eggcup jerseyites fetas leipzig copiers pushiness fesse precociously modules navigates gaiters caldrons lisp humbly datum recite haphazardly dispassion calculability circularization intangibles impressionist jaggy ascribable overseen copses devolvement permutationists potations linesmen hematic fowler pridefully inversive malthus remainders multiplex petty hymnaries cubby donne ohioans avenues reverts glide photos antiaci', 
'leonardo oxygenate cascade fashion fortifiers annelids co intimates cads expanse rusting quashing julienne hydrothermal defunctive permeation sabines hurries precalculates discourteously fooling pestles pellucid circlers hampshirites punchiest extremist cottonwood dadoes identifiers retail gyrations dusked opportunities ictus misjudge neighborly aulder larges predestinate bandstand angling billet drawbridge pantomimes propelled leaned gerontologists candying ingestive museum chlorites maryland s', 
'undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics foetor subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis'
]

alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# A pseudocode description of the encryption algorithm could go as follows:
# Input: key k=k[1],...,k[t] and message m=m[1],...,m[L]
# Instructions: i=1 num_added_characters=0 
# Repeat let j = Scheduling_Algorithm(i,t,L) if 1<= j <=t then set
# c[i] = character obtained by shifting m[i] by k[j] positions (forward on the cycle {,a,..,z})
# if j<1 or j>t then randomly choose a character c from {,a,..,z} set c[i] = c 
# num_added_characters = num_added_characters + 1
# for h = L + added_characters downto i+1 set m[h] = m[h-1] i = i +1
# Until i > L + num_added_characters Return c[1]...c[L + num_added_characters]

def scheduling_algo(i, t, L):
	return i % t

def main():

	message = random.choice(message_candidates) # choose one of the five message candidates
	print(message)

	m = list(message) # split the message into a list of characters
	L = len(m)
	for i in range(L): # change all the letters to numbers 1-26
		if m[i] == ' ': # change spaces to 0
			m[i] = 0 
		else:
			m[i] = string.ascii_lowercase.index(m[i]) + 1

	key = "happyhappyhappy"
	#key = input("Enter key: ") # get key from user (should be a single word)
	k = list(key) # split the key into a list of letters
	t = len(k)
	for i in range(t): # change all the letters to numbers 1-26
		k[i] = string.ascii_lowercase.index(k[i]) + 1 # a = 1, z = 26

	num_added_chars = 0 # initialize num_added_chars 
	c = []

	# Getting the ciphertext into c

	for i in range(L):
	#while i < (L + num_added_chars): # this was what was in the "pseudocode" but doesn't make sense
		j = scheduling_algo(i, t, L)

		#if j >= 0 and j < t: # if the outputted value from the scheduling algo is within the key
		cipher = m[i] + k[j]
		c.append(cipher)

		#else:
		#	cipher = random.choice(alphabet) # pick random letter or space
		#	c.append(cipher)
		#	num_added_chars += 1 

			# not sure if this is right
			# pseudocode says to interate over the range L + num_added_chars
			# but that would go out of bounds
			# I think we're okay since instead of matching c[i] to m[i]
			# we're just appending the extra chars to c
			# essentially this means that as soon as we hit the first random value
			# the rest of the ciphertext is just random values 
			# because we're updating the message to repeat that i that caused the random value
			# into the next index
		#	for h in range(L - 1, i + 1, -1): 
		#		m[h] = m[h-1]

	R = L #+ num_added_chars # R is length of ciphertext, which includes random chars

	for i in range(R):
		c[i] = c[i] % 27 # mod 27 here because the space is an extra character
		c[i] = alphabet[c[i]]

	ciphertext = ''.join(map(str, c)) # convert back from list of chars to string
	print(ciphertext) 


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
