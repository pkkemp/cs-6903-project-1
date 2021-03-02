# CS-6903-Project-1


# A pseudocode description of the encryption algorithm could go as follows:
# Input: key k=k[1],...,k[t] and message m=m[1],...,m[L]
# Instructions: i=1 num_added_characters=0 Repeat let j = Scheduling_Algorithm(i,t,L) if 1<= j <=t then set
# c[i] = character obtained by shifting m[i] by k[j] positions (forward on the cycle {,a,..,z})
# if j<1 or j>t then randomly choose a character c from {,a,..,z} set c[i] = c num_added_characters = num_added_characters + 1
# for h = L + added_characters downto i+1 set m[h] = m[h-1] i = i +1
# Until i > L + num_added_characters Return c[1]...c[L + num_added_characters]

def main():
    print("hello world!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
