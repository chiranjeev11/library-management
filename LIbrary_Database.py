import sqlite3 as sq3
from tkinter import *
from tkinter import ttk

connector = sq3.connect("app.db")
curs = connector.cursor()

try:
	curs.execute("""create table Student_Data(

					name varchar,
					roll_no integer UNIQUE,
					Mob_no integer,
					branch varchar,
					username varchar UNIQUE,
					password varchar,
					book_borrowed varchar

						);""")

	curs.execute("""create table Book_Data(

					book_id varchar NOT NULL UNIQUE,		
					book_name varchar,
					author_name varchar,
					Subject varchar NOT NULL,
					count integer





												);	""")

except:
	print("Table has already been created")
# curs.execute("insert into Student_Data(name, roll_no, Mob_no, branch) values();")

class Library():

	def __init__(self):
		
		self.Library_window = Tk()
		self.Library_window.title("Library")
		self.Library_window.geometry("1350x750+0+0")

		self.Mainframe = Frame(self.Library_window)
		self.Mainframe.grid()

		self.Titleframe = Frame(self.Mainframe, width = 1350, padx = 20, bd = 50, relief = RIDGE )
		self.Titleframe.pack(side=TOP)
		self.lbltitle = Label(self.Titleframe, width = 30, font = ( "arial", 52, "bold" ), text = "LIBRARY MANAGEMENT SYSTEM", padx = 20 )
		self.lbltitle.grid()




		b = Buttons(self.Library_window)

		self.Library_window.mainloop()






class Buttons():	


	def __init__(self, Library_window):
		
		self.Library_window = Library_window
		self.bt1 = Button(self.Library_window, text = "Login as Student", font = ( "arial", 20, "bold" ), width = 20, command=self.bt1_clicked).grid(column=0,row=4, padx = 12, pady = 12)
		self.bt2 = Button(self.Library_window, text = "Login as Admin",font = ( "arial", 20, "bold" ), width = 20, command=self.bt2_clicked).grid(column=0,row=8, padx = 12, pady = 12)
		self.bt3 = Button(self.Library_window, text = "Register",font = ( "arial", 20, "bold" ), width = 20,command=self.bt3_clicked).grid(column=0,row=12, padx = 12, pady = 12)



## Admin Page
## this page will include all the administration related options

	def bt2_clicked(self):
		
		self.Library_window.withdraw()
		self.admin_page = Toplevel(self.Library_window)
		self.admin_page.geometry("1350x750+0+0")

		self.Mainframe = Frame(self.admin_page)
		self.Mainframe.grid()

		self.Titleframe = Frame(self.Mainframe, width = 1350, padx = 20, bd = 50, relief = RIDGE )
		self.Titleframe.pack(side=TOP)
		self.lbltitle = Label(self.Titleframe, width = 30, font = ( "arial", 52, "bold" ), text = "ADMIN LOGIN", padx = 20 )
		self.lbltitle.grid()

		txt1 = Label(self.admin_page, text = "Username:", font = ("arial", 20, "bold" )).grid(column=0, row=2)
		self.Username = Entry(self.admin_page, width =20, borderwidth = 5, font = ("arial", 14))
		self.Username.grid(column=0, row=4, pady = 10)

		txt2 = Label(self.admin_page, text = "Password:", font = ("arial", 20, "bold" )).grid(column=0,row=6)
		self.Password = Entry(self.admin_page, text = "Password", width = 20, borderwidth = 5, font = ("arial", 14))
		self.Password.grid(column=0, row=8, pady = 10)

		bt = Button(self.admin_page, text = "ENTER", font = ("arial", 15, "bold"), command = self.enter_clicked).grid(column=0, row=10, pady = 10)

		btt = Button(self.admin_page, text = "BACK", font = ("arial", 15, "bold"), command = self.btt_back).grid(column = 0, row=11)
	

## Back to Admin Page

	def btt_back(self):

		self.admin_page.withdraw()
		self.Library_window = Toplevel(self.admin_page)
		self.Library_window.geometry("1350x750+0+0")

		self.Mainframe = Frame(self.Library_window)
		self.Mainframe.grid()

		self.Titleframe = Frame(self.Mainframe, width = 1350, padx = 20, bd = 50, relief = RIDGE )
		self.Titleframe.pack(side=TOP)
		self.lbltitle = Label(self.Titleframe, width = 30, font = ( "arial", 52, "bold" ), text = "LIBRARY MANAGEMENT SYSTEM", padx = 20 )
		self.lbltitle.grid()

		l =Buttons(self.Library_window)


