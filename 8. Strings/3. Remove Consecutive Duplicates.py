# @Kunalbhatia-Hub    

from sys import stdin

def removeConsecutiveDuplicates(s) :
	
	i,j=0,0
	ans=""
    
	while(j<len(s)):
        
		if( s[i]==s[j] ):
			j+=1
            
		elif((s[j]!=s[i]) or (j==len(s)-1)):
			ans+=s[i]
            
			i=j
			j+=1
            
	ans+=s[j-1]
	return ans

# @Kunalbhatia-Hub    