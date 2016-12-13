"""

Problem: Complementing a Strand of DNA
ID: revc
URL: http://rosalind.info/problems/revc/
Solution author: Samael Olascoaga

"""

with open("file.txt", 'r') as chain:
	single_chain = chain.readlines()
	complementary = ""
	for chain in single_chain:
		for nucelotide in chain:
			if nucelotide == 'A':
				nucelotide = 'T'
				complementary += nucelotide
			elif nucelotide == 'C':
				nucelotide = 'G'
				complementary += nucelotide
			elif nucelotide == 'G':
				nucelotide = 'C'
				complementary += nucelotide
			elif nucelotide == 'T':
				nucelotide = 'A'
				complementary += nucelotide

reverse = complementary[::-1]
with open('solution.txt', 'a') as solution:
	solution.write(reverse)