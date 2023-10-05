# @Kunalbhatia-Hub


from sys import stdin

def highestOccuringChar(stri) :
	#Your code goes here

	string = list(stri)
	string.sort()

	store={}
	ans=""
	cnt=0

	for i in range(len(string)):
        
		if string[i] in store:
			store[string[i]] += 1
        
		else:
			store[string[i]] = 1
 
        
		if cnt < store[string[i]]:
			ans = string[i]
			cnt = store[string[i]]
	
	return ans


# @Kunalbhatia-Hub