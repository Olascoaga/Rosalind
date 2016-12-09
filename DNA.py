"""

Problem: Counting DNA Nucleotides
ID: DNA
URL: http://rosalind.info/problems/dna/
Solution author: Samael Olascoaga

"""
with open('file.txt', 'r') as file:
    nucelotide = file.readline()
    A = nucelotide.count("A")
    C = nucelotide.count("C")
    G = nucelotide.count("G")
    T = nucelotide.count("T")
    chain = "{0} {1} {2} {3}".format(A, C, G, T)
    solution = open("solutions.txt", 'a')
    solution.write(chain)
    solution.close()