## Student Login Page
## this page will include all the student login related optins

	def bt1_clicked(self):

		self.Library_window.withdraw()
		self.Login_page = Toplevel(self.Library_window)
		self.Login_page.geometry("1350x750+0+0")

		self.Mainframe = Frame(self.Login_page)
		self.Mainframe.grid()

		self.Titleframe = Frame(self.Mainframe, width = 1350, padx = 20, bd = 50, relief = RIDGE )
		self.Titleframe.pack(side=TOP)
		self.lbltitle = Label(self.Titleframe, width = 30, font = ( "arial", 52, "bold" ), text = "LOGIN", padx = 20 )
		self.lbltitle.grid()

		t1 = Label(self.Login_page, text = "Username:     " , font = ("arial", 20, "bold" )).grid(column=0, row=1)

		self.Username = Entry(self.Login_page, width = 25,  borderwidth = 5, font = ("arial", 14))
		self.Username.grid(column=0, row=2, pady = 10)

		t2 = Label(self.Login_page, text = "Password:       ",  font = ("arial", 20, "bold" )).grid(column=0,row=3)

		self.Password = Entry(self.Login_page, width = 25, borderwidth = 5 , font = ("arial", 14))
		self.Password.grid(column=0,row=4, pady = 20)

		b = Button(self.Login_page, text = "Submit", font = ("arial", 15, "bold"), command = self.b_clicked ).grid(column=0,row=5, pady = 10)

		btt2 = Button(self.Login_page, text = "BACK", font = ("arial", 15, "bold"), command = self.btt2_back ).grid(column = 0, row = 6)


## Back to Library Window 


	def btt2_back(self):

		self.Login_page.withdraw()
		self.Library_window = Toplevel(self.Login_page)
		self.Library_window.geometry("1350x750+0+0")

		self.Mainframe = Frame(self.Library_window)
		self.Mainframe.grid()

		self.Titleframe = Frame(self.Mainframe, width = 1350, padx = 20, bd = 50, relief = RIDGE )
		self.Titleframe.pack(side=TOP)
		self.lbltitle = Label(self.Titleframe, width = 30, font = ( "arial", 52, "bold" ), text = "LIBRARY MANAGEMENT SYSTEM", padx = 20 )
		self.lbltitle.grid()

		l =Buttons(self.Library_window)

## Student's Username And Password Check
## page were the user name and password of the students are checked

	def b_clicked(self):
		
		conn = sq3.connect("app.db")
		c = conn.cursor()
		query = "select password from Student_Data where username = '{}' ;".format(self.Username.get())
		c.execute( query )	

		k = c.fetchone()

		if self.Username.get() == "" or self.Password.get() == "":

			txt = Label(self.Login_page, text = "field is empty !").grid(column = 0, row = 6)

		elif k == None:

			txt3 = Label(self.Login_page, text = "username or pasword not correct").grid(column = 0, row = 7)

		elif k[0] == self.Password.get():
			self.Login_page.withdraw()
			self.Student_Page = Toplevel(self.Login_page)
			self.Student_Page.geometry("1350x750+0+0")

			query_name = "select name from Student_Data where username = '{}'".format(self.Username.get())
			c.execute( query_name )
			self.d = c.fetchone()[0]

			self.e = self.Username.get()

			k = Student(self.Student_Page, self.d, self.e)
		else:
			txt2 = Label(self.Login_page, text = "username or pasword not correct").grid(column = 0, row = 8)	
		conn.commit()
		conn.close()

##    To call Register class

	def bt3_clicked(self):
		
		self.register = RegisterForm(self.Library_window)

		self.Library_window.mainloop()


### To check admin username and password 


	def enter_clicked(self): 
			
		if self.Username.get() == "admin" and self.Password.get() == "000":
			
			k = admin_page(self.admin_page)	

		elif self.Username.get()=="" or self.Password.get()=="":
			
			txt1 = Label(self.admin_page, text = "field is empty !").grid( column = 0, row = 14)

		else:
			
			txt = Label(self.admin_page, text = "usernamr or password not correct !").grid(column = 0, row = 15)


