from tkinter import *
from dbhelper import DBhelper
from tkinter import messagebox,filedialog
import random
from PIL import Image,ImageTk
import shutil,os


class quiz:
	def __init__(self):
		self.db=DBhelper()
		self.root=Tk()
		
		self.root.title("GK QUIZ")
		self.root.configure(background="#7D0552")
		self.root.geometry("1000x750")
		self.root.resizable(0,0)

		self.score=0
		self.skip_question=0
		self.right_answer=0
		self.wrong_answer=0
		
		self.load_gui()

	def load_gui(self,mode=0):
		if mode==1:
			self.clear(mode=1)
		else:
			self.clear()
		
		self.label1 = Label(self.root, text = 'QUIZ APP',fg = 'white',bg = '#7D0552')
		self.label1.configure(font = ('Algerian', 60,'bold'))
		self.label1.pack(pady = (5,20))

		self.label2 = Label(self.root, text = 'Email',fg = 'white',bg = '#7D0552')
		self.label2.configure(font = ('Times', 30,'italic'))
		self.label2.pack(pady = (20,20))

		self.email = Entry (self.root)
		self.email.pack(pady = (0,10),ipadx= 30,ipady = 5)
		self.email.focus()
		self.email.bind("<Return>",lambda event :self.password.focus())

		self.label3 = Label(self.root, text = 'Password',fg = 'white',bg = '#7D0552')
		self.label3.configure(font = ('Times', 30,'italic'))
		self.label3.pack(pady = (20,20))

		self.password = Entry (self.root)
		self.password.pack(pady = (0,10),ipadx= 30,ipady = 5)
		self.password.bind("<Return>",lambda event :self.btn_click())

		self.login = Button(self.root,text = 'Login',bg = 'white', command =lambda : self.btn_click())
		self.login.pack(pady=(20,20),ipadx=40,ipady = 4)

		self.label4=Label(self.root,text="Not a member? Sign Up",fg="white",bg="#7D0552")
		self.label4.configure(font=('Times', 15, 'italic'))
		self.label4.pack(pady=(20,20))

		self.register = Button(self.root, text='Sign Up', bg='white', command=lambda : self.register_gui())
		self.register.pack(pady=(10,20), ipadx=40, ipady=2)

		self.root.mainloop()

	def register_gui(self):
		self.clear()

		self.label0 = Label(self.root, text='QUIZ APP', fg='white', bg='#7D0552')
		self.label0.configure(font=('Algerian', 60, 'bold'))
		self.label0.grid(row=0,column=1,pady=(5,5))

		self.label1 = Label(self.root, text='Name', fg='white', bg='#7D0552')
		self.label1.configure(font=('Times', 30, 'italic'))
		self.label1.grid(row=1,column=0,pady=(10,10),sticky=E)

		self.name = Entry(self.root)
		self.name.grid(row=1,column=1,pady=(0, 10), ipadx=30, ipady=5)
		self.name.focus()
		self.name.bind("<Return>",lambda event :self.email.focus())

		self.label2 = Label(self.root, text='Email', fg='white', bg='#7D0552')
		self.label2.configure(font=('Times', 30, 'italic'))
		self.label2.grid(row=2,column=0,pady=(10,10),sticky=E)

		self.email = Entry(self.root)
		self.email.grid(row=2,column=1,pady=(0, 10), ipadx=30, ipady=5)
		self.email.bind("<Return>",lambda event :self.email_check())

		self.label3 = Label(self.root, text='Password', fg='white', bg='#7D0552')
		self.label3.configure(font=('Times', 30, 'italic'))
		self.label3.grid(row=3,column=0,pady=(10,10),sticky=E)

		self.password = Entry(self.root)
		self.password.grid(row=3,column=1,pady=(0, 10), ipadx=30, ipady=5)
		self.password.bind("<Return>",lambda event :self.confirm_password.focus())

		self.label4 = Label(self.root, text='Confirm Password', fg='white', bg='#7D0552')
		self.label4.configure(font=('Times', 30, 'italic'))
		self.label4.grid(row=4,column=0,pady=(10,10),sticky=E)

		self.confirm_password = Entry(self.root)
		self.confirm_password.grid(row=4,column=1,pady=(0, 10), ipadx=30, ipady=5)
		self.confirm_password.bind("<Return>",lambda event :self.reg_submit())

		self.filebtn=Button(self.root,text="Upload Profile Picture",command=lambda : self.upload_file())
		self.filebtn.grid(row=5,column=1,pady=(0, 5))

		self.filename=Label(self.root)
		self.filename.grid(row=5,column=2,pady=(0,5))

		self.register = Button(self.root, text='Sign Up', bg='white', command=lambda: self.reg_submit())
		self.register.grid(row=6,column=1,pady=(10,10), ipadx=40, ipady=4)

		self.label4 = Label(self.root, text="Already a member? Login", fg="white", bg="#7D0552")
		self.label4.configure(font=('Times', 15, 'italic'))
		self.label4.grid(row=7,column=1,pady=(10,10))

		self.login = Button(self.root, text='Login', bg='white', command=lambda: self.load_gui(mode=1))
		self.login.grid(row=8,column=1,pady=(10,10), ipadx=40, ipady=2)

	def email_check(self):
		email = self.email.get()
		data=self.db.check_login(email)
		if data==[]:
			self.password.focus()
		else:
			messagebox.showerror("Sorry","This Email is Already Exists ,Try with another Email")
			self.email.delete(0,END)
			lambda event :self.email.focus()

	def upload_file(self): 
		filename=filedialog.askopenfilename(initialdir="/images",title="Choose File")
		self.filename.configure(text=filename)

	def clear(self,mode=0):
		for i in self.root.pack_slaves():
			i.destroy()
		
		if mode==1:
			for i in self.root.grid_slaves():
				i.destroy()

	def btn_click(self):
		email = self.email.get()
		password = self.password.get()
		data = self.db.check_login(email,password=f"{password}")
		if len(data)>0:
			self.clear()
			self.user_id = data[0][0]
			self.user_data=data[0]
			self.main_window()
		else :
			messagebox.showerror("Error","Invalid Email/Password")
			self.email.delete(0,END)
			self.password.delete(0,END)
			self.email.focus()
	
	def reg_submit(self):
		name = self.name.get()
		email = self.email.get()
		password = self.password.get()
		confirm_password = self.confirm_password.get()
		filename=self.filename['text'].split("/")[-1]

		if name!="":
			if email!="":
				if password!="":
					if confirm_password!="":
						if confirm_password==password:
							if filename!="":
								data = self.db.check_login(email)
								if data==[]:
									response = self.db.insert_user(name,email, password,filename)
									if response == 1:
										messagebox.showinfo("Registration successful", 'You may Login now')
										if filename=="":
											shutil.copyfile(self.filename['text'],'C:\\Users\\admin\\PycharmProjects\\quizapp\\images\\'+ filename)
										self.load_gui(mode=1)
									else:
										messagebox.showerror('Error', 'Database Error')
								else:
									messagebox.showerror("Sorry","This Email is Already Exists ,Try with another Email")
									self.email.delete(0,END)
							else :
								messagebox.showerror("Sorry","Choose a photo first")
						else:
							messagebox.showerror("Sorry","Password not Matched")
					else:
						messagebox.showerror("Sorry","Confirm Your password first")
				else :
					messagebox.showerror("Sorry","Enter Your Password")
			else :
				messagebox.showerror("Sorry","Enter Your Email")
		else :
			messagebox.showerror("Sorry","Enter Your Name")

	def question_generate(self):
		self.question_no=[]
		while (len(self.question_no)<20):
			gen=random.randint(0,35)
			if gen not in self.question_no:
				self.question_no.append(gen)
			else:
				continue
		self.history_question_no=[]
		while (len(self.history_question_no)<20):
			gen=random.randint(0,42)
			if gen not in self.history_question_no:
				self.history_question_no.append(gen)
			else:
				continue
		
	def main_window(self,index=0, mode=0):
		if mode == 1:
			self.clear(mode=1)
		else:
			self.clear()

		self.question_generate()
		self.show_leaderboard()

		self.data=self.db.fetch_question()
		self.num=len(self.data)

		self.data1=self.db.fetch_historyquestion()
		self.num1=len(self.data1)

		self.score=0
		self.skip_question=0
		self.right_answer=0
		self.wrong_answer=0

		self.label1=Label(self.root,text="  WELCOME TO QUIZ APP ",fg="yellow",bg="#7D0552")
		self.label1.configure(font=("Algerian",50,"roman"))
		self.label1.grid(row=0,column=0,columnspan=3,pady=(20,20))

		imageURL="images/failure_to_success.png"
		load=Image.open(imageURL)
		load=load.resize((1000,400),Image.ANTIALIAS)
		render=ImageTk.PhotoImage(load)
		self.img=Label(image=render)
		self.img.image=render
		self.img.grid(row=1,column=0)

		
		self.frame1=Frame(self.root,bg="#7D0552")
		self.frame1.grid(row=2,column=0,pady=(5,5))

		self.human_quiz=Label(self.frame1,text="HUMAN BODY \t\t",fg="white",bg="#7D0552")
		self.human_quiz.config(font=("Times",35,"bold"))
		self.human_quiz.grid(row=0,column=0,pady=(10,10))
		
		self.click_to_start=Button(self.frame1,text="START",bg='white',command=lambda:self.show_question(self.data[self.question_no[index]],mode=1))
		self.click_to_start.config(font=("Times",20,"roman"))
		self.click_to_start.grid(row=0,column=1,pady=(10,20),ipadx=30,ipady=2)

		self.frame2=Frame(self.root,bg="#7D0552")
		self.frame2.grid(row=3,column=0,pady=(5,5))

		self.history_quiz=Label(self.frame2,text="HISTORY OF INDIA\t",fg="white",bg="#7D0552")
		self.history_quiz.config(font=("Times",35,"bold"))
		self.history_quiz.grid(row=0,column=0,pady=(10,10))

		self.click_to_start2=Button(self.frame2,text="START",bg='white',command=lambda:self.show_question(self.data1[self.history_question_no[index]],mode=2))
		self.click_to_start2.config(font=("Times",20,"roman"))
		self.click_to_start2.grid(row=0,column=1,pady=(10,20),ipadx=30,ipady=2)

		self.root.mainloop()

	def show_question(self,data,mode=0,index=0):
		self.label1.destroy()
		self.frame1.destroy()
		self.human_quiz.destroy()
		self.click_to_start.destroy()
		self.frame2.destroy()
		self.history_quiz.destroy()
		self.img.destroy()
		self.click_to_start2.destroy()


		self.radioVar=IntVar()
		self.radioVar.set(-1)

		if mode==1:
			self.label1=Label(self.root,text=f"{index+1} ." +"  " + data[1],fg="white",bg="#7D0552")
			self.label1.configure(font=("Times",30,"roman"),justify=CENTER,width=750,wraplength=750)
			self.label1.pack(pady=(20,20))

			self.frame1=Frame(self.root,bg="#7D0552")
			self.frame1.pack(pady=(20,20))

			self.option1=Radiobutton(self.frame1,text="(a)  " + data[2],fg="white",bg="#7D0552",variable=self.radioVar,value=1,command=lambda :self.show_question_func(index=index+1))
			self.option1.config(font=("Times",40,"roman"),justify=CENTER,anchor=W,width=750,wraplength=750)
			self.option1.pack(pady=(5,10))

			self.option2=Radiobutton(self.frame1,text="(b)  " + data[3],fg="white",bg="#7D0552",variable=self.radioVar,value=2,command=lambda :self.show_question_func(index=index+1))
			self.option2.config(font=("Times",40,"roman"),justify=CENTER,anchor=W,width=750,wraplength=750)
			self.option2.pack(pady=(5,10))
			
			self.option3=Radiobutton(self.frame1,text="(c)  " + data[4],fg="white",bg="#7D0552",variable=self.radioVar,value=3,command=lambda :self.show_question_func(index=index+1))
			self.option3.config(font=("Times",40,"roman"),justify=CENTER,anchor=W,width=750,wraplength=750)
			self.option3.pack(pady=(5,10))
			
			self.option4=Radiobutton(self.frame1,text="(d)  " + data[5],fg="white",bg="#7D0552",variable=self.radioVar,value=4,command=lambda :self.show_question_func(index=index+1))
			self.option4.config(font=("Times",40,"roman"),justify=CENTER,anchor=W,width=750,wraplength=750)
			self.option4.pack(pady=(5,10))

			self.frame2=Frame(self.root,bg="#7D0552")
			self.frame2.pack(pady=(20,20),side=BOTTOM)

			self.backbtn=Button(self.frame2,text="Home",fg="black",bg="white",command=lambda :self.main_window())
			self.backbtn.configure(font=("Times",15))
			self.backbtn.pack(pady=(10,10),ipadx=10,ipady=1,side='left')

			self.skipbtn=Button(self.frame2,text="Skip",fg="black",bg="white",command=lambda :self.show_question_func(index=index+1,skip=1))
			self.skipbtn.configure(font=("Times",15))
			self.skipbtn.pack(pady=(10,10),ipadx=10,ipady=1,side='left')


		if mode==2:
			self.label1=Label(self.root,text=f"{index+1} ." +"  " + data[1],fg="white",bg="#7D0552")
			self.label1.configure(font=("Times",30,"roman"),justify=CENTER,width=750,wraplength=750)
			self.label1.pack(pady=(20,20))

			self.frame1=Frame(self.root,bg="#7D0552")
			self.frame1.pack(pady=(20,0))

			self.option1=Radiobutton(self.frame1,text="(a)  " + data[2],fg="white",bg="#7D0552",variable=self.radioVar,value=1,command=lambda :self.show_history_question_func(index=index+1))
			self.option1.config(font=("Times",40,"roman"),justify=CENTER,anchor=W,width=750,wraplength=750)
			self.option1.pack()

			self.option2=Radiobutton(self.frame1,text="(b)  " + data[3],fg="white",bg="#7D0552",variable=self.radioVar,value=2,command=lambda :self.show_history_question_func(index=index+1))
			self.option2.config(font=("Times",40,"roman"),justify=CENTER,anchor=W,width=750,wraplength=750)
			self.option2.pack()
			
			self.option3=Radiobutton(self.frame1,text="(c)  " + data[4],fg="white",bg="#7D0552",variable=self.radioVar,value=3,command=lambda :self.show_history_question_func(index=index+1))
			self.option3.config(font=("Times",40,"roman"),justify=CENTER,anchor=W,width=750,wraplength=750)
			self.option3.pack()
			
			self.option4=Radiobutton(self.frame1,text="(d)  " + data[5],fg="white",bg="#7D0552",variable=self.radioVar,value=4,command=lambda :self.show_history_question_func(index=index+1))
			self.option4.config(font=("Times",40,"roman"),justify=CENTER,anchor=W,width=750,wraplength=750)
			self.option4.pack()

			self.frame2=Frame(self.root,bg="#7D0552")
			self.frame2.pack(pady=(20,20),side=BOTTOM)

			self.backbtn=Button(self.frame2,text="Home",fg="black",bg="white",command=lambda :self.main_window())
			self.backbtn.configure(font=("Times",15))
			self.backbtn.pack(pady=(10,10),ipadx=10,ipady=1,side='left')

			self.skipbtn=Button(self.frame2,text="Skip",fg="black",bg="white",command=lambda :self.show_history_question_func(index=index+1,skip=1))
			self.skipbtn.configure(font=("Times",15))
			self.skipbtn.pack(pady=(10,10),ipadx=10,ipady=1,side='left')
		
	def show_question_func(self,mode=1,index=0,skip=0):
		data=self.data
		var=self.radioVar.get()

		if skip!=1:
			if var==data[self.question_no[index-1]][6]:
				self.score+=10
				self.right_answer+=1
			else :
				self.score-=5
				self.wrong_answer+=1
		else:
			self.score+=0
			self.skip_question+=1

		if index!=20:
			self.show_question(data[self.question_no[index]],mode=1,index=index)
		else :
			if self.score>self.user_data[4]:
				self.insert_score(self.score)
			self.imageshown()

	def insert_score(self,score):
		self.db.update_score(self.user_id,score)
	
	def show_leaderboard(self):
		self.all_user_data=self.db.check_leaderboard()
	
	def show_history_question_func(self,mode=2,index=0,skip=0):
		data=self.data1
		var=self.radioVar.get()

		if skip!=1:
			if var==data[self.history_question_no[index-1]][6]:
				self.score+=10
				self.right_answer+=1
			else:
				self.score-=5
				self.wrong_answer+=1
		else:
			self.score+=0
			self.skip_question+=1
		
		if index!=20:
			self.show_question(data[self.history_question_no[index]],mode=2,index=index)
		else:
			if self.score>self.user_data[4]:
				self.insert_score(self.score)
			self.imageshown()
	
		 
	def imageshown(self):
		self.clear()
		
		if self.score>self.user_data[4]:
			imageURL="images/success.png"
		else:
			imageURL="images/failure.png"

		load=Image.open(imageURL)
		load=load.resize((800,400),Image.ANTIALIAS)
		render=ImageTk.PhotoImage(load)
		img=Label(image=render)
		img.image=render
		img.pack()

		self.label1=Label(self.root,text=f"Your Current Score is : {self.score}",fg="#33FFFA",bg="#7D0552")
		self.label1.config(font=("Times",25,"roman"))
		self.label1.pack(pady=(5,10))

		self.label1=Label(self.root,text=f"You give {self.right_answer} right, {self.wrong_answer} wrong answer, skipped {self.skip_question} Questions",fg="#33FFFA",bg="#7D0552")
		self.label1.config(font=("Times",25,"roman"))
		self.label1.pack(pady=(5,10))

		self.frame=Frame(self.root,bg="#7D0552")
		self.frame.pack(pady=(5,10))

		self.leaderboardbtn=Button(self.frame,text="See leaderboard",fg="black",bg="white",command=lambda :self.leaderboard())
		self.leaderboardbtn.configure(font=("Times",25))
		self.leaderboardbtn.pack(pady=(5,5),side="left")

		self.home=Button(self.frame,text="Play Again",fg="black",bg="white",command=lambda :self.main_window())
		self.home.configure(font=("Times",25))
		self.home.pack(pady=(5,5),side="left")

	def leaderboard(self):
		self.clear()

		self.dp(0,0,self.all_user_data[0][5])

		self.first=Label(self.root,text=f"  {self.all_user_data[0][1]},  Score :{self.all_user_data[0][4]}",fg="#33FFFA",bg="#7D0552")
		self.first.config(font=("Times",40,"roman"),anchor=W,width=750,wraplength=750)
		self.first.grid(row=0,column=1,pady=(10,50))

		self.dp(1,0,self.all_user_data[1][5])

		self.second=Label(self.root,text=f"  {self.all_user_data[1][1]},  Score :{self.all_user_data[1][4]}",fg="#33FFFA",bg="#7D0552")
		self.second.config(font=("Times",40,"roman"),anchor=W,width=750,wraplength=750)
		self.second.grid(row=1,column=1,pady=(10,50))

		self.dp(2,0,self.all_user_data[2][5])

		self.third=Label(self.root,text=f"  {self.all_user_data[2][1]},  Score :{self.all_user_data[2][4]}",fg="#33FFFA",bg="#7D0552")
		self.third.config(font=("Times",40,"roman"),anchor=W,width=750,wraplength=750)
		self.third.grid(row=2,column=1,pady=(10,50))

		self.dp(3,0,self.all_user_data[3][5])

		self.forth=Label(self.root,text=f"  {self.all_user_data[3][1]},  Score :{self.all_user_data[3][4]}",fg="#33FFFA",bg="#7D0552")
		self.forth.config(font=("Times",40,"roman"),anchor=W,width=750,wraplength=750)
		self.forth.grid(row=3,column=1,pady=(10,50))

		self.dp(4,0,self.all_user_data[4][5])

		self.fifth=Label(self.root,text=f"  {self.all_user_data[4][1]},  Score :{self.all_user_data[4][4]}",fg="#33FFFA",bg="#7D0552")
		self.fifth.config(font=("Times",40,"roman"),anchor=W,width=750,wraplength=750)
		self.fifth.grid(row=4,column=1,pady=(10,50))

		self.home=Button(self.root,text="Play Again",fg="black",bg="white",command=lambda :self.main_window(mode=1))
		self.home.configure(font=("Times",25))
		self.home.grid(row=5,column=0,pady=(5,5))

	def dp(self,row,column,dp):
		imageURL=f"images/{dp}"
		load=Image.open(imageURL)
		load=load.resize((60,60),Image.ANTIALIAS)
		render=ImageTk.PhotoImage(load)
		self.img=Label(image=render)
		self.img.image=render
		self.img.grid(row=f"{row}",column=f"{column}")
		
		
		
		
		
obj = quiz()