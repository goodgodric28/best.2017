import sys

n = sys.argv[1]
f = sorted([int(i.strip()) for i in open(sys.argv[1])])
freq_distribution_sampling = int(sys.argv[2])
divide_by_three = sys.argv[3]

o = open(n[:-4]+str(freq_distribution_sampling)+'.txt','w')

if divide_by_three.upper() == "Y":
	for i in range(0,len(f),int(round(float(len(f))/freq_distribution_sampling))):
		o.write(str(f[i]/3)+'\n')
elif divide_by_three.upper() == "N":
        for i in range(0,len(f),int(round(float(len(f))/freq_distribution_sampling))):
                o.write(str(f[i])+'\n')

o.close()
