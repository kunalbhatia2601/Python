# @Kunalbhatia-Hub


from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def getCompressedString(s) :
	
	i=0
	ans=""
	
	while i<len(s):
	    
		x=s[i]
	    
		j=i+1
		c=1
	    
		while j<len(s) and s[j]==x:
			j=j+1
			c=c+1
	    
		if c>1:
			ans+=s[i]+str(c)
	    
		else:
			ans+=s[i]
	    
		i=j
	
	return ans



# Main.
string = stdin.readline().strip();
ans = getCompressedString(string)
print(ans)


# @Kunalbhatia-Hub