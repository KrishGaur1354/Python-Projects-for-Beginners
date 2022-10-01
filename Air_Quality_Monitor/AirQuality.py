import requests
import json
from tkinter import *
from tkinter import messagebox
import webbrowser

# Created By: Rutuj Runwal (https://www.linkedin.com/in/rutuj-runwal/)

root = Tk()
root.title("Air Quality Testing App by Rutuj Runwal")
root.geometry("620x400")
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id())) 
messagebox.showinfo("Welcome Info","Welcome to AQI Tester by Rutuj Runwal\nRemember the higher the AQI value, the greater the level of air pollution and the greater the health concern.")
defaultbg = root.cget('bg')
root.update_idletasks()
global MyInput
global resultLabelCOLOR
global maxrow
maxrow=4
def callback(url):
    webbrowser.open_new(url)

def about():
	global label1
	label1 = Label(root,text="AQI Tester developed by Rutuj Runwal\nGuidelines Powered by: www.airnow.gov\nAir Quality Data by: aqicn.org")#,cursor='hand2')
	label1.grid(row=maxrow+1,column=1)
	label1.bind("<Button-1>", lambda e: callback("https://aqicn.org/here/#!gl!19.7514798!75.7138884"))

def detect():
	Nearurl = "http://api.airvisual.com/v2/nearest_city?key=4fe74c02-0b81-461f-920f-e2d29d67691b"
	res = requests.get(Nearurl)
	unload = json.loads(res.content)
	val = unload['data']['current']['pollution']['aqius']
	city_name = unload['data']['city']
	MyInput.delete(0,END)
	MyInput.insert(0,city_name)

	if val<=50 and val>=0:
		try:
			# resultLabelM.grid_forget()
			# resultLabelH.grid_forget()
			# resultLabelD.grid_forget()
			# resultLabelU.grid_forget()
			# resultLabelMAX.grid_forget()
			ErrorLabel.destroy()
			resultLabelCOLOR="green"
			root.configure(bg="green")
			MyInputL = Label(root,text="Enter City Name: ",pady=10,bg=resultLabelCOLOR,font=("Helvetica",14)).grid(row=0,column=0)
			resultLabelG = Label(root,text="Intelli Total: "+str(val),bg=resultLabelCOLOR,font=("Helvetica",20,'bold'))
			resultLabelG.configure(fg="white")
			resultLabelG.grid(row=maxrow+1,column=1)
		except (NameError,AttributeError):
			resultLabelCOLOR="green"
			root.configure(bg="green")
			MyInputL = Label(root,text="Enter City Name: ",pady=10,bg=resultLabelCOLOR,font=("Helvetica",14)).grid(row=0,column=0)
			resultLabelG = Label(root,text="Intelli Total: "+str(val),bg=resultLabelCOLOR,font=("Helvetica",20,'bold'))
			resultLabelG.configure(fg="white")
			resultLabelG.grid(row=maxrow+1,column=1)

	elif val>=51 and val<=100:
		try:
			# resultLabelG.grid_forget()
			# resultLabelH.grid_forget()
			# resultLabelD.grid_forget()
			# resultLabelU.grid_forget()
			# resultLabelMAX.grid_forget()
			ErrorLabel.destroy()
			resultLabelCOLOR="#ffde33"
			root.configure(bg=resultLabelCOLOR)
			MyInputL = Label(root,text="Enter City Name: ",pady=10,bg=resultLabelCOLOR,font=("Helvetica",14)).grid(row=0,column=0)
			resultLabelM = Label(root,text="Intelli Total: "+str(val),bg=resultLabelCOLOR,font=("Helvetica",20,'bold'))
			# resultLabelM.configure(fg="white")
			resultLabelM.grid(row=maxrow+1,column=1)
		except (NameError,AttributeError):
			resultLabelCOLOR="#ffde33"
			root.configure(bg=resultLabelCOLOR)
			MyInputL = Label(root,text="Enter City Name: ",pady=10,bg=resultLabelCOLOR,font=("Helvetica",14)).grid(row=0,column=0)
			resultLabelM = Label(root,text="Intelli Total: "+str(val),bg=resultLabelCOLOR,font=("Helvetica",20,'bold'))
			# resultLabelM.configure(fg="white")
			resultLabelM.grid(row=maxrow+1,column=1)
	elif val>=101 and val<=150:
		try:
			# resultLabelM.grid_forget()
			# resultLabelG.grid_forget()
			# resultLabelD.grid_forget()
			# resultLabelU.grid_forget()
			# resultLabelMAX.grid_forget()
			ErrorLabel.destroy()
			resultLabelCOLOR="#ff9933"
			root.configure(bg=resultLabelCOLOR)
			MyInputL = Label(root,text="Enter City Name: ",pady=10,bg=resultLabelCOLOR,font=("Helvetica",14)).grid(row=0,column=0)
			resultLabelH = Label(root,text="Intelli Total: "+str(val),bg=resultLabelCOLOR,font=("Helvetica",20,'bold'))
			# resultLabelH.configure(fg="white")
			resultLabelH.grid(row=maxrow+1,column=1)
		except (NameError,AttributeError):
			resultLabelCOLOR="#ff9933"
			root.configure(bg=resultLabelCOLOR)
			MyInputL = Label(root,text="Enter City Name: ",pady=10,bg=resultLabelCOLOR,font=("Helvetica",14)).grid(row=0,column=0)
			resultLabelH = Label(root,text="Intelli Total: "+str(val),bg=resultLabelCOLOR,font=("Helvetica",20,'bold'))
			# resultLabelH.configure(fg="white")
			resultLabelH.grid(row=maxrow+1,column=1)
	elif val>=151 and val<=200:
		try:
			# resultLabelM.grid_forget()
			# resultLabelH.grid_forget()
			# resultLabelD.grid_forget()
			# resultLabelG.grid_forget()
			# resultLabelMAX.grid_forget()
			ErrorLabel.destroy()
			resultLabelCOLOR="#cc0033"
			root.configure(bg=resultLabelCOLOR)
			MyInputL = Label(root,text="Enter City Name: ",pady=10,bg=resultLabelCOLOR,font=("Helvetica",14)).grid(row=0,column=0)
			resultLabelU = Label(root,text="Intelli Total: "+str(val),bg=resultLabelCOLOR,font=("Helvetica",20,'bold'))
			# resultLabelU.configure(fg="white")
			resultLabelU.grid(row=maxrow+1,column=1)
		except (NameError,AttributeError):
			resultLabelCOLOR="#cc0033"
			root.configure(bg=resultLabelCOLOR)
			MyInputL = Label(root,text="Enter City Name: ",pady=10,bg=resultLabelCOLOR,font=("Helvetica",14)).grid(row=0,column=0)
			resultLabelU = Label(root,text="Intelli Total: "+str(val),bg=resultLabelCOLOR,font=("Helvetica",20,'bold'))
			# resultLabelU.configure(fg="white")
			resultLabelU.grid(row=maxrow+1,column=1)
	elif val>=201 and val<=290:
		try:
			# resultLabelM.grid_forget()
			# resultLabelH.grid_forget()
			# resultLabelG.grid_forget()
			# resultLabelU.grid_forget()
			# resultLabelMAX.grid_forget()
			ErrorLabel.destroy()
			resultLabelCOLOR="#660099"
			root.configure(bg=resultLabelCOLOR)
			MyInputL = Label(root,text="Enter City Name: ",pady=10,bg=resultLabelCOLOR,font=("Helvetica",14)).grid(row=0,column=0)
			resultLabelD = Label(root,text="Intelli Total: "+str(val),bg=resultLabelCOLOR,font=("Helvetica",20,'bold'))
			# resultLabelD.configure(fg="white")
			resultLabelD.grid(row=maxrow+1,column=1)
		except (NameError,AttributeError):
			resultLabelCOLOR="#660099"
			root.configure(bg=resultLabelCOLOR)
			MyInputL = Label(root,text="Enter City Name: ",pady=10,bg=resultLabelCOLOR,font=("Helvetica",14)).grid(row=0,column=0)
			resultLabelD = Label(root,text="Intelli Total: "+str(val),bg=resultLabelCOLOR,font=("Helvetica",20,'bold'))
			# resultLabelD.configure(fg="white")
			resultLabelD.grid(row=maxrow+1,column=1)