#   Student Page
#   page having all information related to the student

class Student():

	def __init__(self, Student_Page, d, e):

		self.Student_Page = Student_Page
		self.d = d
		self.e = e

		self.Mainframe = Frame(self.Student_Page)
		self.Mainframe.grid()

		self.Titleframe = Frame(self.Mainframe, width = 1350, padx = 20, bd = 50, relief = RIDGE )
		self.Titleframe.pack(side=TOP)
		self.lbltitle = Label(self.Titleframe, width = 30, font = ( "arial", 52, "bold" ), text = "HEY '{}'".format(self.d), padx = 30 )
		self.lbltitle.grid()

		
		b2 = Button(self.Student_Page, text = "Books", font = ( "arial", 20, "bold" ), width = 20, command = self.b2_clicked).grid(column=0, row=2, pady = 10)

		b3 = Button(self.Student_Page, text = "Borrow Book", font = ( "arial", 20, "bold" ), width = 20, command = self.borrow_clicked).grid(column = 0, row = 3, pady = 10)

		b4 = Button(self.Student_Page, text = "Deposit Book", font = ( "arial", 20, "bold" ), width = 20, command = self.deposit_clicked).grid(column = 0, row = 4, pady = 10)

		b5 = Button(self.Student_Page, text = "Logout", font = ( "arial", 20, "bold" ), width = 20, command = self.logout_clicked).grid(column = 0, row = 5, pady = 10)

		b6 = Button(self.Student_Page, text = "Profile", font = ("arial", 20, "bpld"), width = 20, command = self.student_profile).grid(column = 0, row = 6, pady = 10)




#### Student_profile


	def student_profile(self):

		self.Student_Page.withdraw()
		self.Student_profile = Toplevel(self.Student_Page)
		self.Student_profile.geometry("1350x750+0+0")

		self.Mainframe = Frame(self.Student_profile)
		self.Mainframe.grid()




## Student Logout and back to Library Window
	
	def logout_clicked(self):

		self.Student_Page.withdraw()
		self.Library_window = Toplevel(self.Student_Page)
		self.Library_window.geometry("1350x750+0+0")

		self.Mainframe = Frame(self.Library_window)
		self.Mainframe.grid()

		self.Titleframe = Frame(self.Mainframe, width = 1350, padx = 20, bd = 50, relief = RIDGE )
		self.Titleframe.pack(side=TOP)
		self.lbltitle = Label(self.Titleframe, width = 30, font = ( "arial", 52, "bold" ), text = "LIBRARY MANAGEMENT SYSTEM", padx = 20 )
		self.lbltitle.grid()

		l =Buttons(self.Library_window)
		

## Student's Book borrow page

	def borrow_clicked(self):
	
		self.Student_Page.withdraw()
		self.borrow_page = Toplevel(self.Student_Page)
		self.borrow_page.geometry("1350x750+0+0")



		txt2 = Label(self.borrow_page, text = "Book ID").grid( column = 0, row = 1)
		self.id = Entry(self.borrow_page, width = 20, borderwidth = 5)
		self.id.grid( column = 1, row = 1)

		b1 = Button(self.borrow_page, text = "ENTER", command = self.enter_clicked2).grid(column = 2, row = 2)

		b2 = Button(self.borrow_page, text = "BACK", command = self.back_clicked2).grid(column = 3, row = 2)


## Student's Book Deposit Page 


	def deposit_clicked(self):
		
		self.Student_Page.withdraw()
		self.deposit_page = Toplevel(self.Student_Page)
		self.deposit_page.geometry("1350x750+0+0")



		txt2 = Label(self.deposit_page, text = "Book ID").grid( column = 0, row = 1)
		self.id = Entry(self.deposit_page, width = 20, borderwidth = 5)
		self.id.grid( column = 1, row = 1)


		b1 = Button(self.deposit_page, text = "ENTER", command = self.enter_clicked1).grid(column = 2, row = 2)

		b2 = Button(self.deposit_page, text = "BACK", command = self.back_clicked1).grid(column = 3, row = 2)

## Back to the Student page from borrow page

	def back_clicked2(self):
		
		self.borrow_page.withdraw()
		self.Student_Page = Toplevel(self.borrow_page)
		self.Student_Page.geometry("1350x750+0+0")
		conn = sq3.connect("app.db")
		c = conn.cursor()

		query_name = "select name from Student_Data where username = '{}'".format(self.e)
		c.execute( query_name )
		self.d = c.fetchone()[0]

		conn.commit()
		conn.close()
		
		a = Student(self.Student_Page, self.d, self.e)	

