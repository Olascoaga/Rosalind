"""

Problem: Transcribing DNA into RNA
ID: RNA
URL: http://rosalind.info/problems/rna/
Solution author: Samael Olascoaga

"""

def dna_to_rna():
	with open('problem.txt') as dna_chain:
		dna = dna_chain.readline()
		rna = dna.replace("T", "U")
		with open('solution.txt', 'a') as solution:
			solution.write(rna)

dna_to_rna()