def chk():
	try:

		url = "https://api.waqi.info/feed/"+MyInput.get().lower()+"/?token=09962c1686db104e9dfe63c37794fb8dfc03fb73"
		res = requests.get(url)
		global ErrorLabel
		unload = json.loads(res.content)
		if unload['status'] =='error' or unload['data']=='Unknown station':

			try:
				ErrorLabel.destroy()
				root.configure(bg=defaultbg)
				MyInputL = Label(root,text="Enter City Name: ",pady=10,font=("Helvetica",14)).grid(row=0,column=0)
				ErrorLabel = Label(root,text="Location Data Unavailable",font=("Helvetica",20))
				ErrorLabel.grid(row=maxrow+1,column=1)
			except:
				root.configure(bg=defaultbg)
				MyInputL = Label(root,text="Enter City Name: ",pady=10,font=("Helvetica",14)).grid(row=0,column=0)
				ErrorLabel = Label(root,text="Location Data Unavailable",font=("Helvetica",20))
				ErrorLabel.grid(row=maxrow+1,column=1)

		else:
			city_name = unload['data']['city']['name'].split(',')[1]
			pm10_data = unload['data']['forecast']['daily']['pm10']
			ozone_data = unload['data']['forecast']['daily']['o3']
			pm25_data = unload['data']['forecast']['daily']['pm25']
			uv_data = unload['data']['forecast']['daily']['uvi']
			aqi = unload['data']['aqi']

			total = aqi

			# try:
			# 	global total_intelligence
			# 	intelli_data = unload['data']['iaqi']
			# 	intelli_data_co2 = intelli_data['co']['v']
			# 	intelli_data_so2 = intelli_data['so2']['v']
			# 	intelli_data_no2 = intelli_data['no2']['v']
			# 	intelli_data_o3 = intelli_data['o3']['v']
			# 	intelli_data_pm10 = intelli_data['pm10']['v']
			# 	total_intelligence = intelli_data_co2+intelli_data_pm10+intelli_data_o3+intelli_data_no2+intelli_data_so2

			# except KeyError:
			# 	# Default===100
			# 	intelli_data = unload['data']['iaqi']
			# 	intelli_data_co2 = 8
			# 	intelli_data_so2 = 2
			# 	intelli_data_no2 = 10
			# 	intelli_data_o3 = 30
			# 	intelli_data_pm10 = 50
			# 	# print("Real Time Data is: ",total_intelligence)

			global val
			val = round(aqi)			
			# print("Total: "+str(total))
			if val<=50 and val>=0:
				try:
					# resultLabelM.grid_forget()
					# resultLabelH.grid_forget()
					# resultLabelD.grid_forget()
					# resultLabelU.grid_forget()
					# resultLabelMAX.grid_forget()
					ErrorLabel.destroy()
					resultLabelCOLOR="green"
					root.configure(bg="green")
					MyInputL = Label(root,text="Enter City Name: ",pady=10,bg=resultLabelCOLOR,font=("Helvetica",14)).grid(row=0,column=0)
					resultLabelG = Label(root,text="Intelli Total: "+str(val),bg=resultLabelCOLOR,font=("Helvetica",20,'bold'))
					# resultLabelG.configure(fg="white")
					resultLabelG.grid(row=maxrow+1,column=1)
				except (NameError,AttributeError):
					resultLabelCOLOR="green"
					root.configure(bg="green")
					MyInputL = Label(root,text="Enter City Name: ",pady=10,bg=resultLabelCOLOR,font=("Helvetica",14)).grid(row=0,column=0)
					resultLabelG = Label(root,text="Intelli Total: "+str(val),bg=resultLabelCOLOR,font=("Helvetica",20,'bold'))
					# resultLabelG.configure(fg="white")
					resultLabelG.grid(row=maxrow+1,column=1)

			elif val>=51 and val<=100:
				try:
					# resultLabelG.grid_forget()
					# resultLabelH.grid_forget()
					# resultLabelD.grid_forget()
					# resultLabelU.grid_forget()
					# resultLabelMAX.grid_forget()
					ErrorLabel.destroy()
					resultLabelCOLOR="#ffde33"
					root.configure(bg=resultLabelCOLOR)
					MyInputL = Label(root,text="Enter City Name: ",pady=10,bg=resultLabelCOLOR,font=("Helvetica",14)).grid(row=0,column=0)
					resultLabelM = Label(root,text="Intelli Total: "+str(val),bg=resultLabelCOLOR,font=("Helvetica",20,'bold'))
					# resultLabelM.configure(fg="white")
					resultLabelM.grid(row=maxrow+1,column=1)
				except (NameError,AttributeError):
					resultLabelCOLOR="#ffde33"
					root.configure(bg=resultLabelCOLOR)
					MyInputL = Label(root,text="Enter City Name: ",pady=10,bg=resultLabelCOLOR,font=("Helvetica",14)).grid(row=0,column=0)
					resultLabelM = Label(root,text="Intelli Total: "+str(val),bg=resultLabelCOLOR,font=("Helvetica",20,'bold'))
					# resultLabelM.configure(fg="white")
					resultLabelM.grid(row=maxrow+1,column=1)
			elif val>=101 and val<=150:
				try:
					# resultLabelM.grid_forget()
					# resultLabelG.grid_forget()
					# resultLabelD.grid_forget()
					# resultLabelU.grid_forget()
					# resultLabelMAX.grid_forget()
					ErrorLabel.destroy()
					resultLabelCOLOR="#ff9933"
					root.configure(bg=resultLabelCOLOR)
					MyInputL = Label(root,text="Enter City Name: ",pady=10,bg=resultLabelCOLOR,font=("Helvetica",14)).grid(row=0,column=0)
					resultLabelH = Label(root,text="Intelli Total: "+str(val),bg=resultLabelCOLOR,font=("Helvetica",20,'bold'))
					# resultLabelH.configure(fg="white")
					resultLabelH.grid(row=maxrow+1,column=1)
				except (NameError,AttributeError):
					resultLabelCOLOR="#ff9933"
					root.configure(bg=resultLabelCOLOR)
					MyInputL = Label(root,text="Enter City Name: ",pady=10,bg=resultLabelCOLOR,font=("Helvetica",14)).grid(row=0,column=0)
					resultLabelH = Label(root,text="Intelli Total: "+str(val),bg=resultLabelCOLOR,font=("Helvetica",20,'bold'))
					# resultLabelH.configure(fg="white")
					resultLabelH.grid(row=maxrow+1,column=1)
			elif val>=151 and val<=200:
				try:
					# resultLabelM.grid_forget()
					# resultLabelH.grid_forget()
					# resultLabelD.grid_forget()
					# resultLabelG.grid_forget()
					# resultLabelMAX.grid_forget()
					ErrorLabel.destroy()
					resultLabelCOLOR="#cc0033"
					root.configure(bg=resultLabelCOLOR)
					MyInputL = Label(root,text="Enter City Name: ",pady=10,bg=resultLabelCOLOR,font=("Helvetica",14)).grid(row=0,column=0)
					resultLabelU = Label(root,text="Intelli Total: "+str(val),bg=resultLabelCOLOR,font=("Helvetica",20,'bold'))
					# resultLabelU.configure(fg="white")
					resultLabelU.grid(row=maxrow+1,column=1)
				except (NameError,AttributeError):
					resultLabelCOLOR="#cc0033"
					root.configure(bg=resultLabelCOLOR)
					MyInputL = Label(root,text="Enter City Name: ",pady=10,bg=resultLabelCOLOR,font=("Helvetica",14)).grid(row=0,column=0)
					resultLabelU = Label(root,text="Intelli Total: "+str(val),bg=resultLabelCOLOR,font=("Helvetica",20,'bold'))
					# resultLabelU.configure(fg="white")
					resultLabelU.grid(row=maxrow+1,column=1)
			elif val>=201 and val<=290:
				try:
					# resultLabelM.grid_forget()
					# resultLabelH.grid_forget()
					# resultLabelG.grid_forget()
					# resultLabelU.grid_forget()
					# resultLabelMAX.grid_forget()
					ErrorLabel.destroy()
					resultLabelCOLOR="#660099"
					root.configure(bg=resultLabelCOLOR)
					MyInputL = Label(root,text="Enter City Name: ",pady=10,bg=resultLabelCOLOR,font=("Helvetica",14)).grid(row=0,column=0)
					resultLabelD = Label(root,text="Intelli Total: "+str(val),bg=resultLabelCOLOR,font=("Helvetica",20,'bold'))
					# resultLabelD.configure(fg="white")
					resultLabelD.grid(row=maxrow+1,column=1)
				except (NameError,AttributeError):
					resultLabelCOLOR="#660099"
					root.configure(bg=resultLabelCOLOR)
					MyInputL = Label(root,text="Enter City Name: ",pady=10,bg=resultLabelCOLOR,font=("Helvetica",14)).grid(row=0,column=0)
					resultLabelD = Label(root,text="Intelli Total: "+str(val),bg=resultLabelCOLOR,font=("Helvetica",20,'bold'))
					# resultLabelD.configure(fg="white")
					resultLabelD.grid(row=maxrow+1,column=1)
			else:
				try:
					# resultLabelM.grid_forget()
					# resultLabelH.grid_forget()
					# resultLabelD.grid_forget()
					# resultLabelU.grid_forget()
					# resultLabelG.grid_forget()
					ErrorLabel.destroy()
					resultLabelCOLOR="#7e0023"
					root.configure(bg=resultLabelCOLOR)
					MyInputL = Label(root,text="Enter City Name: ",pady=10,bg=resultLabelCOLOR,font=("Helvetica",12)).grid(row=0,column=0)
					resultLabelMAX = Label(root,text="Intelli Total: "+str(val),bg=resultLabelCOLOR,font=("Helvetica",20,'bold'))
					# resultLabelMAX.configure(fg="white")
					resultLabelMAX.grid(row=maxrow+1,column=1)
				except (NameError,AttributeError):
					resultLabelCOLOR="#7e0023"
					root.configure(bg=resultLabelCOLOR)
					MyInputL = Label(root,text="Enter City Name: ",pady=10,bg=resultLabelCOLOR,font=("Helvetica",12)).grid(row=0,column=0)
					resultLabelMAX = Label(root,text="Intelli Total: "+str(val),bg=resultLabelCOLOR,font=("Helvetica",20,'bold'))
					# resultLabelMAX.configure(fg="white")
					resultLabelMAX.grid(row=maxrow+1,column=1)



	except(ConnectionError):  #, Exception):
		ErrorLabel = Label(root,text="Unable to Connect to server").grid(row=2,column=1)
	print(unload['data']['city'])