# Book borrow funtionality

	def enter_clicked2(self):

		conn = sq3.connect("app.db")
		c = conn.cursor()

		query5 = "select book_id from Book_Data"
		c.execute( query5 )
		k=c.fetchall()

		b=[]

		for i in range(len(k)):
			b.append(k[i][0])



		if self.id.get() not in b:

			txt4 = Label(self.borrow_page, text = "Book Not Available !").grid(column = 0, row = 8)

		else:	

			query4 = "select roll_no from Student_Data where username = '{}' ".format(self.e)
			c.execute( query4 )
			g=c.fetchone()


			query1 = "select book_borrowed from Student_Data where roll_no = {} ".format(g[0])
			c.execute( query1 )
			t = c.fetchall()
			

			query3 = "select count from Book_Data where book_id = '{}' ".format(self.id.get())
			c.execute( query3 )
			m=c.fetchone()

			r = list(m)


			if t[0][0]!=None:
				l = t[0][0].split("|")
			else:
				l=[]

			if self.id.get() == "":

				txt2 = Label(self.borrow_page, text = "field is empty !").grid( column = 0, row = 4)

			elif r[0]<1:

				txt = Label(self.borrow_page, text  = "Book Not Available").grid(column = 0, row = 5)

			elif self.id.get() in l:

				txt1 = Label(self.borrow_page, text = "Book has already been borrowed by you !").grid(column = 0, row = 6)
		
			
			else:

				r[0]-=1
				query2 = "update Book_Data set count = {} where book_id = '{}' ".format(r[0],self.id.get())
				c.execute( query2 )

				l=[]
				for i in range(len(t)):
					l.append(t[i][0])
				l.append(self.id.get())
				if None in l:
					l.remove(None)

				query = "update Student_Data set book_borrowed = '{}' where roll_no = {} ".format("|".join(l), g[0])
				c.execute( query )
				txt3 = Label(self.borrow_page, text = "Book Borrowed Succesfully !").grid(column = 0, row = 7)

		conn.commit()
		conn.close()	

# Back to Student page from deposit Page

	def back_clicked1(self):

		self.deposit_page.withdraw()
		self.Student_Page = Toplevel(self.deposit_page)
		self.Student_Page.geometry("1350x750+0+0")
		conn = sq3.connect("app.db")
		c = conn.cursor()

		query_name = "select name from Student_Data where username = '{}'".format(self.e)
		c.execute( query_name )
		self.d = c.fetchone()[0]

		conn.commit()
		conn.close()
		
		k = Student(self.Student_Page, self.d, self.e)	

# Book borrow funtionality		

	def enter_clicked1(self):

		conn = sq3.connect("app.db")
		c = conn.cursor()

		query4 = "select roll_no from Student_Data where username = '{}' ".format(self.e)
		c.execute( query4 )
		k=c.fetchone()[0]	


		if self.id.get() == "":

			txt1 = Label(self.deposit_page, text = "Field is empty").grid(column = 3, row = 4)

		else:	

			query1 = "select book_borrowed from Student_Data where roll_no = {}".format(k)
			c.execute( query1 )

			t = list(c.fetchone())
			t = t[0].split("|")
		

			if self.id.get() not in t:

				txt = Label(self.deposit_page, text = "This book has not been borrowed by you").grid(column = 3, row = 3)
			else:	

				t.remove(self.id.get())

				query = "update Student_Data set book_borrowed = '{}' where roll_no = {} ".format("|".join(t), k)
				c.execute( query )
				
				query3 = "select count from Book_Data where book_id = '{}' ".format(self.id.get())
				c.execute( query3 )
				r = list(c.fetchone())
				r[0]+=1


				query2 = "update Book_Data set count = {} where book_id = '{}' ".format(r[0],self.id.get())
				c.execute( query2 )

		conn.commit()
		conn.close()

