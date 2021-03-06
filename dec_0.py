# CS-6903-Project-1

import string
import numpy as np

message_candidates = [
'cabooses meltdowns bigmouth makework flippest neutralizers gipped mule antithetical imperials carom masochism stair retsina dullness adeste corsage saraband promenaders gestational mansuetude fig redress pregame borshts pardoner reforges refutations calendal moaning doggerel dendrology governs ribonucleic circumscriptions reassimilating machinize rebuilding mezcal fluoresced antepenults blacksmith constance furores chroniclers overlie hoers jabbing resigner quartics polishers mallow hovelling ch', 
'biorhythmic personalizing abjure greets rewashed thruput kashmir chores fiendishly combatting alliums lolly milder postpaid larry annuli codgers apostatizing scrim carillon rust grimly lignifying lycanthrope samisen founds millimeters pentagon humidification checkup hilts agonise crumbs rejected kangaroo forenoons grazable acidy duellist potent recyclability capture memorized psalmed meters decline deduced after oversolicitousness demoralizers ologist conscript cronyisms melodized girdles nonago', 
'hermitage rejoices oxgall bloodstone fisticuff huguenot janitress assailed eggcup jerseyites fetas leipzig copiers pushiness fesse precociously modules navigates gaiters caldrons lisp humbly datum recite haphazardly dispassion calculability circularization intangibles impressionist jaggy ascribable overseen copses devolvement permutationists potations linesmen hematic fowler pridefully inversive malthus remainders multiplex petty hymnaries cubby donne ohioans avenues reverts glide photos antiaci', 
'leonardo oxygenate cascade fashion fortifiers annelids co intimates cads expanse rusting quashing julienne hydrothermal defunctive permeation sabines hurries precalculates discourteously fooling pestles pellucid circlers hampshirites punchiest extremist cottonwood dadoes identifiers retail gyrations dusked opportunities ictus misjudge neighborly aulder larges predestinate bandstand angling billet drawbridge pantomimes propelled leaned gerontologists candying ingestive museum chlorites maryland s', 
'undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics foetor subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis'
]

alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():

	ciphertext = input("Enter the ciphertext: ")
	c = list(ciphertext) # convert to list
	L = len(c) 

	# Convert list to numbers for easier handling
	for i in range(L): # change all the letters to numbers 1-26
		if c[i] == ' ': # change spaces to 0
			c[i] = 0 
		else:
			c[i] = string.ascii_lowercase.index(c[i]) + 1

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
	# We'll do that by 
	key_lengths = np.flip(np.argsort(num_matches))

	# Try the most likely key length
	t = key_lengths[0] # the most likely key length
	# print(key_lengths)

	# Do frequency analysis
	


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
