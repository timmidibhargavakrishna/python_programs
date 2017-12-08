import re
string1=input()
string2=input()
for i in string1:
	if(re.search(string1,string2)):
		print(int(string1[i]),int(string1[i+1]))
		