##     Books Borrowed Page

	def b2_clicked(self):
		
		self.Student_Page.withdraw()
		self.Book_page = Toplevel(self.Student_Page)
		self.Book_page.geometry("1920x1080+0+0")

		self.Mainframe = Frame(self.Book_page)
		self.Mainframe.grid()

		txt1 = Label(self.Book_page, text = "Books Borrowed", font = ("arial", 15, "bold")).grid(column = 0, row = 0)

		conn = sq3.connect("app.db")
		c = conn.cursor()

		query = "select book_borrowed from Student_Data where username = '{}'".format(self.e)
		c.execute( query )


		t = c.fetchone()[0]

		if t==None:
			txt = Label(self.Book_page, text = "Not borrowed any book").grid(column = 0, row = 1)
		
		else:	

			l = list(t.split("|"))

			rows = []

			

			for i in range(len(l)):
				query1 = "select book_id, book_name, author_name, Subject from Book_Data where book_id = '{}' ".format(l[i])
				c.execute( query1 )
				www = c.fetchall()
				if www:
					rows.append(www[0])

			
			self.frame = Frame(self.Book_page)
			self.frame.grid()

			self.tv = ttk.Treeview(self.frame, column =("book_id","book_name","author_name", "Subject"), height = len(l))
			

			self.tv.heading("book_id", text = "Book ID")
			self.tv.heading("book_name", text = "Book Name")
			self.tv.heading("author_name", text = "Author Name")
			self.tv.heading("Subject", text = "Subject")


			self.tv.grid(column = 0, row = 2, padx=20)

			for i in rows:
				self.tv.insert('', 'end', values = i)



		txt2 = Label(self.Book_page, text = "Books Available", font = ("arial", 15, "bold")).grid(column = 0, row = 3)

		self.frame = Frame(self.Book_page)
		self.frame.grid()

		
		query2 = "select * from Book_Data"

		c.execute( query2 )

		all_data = c.fetchall()

		if len(all_data)==0:
			txt4 = Label(self.Book_page,  text = "No Book Available").grid( column = 0, row  = 4 )

		else:


			self.tv2 = ttk.Treeview(self.frame, column = ("book_id", "book_name", "author_name", "Subject", "count"), height = len(all_data))

			self.tv2.heading("book_id", text = "Book ID")
			self.tv2.heading("book_name", text = "Book Name")
			self.tv2.heading("author_name", text = "Author Name")
			self.tv2.heading("Subject", text = "Subject")
			self.tv2.heading("count", text = "Count")


			self.tv2.grid(column = 0, row = 6, padx=10)

			for i in all_data:
				self.tv2.insert('', 'end', values = i)


		b = Button(self.Book_page, text = "BACK", command = self.back_clicked3).grid(column = 0, row = 10)


		self.Book_page.mainloop()

## Back  to Student page from book borrow page		

	def back_clicked3(self):

		self.Book_page.withdraw()
		self.Student_Page = Toplevel(self.Book_page)
		self.Student_Page.geometry("1350x750+0+0")
		conn = sq3.connect("app.db")
		c = conn.cursor()

		query_name = "select name from Student_Data where username = '{}'".format(self.e)
		c.execute( query_name )
		self.d = c.fetchone()[0]

		conn.commit()
		conn.close()
		
		k = Student(self.Student_Page, self.d, self.e)	
			
		
##   Admin Page

class admin_page():

	def __init__(self,admin_page):

		self.admin_page = admin_page
		self.admin_page.withdraw()
		self.admin_page = Toplevel(self.admin_page)
		self.admin_page.geometry("1350x750+0+0")


		self.Mainframe = Frame(self.admin_page)
		self.Mainframe.grid()

		self.Titleframe = Frame(self.Mainframe, width = 1350, padx = 20, bd = 50, relief = RIDGE )
		self.Titleframe.pack(side=TOP)
		self.lbltitle = Label(self.Titleframe, width = 30, font = ( "arial", 52, "bold" ), text = "WELCOME ADMIN", padx = 30 )
		self.lbltitle.grid()


		b1 = Button(self.admin_page, text = "Add Book", font = ( "arial", 20, "bold" ), width = 20, command = self.ok_clicked1).grid( column = 0, row = 2, pady = 20 )

		txt2 = Label(self.admin_page, text = "Remove Book:", font = ( "arial", 20, "bold" )).grid( column = 0, row = 3)
		self.remove_book = Entry(self.admin_page, width = 20, borderwidth = 5 )
		self.remove_book.grid( column = 0, row = 4)
		
		b2 = Button(self.admin_page, text = "OK", command = self.ok_clicked2).grid( column = 0, row = 5 )

		b3 = Button(self.admin_page, text = "Book Details", font = ( "arial", 20, "bold" ), width = 20, command = self.book_d_clicked).grid(column = 0, row = 8, pady = 20)


		b5 = Button(self.admin_page, text = "Logout", font = ( "arial", 20, "bold" ), width = 20, command = self.logout_clicked).grid( column = 0, row = 9, pady = 10)