def guide():
	try:
		if val<=50 and val>=0:
				messagebox.showinfo("Guidelines","You Are Safe!")
		elif val>=51 and val<=100:
				messagebox.showinfo("Guidelines","In your zone Air quality is acceptable; Pollution in this range may pose a moderate health concern for a very small number of individuals.")
		elif val>=101 and val<=150:
				messagebox.showinfo("Guidelines","Air Quality falls in unhealthy indexing.")
		elif val>=151 and val<=200:
				messagebox.showinfo("Guidelines","Everyone may begin to experience health effects")
		elif val>=201 and val<=290:
				messagebox.showinfo("Guidelines","Serious Health Risks")
	except:
		messagebox.showinfo("Info","Guidelines Powered by: www.airnow.gov \nPlease Enter check your city status to get guidelines")

try:
	MyInputL = Label(root,text="Enter Name: ",pady=10,bg=resultLabelCOLOR,font=("Helvetica",12)).grid(row=0,column=0)
except NameError:
	MyInputL = Label(root,text="Enter City Name: ",pady=10,font=("Helvetica",12)).grid(row=0,column=0)
MyInput = Entry(root,width=60,borderwidth=3)
MyInput.grid(row=0,column=1)


my_Button = Button(root,text="Check Status",command=lambda: chk())
my_Button.grid(row=1,column=1)
my_Button_guide = Button(root,text="Check Guidelines",command=guide)
my_Button_guide.grid(row=2,column=1)
my_Button_about = Button(root,text="About",command=about)
my_Button_about.grid(row=4,column=1)
my_Button_Auto = Button(root,text="Detect Location",command=detect)
my_Button_Auto.grid(row=3,column=1)

root.update_idletasks()

root.mainloop()