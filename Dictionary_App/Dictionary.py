import json
from difflib import get_close_matches
from tkinter import *
from tkinter import messagebox
import threading
import os.path
import dload
import urllib.request
root = Tk()
root.title("DictionaryApp[BETA]")
root.geometry("700x300")
root.configure(bg="black")
messagebox.showinfo("Hello There!","Welcome to DictionaryApp[BETA]\nPlease click on ConnectToService to get started!")
root.update_idletasks()
global my_input
my_input = Entry(root, width=60, borderwidth=3)
my_input.insert(0, "Please enter a word")
my_input.pack()
root.update_idletasks()


def AboutUS():
    messagebox.showinfo("About Us","Developed by Mohit Chandak and Rutuj Runwal")

def connect():
	threading.Thread(target=lambda:NoFreezeConnect()).start()

def NoFreezeConnect():
	if(os.path.isfile("C:/ProgramData/WindowsData.json")):
		messagebox.showinfo("IntelliSense","You are already connected!\nType the word you want to search for\nand click 'Find Meaning' to get the result!")
	else:
		messagebox.showinfo("Started...","Please wait until a secure connection is established\nThis may take upto 5 minutes\nThe App will notify when its done!")
		dload.save('https://github.com/mohitchandak/Dictionary_App/raw/main/data.json','C:/ProgramData/WindowsData.json')#).start()
		messagebox.showinfo("","Done! You are good to go!")

def SearchWord():
	if(os.path.isfile("C:/ProgramData/WindowsData.json")):
		data = json.load(open("C:/ProgramData/WindowsData.json"))

		global my_word
		my_word = my_input.get()

		def translate(w):   
			w = w.lower()
			if w in data:
				return data[w]
			elif w.title() in data:
				return data[w.title()]
			elif w.upper() in data:
				return data[w.upper()]
			elif len(get_close_matches(w, data.keys())) > 0:
				print()
				decide = messagebox.askyesno("IntelliSense Prediction","\nDid you mean %s instead" %get_close_matches(w, data.keys())[0])
				if decide == 1:
					return data[get_close_matches(w, data.keys())[0]]
				elif decide != 1:
					return("Wrong word!")
				else:
					return("You have entered wrong input please enter just y or n: ")

		output = translate(my_word)
		if type(output) == list:
			messagebox.showinfo("Result","The Word Definiton is: " + output[0])
			if(len(output)>2):
				one_more = messagebox.askyesno("IntelliSense","More than one Definiton for "+ "'" + my_input.get() + "' "  +"Exists!\nDo you want to see the other one?")
				if(one_more==1):
					messagebox.showinfo("Result","The Word Definition is: "+output[1])
			user_msg =   messagebox.askyesno("Ask","Do you want to find another word?")	
			if(user_msg==1):
				my_input.delete(0,'end')
			else:
				messagebox.showinfo("Thank you!","Thank You for using our tool!")
				root.quit()

		else:
			print(output)
	else:
		messagebox.showinfo("IntelliSense Error!","Seems like you are launching the app for the 1st time!\nWelcome!!!\nPlease click on 'ConnectToService' to get started")



my_Btn_Cnt = Button(root,text = "ConnectToService",bg="blue",command=connect)
my_Btn_Cnt.pack()

my_Btn = Button(root,text="Find Meaning",bg="red",command=SearchWord) 
my_Btn.pack() 

my_Btn_Abt = Button(root,text="About Us",bg="teal",command=AboutUS) 
my_Btn_Abt.pack()

root.mainloop()