## 		Book Details page on admin account

	def book_d_clicked(self):

		self.admin_page.withdraw()
		self.book_details = Toplevel(self.admin_page)
		self.book_details.geometry("1350x750+0+0")

		conn = sq3.connect("app.db")
		c = conn.cursor()

		self.frame = Frame(self.book_details)
		self.frame.grid()



		
		query2 = "select * from Book_Data"

		c.execute( query2 )

		all_data = c.fetchall()

		if len(all_data)==0:

			txt4 = Label(self.book_details,  text = "No Book Available", font = ("arial", 10, "bold")).grid(column = 0, row  = 3)

		else:

			tv2 = ttk.Treeview(self.frame, column = ("book_id", "book_name", "author_name", "Subject", "count"), height = len(all_data))

			tv2.heading("book_id", text = "Book ID")
			tv2.heading("book_name", text = "Book Name")
			tv2.heading("author_name", text = "Author Name")
			tv2.heading("Subject", text = "Subject")
			tv2.heading("count", text = "Count")


			tv2.grid(column = 1, row = 5, padx=10, pady = 20)

			for i in all_data:
				tv2.insert('', 'end', values = i)

		conn.commit()
		conn.close()	


		b = Button(self.book_details, text = "BACK", command = self.back_clicked3).grid(column = 0, row = 8)

		self.book_details.mainloop()

## Back to admin page from book details page

	def back_clicked3(self):

		k = admin_page(self.book_details)	



## Admin Logout


	def logout_clicked(self):

		self.admin_page.withdraw()
		self.Library_window = Toplevel(self.admin_page)
		self.Library_window.geometry("1350x750+0+0")

		self.Mainframe = Frame(self.Library_window)
		self.Mainframe.grid()

		self.Titleframe = Frame(self.Mainframe, width = 1350, padx = 20, bd = 50, relief = RIDGE )
		self.Titleframe.pack(side=TOP)
		self.lbltitle = Label(self.Titleframe, width = 30, font = ( "arial", 52, "bold" ), text = "LIBRARY MANAGEMENT SYSTEM", padx = 20 )
		self.lbltitle.grid()

		l =Buttons(self.Library_window)

## Add book

	def ok_clicked1(self):

		k = Add_Book(self.admin_page)

## Remove Book in admin Account

	def ok_clicked2(self):
		
		conn = sq3.connect("app.db")
		c = conn.cursor()

		query1 = "select book_borrowed from Student_Data"
		c.execute( query1 )

		data = c.fetchall()


		l=[]

		for i in range(len(data)):

			if data[i][0] == None:

				data.remove(data[i])

			else:

				l+=data[i][0].split("|")

		

		if self.remove_book.get() in l:
			txt = Label(self.admin_page, text = "Book can not be remove as it is already bougtht by someone !").grid(column = 7, row = 7)

		elif self.remove_book.get() == "":

			txt1 = Label(self.admin_page, text = "field is empty").grid(column = 7, row = 7)
		
		else:
		

			query = "delete from Book_Data where book_id = '{}'".format(self.remove_book.get())
			c.execute( query )

			txt2 = Label(self.admin_page, text = "Book is removed succesfully !").grid(column = 9, row = 9)

		conn.commit()
		conn.close()


