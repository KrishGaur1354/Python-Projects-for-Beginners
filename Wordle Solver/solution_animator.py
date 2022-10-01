def wordle(attempt, word):
	out=[]
	for i in range(5):
		if attempt[i]==word[i]:
			out.append('g')
		elif attempt[i] in word:
			out.append('y')
		else:
			out.append('b')
	return(out)
 
with open("5lw.txt", "r") as tf:
    wordlist = tf.read().split('\n')

def run(word,hint):

	for x in range(5):
		y=hint[x]
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



def listgen(finalword,startingword):
	x=[]
	b=0
	for c in range(6):
		hint=wordle(startingword,finalword)
		a=[startingword,hint]
		if startingword==finalword:
			b=b+1
			if b>1:
				a=['ㅤㅤㅤㅤㅤ',['b','b','b','b','b']]
		x.append(a)
		run(startingword,hint)
		startingword=wordlist[0]
	return(x)
from manim import *

out_list=listgen('ulcer','crane')
print(out_list)
class tab(Scene):
    def construct(self):
    	a=list(out_list[0][0].upper())
    	b=list(out_list[1][0].upper())
    	c=list(out_list[2][0].upper())
    	d=list(out_list[3][0].upper())
    	e=list(out_list[4][0].upper())
    	f=list(out_list[5][0].upper())        
    	t0 = Table([a,b,c,d,e,f],include_outer_lines = True,h_buff=0.6,v_buff=0.8)

    	#t0.add_highlighted_cell((2,2), color=GREEN)
    	
    	t0.scale(0.7)
    	title=Text("Wordle Solver", font_size=40, color=WHITE)
    	self.add(title)
    	title.next_to(t0, UP, buff=0.5)

    	self.play(t0.create(), run_time = 1)
    	
    	for y in range(6):
    		for x in range(5):
    			if out_list[y][1][x]=='g':
    				t0.add_highlighted_cell((y+1,x+1), color=GREEN)
    			if out_list[y][1][x]=='y':
    				t0.add_highlighted_cell((y+1,x+1), color=YELLOW)
    			print(x,y)
    			self.play(Transform(t0,t0),run_time = 0.1)
    	self.wait(5)



