# @Kunalbhatia-Hub  


from sys import stdin

def reverseEachWord(string) :

	# return " ".join(word[::-1] for word in string.split())

	words = string.split(" ")

	newWords = [word[::-1] for word in words]

	newSentence = " ".join(newWords)
 	
	return newSentence


# @Kunalbhatia-Hub  