class Add_Book():

	def __init__(self, admin_page):
		self.admin_page = admin_page
		self.admin_page.withdraw()
		self.book_page = Toplevel(self.admin_page)
		self.book_page.geometry("1350x750+0+0")

		txt1 = Label(self.book_page, text = "Book ID    ").grid( column = 0, row = 0 )
		self.book_id = Entry(self.book_page, width = 20, borderwidth = 5 )
		self.book_id.grid( column = 1, row = 0 )

		txt2 = Label(self.book_page, text = "Book Name    ").grid( column = 0, row = 1 )
		self.book_name = Entry(self.book_page, width = 20, borderwidth = 5 )
		self.book_name.grid( column = 1, row = 1 )

		txt3 = Label(self.book_page, text = "Author Name    ").grid( column = 0, row = 2 )
		self.author_name = Entry(self.book_page, width = 20, borderwidth = 5 )
		self.author_name.grid( column = 1, row = 2 )

		txt4 = Label(self.book_page, text = "Subject	").grid( column = 0, row = 3 )
		self.Subject = Entry(self.book_page, width = 20, borderwidth = 5 )
		self.Subject.grid( column = 1, row = 3)

		txt5 = Label(self.book_page, text = "Count    ").grid( column = 0, row = 4 ) 
		self.Count = Entry(self.book_page, width = 20, borderwidth = 5 )
		self.Count.grid(column = 1, row = 4)

		b = Button(self.book_page, text = "ADD", command = self.add_clicked).grid(column = 4, row = 4)

		b1 = Button(self.book_page, text = "BACK", command = self.back_clicked).grid(column = 5, row = 4)

##  Book add funtionality

	def add_clicked(self):

		conn = sq3.connect("app.db")
		c = conn.cursor()

		query1 = "select book_id from Book_Data"
		c.execute( query1 )

		t = c.fetchall()

		l=[]

		for i in range(len(t)):
			l.append(t[i][0])

		try:	
			if self.book_id.get() == "" or self.book_name.get()=="" or self.author_name.get()=="" or self.Count.get()=="":
				
				txt1 = Label(self.book_page, text = "field is empty !").grid(column = 7, row = 7)	

			else:	


				query = "insert into Book_Data(book_id, book_name, author_name, Subject, count) values( '{}', '{}', '{}', '{}', {} );".format(self.book_id.get(), self.book_name.get(), self.author_name.get(), self.Subject.get(), self.Count.get() )
				c.execute( query )

				txt2 = Label(self.book_page, text = "Book added succesfully !").grid(column = 8, row = 8)
			
			conn.commit()
			conn.close()

		except:
			txt = Label(self.book_page, text = "Book already exist in Library Database !").grid(column = 6, row = 6)	

	
## Back to admin page from book page

	def back_clicked(self):
		
		k = admin_page(self.book_page)

		
## Students registration 


class RegisterForm():

	def __init__(self, root):
		
		self.root = root

		self.root.withdraw()

		self.Library_window = Toplevel(root)

		self.Library_window.geometry("1350x820+0+0")

		self.Mainframe = Frame(self.Library_window)
		self.Mainframe.grid()

		self.Titleframe = Frame(self.Mainframe, width = 1350, padx = 2, bd = 50, relief = RIDGE )
		self.Titleframe.grid(row=0,column=0)
		self.lbltitle = Label(self.Titleframe, width = 31, font = ( "arial", 53, "bold" ), text = "REGISTRATION" )
		self.lbltitle.grid(row=0,column=0)



		txt1 = Label(self.Library_window, text =  "Student Name:", font = ("arial", 20, "bold" )).grid(column =0, row = 1)
		self.Name = Entry(self.Library_window,width=20, borderwidth=5, font = ("arial", 14))
		self.Name.grid(column=0,row=2, pady  = 10)

		txt2 = Label(self.Library_window, text="Roll no:", font = ("arial", 20, "bold")).grid(column=0,row=3)
		self.Roll_no = Entry(self.Library_window, width=20, borderwidth=5, font = ("arial", 14))
		self.Roll_no.grid(column=0,row=4, pady = 10)

		txt3 = Label(self.Library_window, text = "Phone no:", font = ("arial", 20, "bold")).grid(column=0,row=5)
		self.Mobile_no = Entry(self.Library_window, width=20,borderwidth=5, font = ("arial", 14))
		self.Mobile_no.grid(column=0,row=6, pady = 10)

		txt4 = Label(self.Library_window, text = "Branch:", font = ("arial", 20, "bold")).grid(column=0,row=7)
		self.Branch = Entry(self.Library_window, width=20, borderwidth=5, font = ("arial", 14))
		self.Branch.grid(column=0,row=8, pady = 10)

		txt5 = Label(self.Library_window, text = "Username:", font = ("arial", 20, "bold")).grid(column=0,row=9)
		self.Username = Entry(self.Library_window, width=20, borderwidth=5, font = ("arial", 14))
		self.Username.grid(column=0,row=10, pady = 10)

		txt6 = Label(self.Library_window, text = "Password:", font = ("arial", 20, "bold")).grid(column = 0, row =11)
		self.Password = Entry( self.Library_window, width=20, borderwidth=5, font = ("arial", 14))
		self.Password.grid( column=0,row=12, pady = 10 )

		bt = Button( self.Library_window, text="ENTER", font = ("arial", 15, "bold"), command=self.submit ).grid( column=0,row=14, pady=10)

		btt = Button(self.Library_window, text = "BACK", font = ("arial", 15, "bold"), command = self.btt3_back).grid(column = 0, row = 15)

		self.Library_window.mainloop()

