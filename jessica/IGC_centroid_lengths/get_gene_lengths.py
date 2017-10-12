import sys

from Bio import SeqIO

results = []
# Requires a file to be specified after calling the script
IGC_file = sys.argv[1]

for i in SeqIO.parse(IGC_file,'fasta'):
	results.append(len(i.seq))

results = sorted(results)

o = open('gene_lengths_IGC_centroids.txt','w')

for i in results:
	o.write(str(i)+'\n')

o.close()
