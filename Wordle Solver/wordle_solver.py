print("b for observed black")
print("y for observed yellow")
print("g for observed green")

print("----------------------\n")
print("for example if you enter the word 'APPLE' and the 1st and 5th letters are green and 2nd and 3rd letters are yellow")
print("the observed hint would be gyybg\n\n")
def wordle(attempt, word):
	out=[]
	for i in range(5):
		if attempt[i]==word[i]:
			out.append(1)
		elif attempt[i] in word:
			out.append(0)
		else:
			out.append(-1)
	return(out)
 
with open("5lw.txt", "r") as tf:
    wordlist = tf.read().split('\n')

def run(word):
	for x in range(5):
		y=temp[x]
		letter=word[x]
		if y=='b':
			for i in wordlist[:]:
				if letter in i:
					wordlist.remove(i)
		if y=='g':
			for j in wordlist[:]:

				if letter in j:
					if j[x]==letter:
						pass
					else:
						wordlist.remove(j)
				else:
					wordlist.remove(j)
		if y=='y':
			for i in wordlist[:]:
				if letter not in i:
					wordlist.remove(i)
	print("------")
	print('pool count: ',len(wordlist))
	print('suggested word: ',wordlist[0])	
	print("------")
for l in range(6):
	temp=list(input("observed hint: "))
	if l==0:
		attempt=input("starting word: ")
	else:
		attempt=wordlist[0]
	for x in range(5):
		if attempt.count(attempt[x])>1:
			if temp[x]=='b':
				temp[x]='y'

	run(attempt)