## Back too  library page from registration page

	def btt3_back(self):

		self.Library_window.withdraw()
		self.Library_window = Toplevel(self.Library_window)
		self.Library_window.geometry("1350x760+0+0")

		self.Mainframe = Frame(self.Library_window)
		self.Mainframe.grid()

		self.Titleframe = Frame(self.Mainframe, width = 1350, padx = 20, bd = 50, relief = RIDGE )
		self.Titleframe.pack(side=TOP)
		self.lbltitle = Label(self.Titleframe, width = 30, font = ( "arial", 52, "bold" ), text = "LIBRARY MANAGEMENT SYSTEM", padx = 20 )
		self.lbltitle.grid()

		l =Buttons(self.Library_window)

	def submit(self):
		
		conn = sq3.connect("app.db")
		c = conn.cursor()

		query2 = "select roll_no from Student_Data"
		c.execute( query2 )

		m = c.fetchall()

		n=[]

		for i in range(len(m)):
			n+=m[i]


		query1 = "select username from Student_Data"
		c.execute( query1 )

		k=[]

		t = c.fetchall()
		
		for i in range(len(t)):
			k+=t[i]


		if self.Name.get() == "" or self.Roll_no.get() == "" or self.Mobile_no.get() == "" or self.Branch.get() == "" or self.Username.get() == "" or self.Password.get() == "":

			txt = Label(self.Library_window, text = "field is empty !").grid(column = 0, row = 19)

			conn.commit()
			conn.close()

		else:
			flag=0

			try:
				roll = self.Roll_no.get()
				query = "insert into Student_Data( roll_no ) values( {} )".format(roll)
				c.execute( query )
			
			except sq3.IntegrityError:	
				txt2 = Label(self.Library_window, text = "This Roll no. has already registered !").grid(column = 0, row = 16)
				flag=1
		
			except sq3.OperationalError:
				txt = Label(self.Library_window, text = "Please enter valid Roll N0. !").grid(column = 0, row = 17)
				flag=1

			if flag==0:	
				try:
					query = "update Student_Data set username = '{}' where roll_no = {}".format(self.Username.get(), roll)
					c.execute( query )

				except sq3.IntegrityError:
					txt1 = Label(self.Library_window, text = "This usenamae has already been taken").grid( column = 0, row = 17 )
					flag=1	

				except  sq3.OperationalError:
					txt = Label(self.Library_window, text = "Please Enter valid Username !").grid(column = 0, row = 18)
					flag=1

				if flag==0:
					try:
						query = "update Student_Data set name = '{}', Mob_no = {}, branch = '{}', password = '{}' where roll_no = {};".format(self.Name.get(), self.Mobile_no.get() , self.Branch.get(), self.Password.get(), roll )
						c.execute( query )
						
						conn.commit()
						conn.close()
						
						self.Library_window.withdraw()
						self.Library_window = Toplevel(self.Library_window)
						self.Library_window.geometry("1350x750+0+0")

						self.Mainframe = Frame(self.Library_window)
						self.Mainframe.grid()

						self.Titleframe = Frame(self.Mainframe, width = 1350, padx = 20, bd = 50, relief = RIDGE )
						self.Titleframe.pack(side=TOP)
						self.lbltitle = Label(self.Titleframe, width = 30, font = ( "arial", 52, "bold" ), text = "LIBRARY MANAGEMENT SYSTEM", padx = 20 )
						self.lbltitle.grid()
						l =Buttons(self.Library_window)
					except:
						txt = Label(self.Library_window, text = "Please enter a valid Phone number !").grid(column = 0, row = 18)	

					




if __name__=="__main__":

	lib = Library()
