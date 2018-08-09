from collections import Counter, defaultdict
import time
start_time = time.time()

words = []
e_dict = open("e_dict.txt","r")
read = e_dict.readlines()
for i in range(len(read)):
	if len(read[i])>=8:
		words.append(read[i].rstrip('\n').lower())
ana = []
for i in range(len(words)):
	ana.append(["".join(sorted(words[i])), words[i]])
ana_dict = defaultdict(list)
for key, word in ana:
	ana_dict[key].append(word)
masterlist = []
for i in ana_dict.items():
	masterlist.append(i[1])
masterlist.sort(key=len)
counter = 0
register = open("register.txt","w")
for i in masterlist:
	if len(i)>1:
		register.write(str(i) + "\n")
#print(counter)
register.close()

for i in masterlist:  #Finds words that are mirrors of each other
	if len(i)>1:
		for j in i:
			if i[0] == j[::-1]:
				print(i[0],j)

print("--- %s seconds ---" % (time.time() - start_time))
