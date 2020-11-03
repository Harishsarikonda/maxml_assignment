

def smallestSubString(strr): 
	
	n = len(strr) 
	dist_char=[]
	for i in strr:
		if i not in dist_char:
			dist_char.append(i)
	dist_count=len(dist_char)
	#print(dist_char,dist_count)
	
	char_count={}
	count = 0
	start = 0
	min_len = n 
	
	for i in range(n): 
		if strr[i] not in char_count:
			char_count[strr[i]]=1
		else:
		    char_count[strr[i]] += 1
		
		if char_count[strr[i]] == 1: 
			count += 1
			
		
		if count == dist_count: 
			while char_count[strr[start]] > 1: 
				if char_count[strr[start]] > 1: 
					char_count[strr[start]] -= 1
					
				start += 1
				
			string_length = i - start + 1
			
			if min_len > string_length: 
				min_len = string_length 
				starting_index = start 

	return str(strr[starting_index: starting_index + min_len]),min_len
						
	
print("Smallest substring containing "
		"maximum distinct characters is: ",end="") 
substring,min_len=smallestSubString("aabcc")
print(substring,end=" ")
print("and length is ",end="")
print(min_len)

