from tkinter import*
import math,random,os
from tkinter import messagebox ,ttk
import sqlite3
import os
import tempfile
root=Tk()

#connection of data base --
con = sqlite3.connect('bill_store.db')
#create curser
c = con.cursor()








class bill_app:
	def __init__(self,root):
		self.root=root
		self.root.geometry("1525x1500+0+0")
		self.root.title("Billing Software")
		bg_color="#074463"
		title=Label(self.root,text="Billing Software",bd=15,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
		# variable==================
		#=========total product price and tax variable=====

		self.cosmetic_price=StringVar()
		self.grocery_price=StringVar()
		self.cold_drink_price=StringVar()

		self.cosmetics_tax=StringVar()
		self.grocery_tax=StringVar()
		self.cold_drink_tax=StringVar()

		#=========customer details=====

		self.c_name=StringVar()
		self.c_phon=StringVar()

		self.bill_no=StringVar()
		x=random.randint(1000,9999)
		self.bill_no.set(str(x))

		self.search_bill=StringVar()

		self.bill_sucess=0

		###############################
		#wrapper1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
		wrapper1=LabelFrame(root,text="cosmetic")
		wrapper2=LabelFrame(root,text="grocery")
		wrapper3=LabelFrame(root,text="cold_drink")		   		    







		#CUSTOMAR DETAILSSS-----
		F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="customer details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
		F1.place(x=0,y=80,relwidth=1)
		
		cname_lbl=Label(F1,text="Customer name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
		cname_txt=Entry(F1,width=15,textvariable=self.c_name ,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

		cphn_lbl=Label(F1,text="Contact No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
		cphn_txt=Entry(F1,width=15,textvariable=self.c_phon, font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

		c_bill_lbl=Label(F1,text="Bill No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
		c_bill_txt=Entry(F1,width=10,textvariable=self.search_bill ,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)


		btn_btn=Button(F1,text="search",command=self.find_bill,width=10,bd=10,font="arial 12 bold").grid(row=0,column=6,padx=13,pady=10)
		back_btn=Button(F1,text="settings",command=self.settings,width=10,bd=10,font="arial 12 bold").grid(row=0,column=7,padx=13,pady=10)
		logout_btn=Button(F1,text="Logout",command=self.Logout,width=10,bd=10,font="arial 12 bold").grid(row=0,column=8,padx=13,pady=10)

		##################################################

########################
		mycanvas=Canvas(wrapper1 , width=5)
		mycanvas.pack(side=LEFT,fill="both",expand="yes")
		yscrollbar =ttk.Scrollbar(wrapper1,orient="vertical",command=mycanvas.yview)
		yscrollbar.pack(side=RIGHT,fill="y")
		mycanvas.configure(yscrollcommand=yscrollbar.set)
		mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
		self.myframe=Frame(mycanvas)
		mycanvas.create_window((0,0),window=self.myframe,anchor="nw")
		wrapper1.place(x=5,y=200,width=350,height=440)
		#.pack(fill="both",expand="yes",padx=10,pady=10)
		self.show()
		###################################

		mycanvas1=Canvas(wrapper2 ,width=5)
		mycanvas1.pack(side=LEFT,fill="both",expand="yes")
		yscrollbar =ttk.Scrollbar(wrapper2,orient="vertical",command=mycanvas1.yview)
		yscrollbar.pack(side=RIGHT,fill="y")
		mycanvas1.configure(yscrollcommand=yscrollbar.set)
		mycanvas1.bind('<Configure>', lambda e: mycanvas1.configure(scrollregion = mycanvas1.bbox('all')))
		self.myframe=Frame(mycanvas1)
		mycanvas1.create_window((0,0),window=self.myframe,anchor="nw")
		wrapper2.place(x=380,y=200,width=350,height=440)
		#.pack(fill="both",expand="yes",padx=10,pady=10)
		self.show1()
		################################

		mycanvas2=Canvas(wrapper3 ,width=5)
		mycanvas2.pack(side=LEFT,fill="both",expand="yes")
		yscrollbar =ttk.Scrollbar(wrapper3,orient="vertical",command=mycanvas2.yview)
		yscrollbar.pack(side=RIGHT,fill="y")
		mycanvas2.configure(yscrollcommand=yscrollbar.set)
		mycanvas2.bind('<Configure>', lambda e: mycanvas2.configure(scrollregion = mycanvas2.bbox('all')))
		self.myframe=Frame(mycanvas2)
		mycanvas2.create_window((0,0),window=self.myframe,anchor="nw")
		wrapper3.place(x=755,y=200,width=350,height=440)
		#.pack(fill="both",expand="yes",padx=10,pady=10)
		self.show2()
		###################################################



		

		#============bill area========++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		F5=Frame(self.root,bd=10,relief=GROOVE)
		F5.place(x=1140,y=200,width=360,height=440)
		
		bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
		scrol_y=Scrollbar(F5,orient=VERTICAL)
		self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
		scrol_y.pack(side=RIGHT,fill=Y)
		scrol_y.config(command=self.txtarea.yview)
		self.txtarea.pack(fill=BOTH,expand=1)
		


		#button frame+++++++++++++++++

		F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
		F6.place(x=0,y=650,relwidth=1,height=140)

		m1_lbl=Label(F6,text="cosmetic_price",bg=bg_color,fg="white",font=("times new roamn",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
		self.answer=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)


		m2_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roamn",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
		m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)


		m3_lbl=Label(F6,text="Total Cold Drinks Price",bg=bg_color,fg="white",font=("times new roamn",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
		m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)
		


		c1_lbl=Label(F6,text=" Cosmetic Tax",bg=bg_color,fg="white",font=("times new roamn",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
		c1_txt=Entry(F6,width=18,textvariable=self.cosmetics_tax ,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)


		c2_lbl=Label(F6,text=" Grocery Tax",bg=bg_color,fg="white",font=("times new roamn",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
		c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)


		c3_lbl=Label(F6,text=" Cold Drinks Tax",bg=bg_color,fg="white",font=("times new roamn",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
		c3_txt=Entry(F6,width=18,textvariable=self.cold_drink_tax ,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)



		btn_f=Frame(F6,bd=7,relief=GROOVE)
		btn_f.place(x=780,width=730,height=105)

		Total_btn=Button(btn_f,text="Total",command=self.total,bg="cadetblue",fg="white",bd=5,pady=15,width=14,font="arial 12 bold").grid(row=0,column=0,padx=10,pady=5)
		Gbill_btn=Button(btn_f,text="GenrateBill ",command=self.bill_area,bg="cadetblue",fg="white",bd=5,pady=15,width=14,font="arial 12 bold").grid(row=0,column=1,padx=10,pady=5)
		Clear_btn=Button(btn_f,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",bd=5,pady=15,width=14,font="arial 12 bold").grid(row=0,column=2,padx=10,pady=5)
		print_btn=Button(btn_f,text="print",command=self.print_txt, bg="cadetblue",fg="white",bd=5,pady=15,width=14,font="arial 12 bold").grid(row=0,column=4,padx=10,pady=5)
		self.welcome_bill()



	
	def welcome_bill(self):
		self.txtarea.delete('1.0',END)
		self.txtarea.insert(END,"\t Welcome Pradeep Retail\n")
		self.txtarea.insert(END,f"\n Bill Number:   {self.bill_no.get() }")
		self.txtarea.insert(END,f"\n Customer Name: {self.c_name.get() }")
		self.txtarea.insert(END,f"\n Phone Number:  {self.c_phon.get()  }")
		self.txtarea.insert(END,f"\n=======================================")
		self.txtarea.insert(END,f"\n product\t\tQTY\t\tPrice")
		self.txtarea.insert(END,f"\n=======================================")


		
	###########################################################################################


	
		    ##############################################################################################
	def save_bill(self):
		op=messagebox.askyesno("save bill","do you want save the file..")
		if op>0:
			self.bill_data=self.txtarea.get('1.0',END)
			f1=open("bills/"+str(self.bill_no.get())+".txt","w")
			f1.write(self.bill_data)
			f1.close()
			###############################################
			#insert into tabel database billl-information---------------
			#connection of data base --
			con = sqlite3.connect('bill_store.db')
			#create curser
			c = con.cursor()

			c.execute("INSERT INTO bill_info VALUES (:bill_number, :name, :contact_num, :total_cost)",
			{
				'bill_number':self.bill_no.get(),	
				'name':self.c_name.get(),
				'contact_num': self.c_phon.get(),
				'total_cost': self.t_b
				
			})
			con.commit()						
			con.close()
			#################################################
			messagebox.showinfo("saved",f"Bill no.:{self.bill_no.get()} saved succesfully")
			

		else:
			return


	def find_bill(self):
		present="no"
		for i in os.listdir("bills/"):
			if i.split('.')[0]==self.search_bill.get():
				f1=open(f"bills/{i}","r")
				self.txtarea.delete('1.0',END)
				for d in f1:
					self.txtarea.insert(END,d)
				f1.close()
				present="yes"
		if present=="no":
			messagebox.showerror("Error","invalid Bill No..")

	def clear_data(self):
		op=messagebox.askyesno("clear","do you really want clear?")
		if op>0:
		#=========total product price and tax variable=====
			wrapper1=LabelFrame(root,text="cosmetic")
			wrapper2=LabelFrame(root,text="grocery")
			wrapper3=LabelFrame(root,text="cold_drink")

			################################################
			mycanvas=Canvas(wrapper1)
			mycanvas.pack(side=LEFT,fill="both",expand="yes")
			yscrollbar =ttk.Scrollbar(wrapper1,orient="vertical",command=mycanvas.yview)
			yscrollbar.pack(side=RIGHT,fill="y")
			mycanvas.configure(yscrollcommand=yscrollbar.set)
			mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
			self.myframe=Frame(mycanvas)
			mycanvas.create_window((0,0),window=self.myframe,anchor="nw")
			wrapper1.place(x=5,y=200,width=350,height=440)
			#.pack(fill="both",expand="yes",padx=10,pady=10)
			self.show_clear()
			##############################
			mycanvas1=Canvas(wrapper2)
			mycanvas1.pack(side=LEFT,fill="both",expand="yes")
			yscrollbar =ttk.Scrollbar(wrapper2,orient="vertical",command=mycanvas1.yview)
			yscrollbar.pack(side=RIGHT,fill="y")
			mycanvas1.configure(yscrollcommand=yscrollbar.set)
			mycanvas1.bind('<Configure>', lambda e: mycanvas1.configure(scrollregion = mycanvas1.bbox('all')))
			self.myframe=Frame(mycanvas1)
			mycanvas1.create_window((0,0),window=self.myframe,anchor="nw")
			wrapper2.place(x=380,y=200,width=350,height=440)
			#.pack(fill="both",expand="yes",padx=10,pady=10)
			self.show_clear1()
			################################
			mycanvas2=Canvas(wrapper3)
			mycanvas2.pack(side=LEFT,fill="both",expand="yes")
			yscrollbar =ttk.Scrollbar(wrapper3,orient="vertical",command=mycanvas2.yview)
			yscrollbar.pack(side=RIGHT,fill="y")
			mycanvas2.configure(yscrollcommand=yscrollbar.set)
			mycanvas2.bind('<Configure>', lambda e: mycanvas2.configure(scrollregion = mycanvas2.bbox('all')))
			self.myframe=Frame(mycanvas2)
			mycanvas2.create_window((0,0),window=self.myframe,anchor="nw")
			wrapper3.place(x=755,y=200,width=350,height=440)
			#.pack(fill="both",expand="yes",padx=10,pady=10)
			self.show_clear2()

			##################################
			self.cosmetic_price.set("")
			self.grocery_price.set("")
			self.cold_drink_price.set("")

			self.cosmetics_tax.set("")
			self.grocery_tax.set("")
			self.cold_drink_tax.set("")

			#=========customer details=====

			self.c_name.set("")
			self.c_phon.set("")

			self.bill_no.set("")
			x=random.randint(1000,9999)
			self.bill_no.set(str(x))

			self.search_bill.set("")



			self.welcome_bill()






		
	



		
	def print_txt(self):
		if self.c_name.get()=="" or self.c_phon.get()=="":
			messagebox.showerror("Error","Customer details must be required..")
		if self.bill_sucess==0:
			messagebox.showerror("Error","No try again..")


		elif self.cosmetic_price.get()=="Rs. 0" and self.grocery_price.get()=="Rs. 0" and self.cold_drink_price.get()=="Rs. 0":
			messagebox.showerror("Error","No product purchased...")
		else:
			op=messagebox.askyesno("print","do you really want print the bill?")
			if op>0:
				self.bill_data=self.txtarea.get('1.0',END)
				filename = tempfile.mktemp(".txt")
				open (filename,"w").write(self.bill_data)
				os.startfile(filename,"print")

	###############################################

	def get_values(self):
		return [int(entry.get()) for entry in self.entries]


	def get_values1(self):
		return [int(entry1.get()) for entry1 in self.entries1]

	def get_values2(self):
		return [int(entry2.get()) for entry2 in self.entries2]


	##################################total calculation###################
#Cosmetics cosmetic_price  cosmetics_tax
	
	def total(self):

		###########tax calculate##########################################1111111111111
		con = sqlite3.connect('bill_store.db')
		self.entry_val =[]
		self.tax_val=[]
		self.price_val=[]
		#create curser
		c = con.cursor()
		find_user = ('SELECT tax FROM user_details WHERE category = "Cosmetics"')	
		c.execute(find_user) 	
		rows=c.fetchall()
		#####
		find_user = ('SELECT price FROM user_details WHERE category = "Cosmetics"')	
		c.execute(find_user) 	
		rowss=c.fetchall()
		a=self.get_values()
		b=0
		for i in a:
			if i>0.0:
				self.tax_val.append(rows[b])
				self.price_val.append(rowss[b])
				self.entry_val.append(i)
				b=b+1
			else:
				b=b+1

		################
		#print(self.entry_val)	###which you submit in entery box
		
		#############
		p_convert=[i[0] for i in self.price_val]  ########conveert price value in tuple to  list
		#print(p_convert)

		p_multi=list(map(lambda x,y: x*y, self.entry_val,p_convert))  ##multiplication in entry box value and price value
		#print(p_multi)
		################
		self.cost_val=sum( p_multi)	##########self.cost_val is a sum of value of @@@@@@@@@cost price
		#print(self.cost_val)

		p_tax_convert=[i[0] for i in self.tax_val]    ######cnvert tax tuple to list
		#print(p_tax_convert)

		p_tax_cal=list(map(lambda x,y: x*y,p_multi,p_tax_convert)) ######## multipllication  on tax value and price value
		#print(p_tax_cal)

		self.tax_show=sum( p_tax_cal)	######## sum of tax which is show
		#print(self.tax_show)
		##############
		self.cosmetic_price.set("Rs. "+str((self.cost_val)))
		#############
		self.c_tax=round((self.tax_show),2)
		self.cosmetics_tax.set("Rs. "+str(self.c_tax))
		con.commit()						
		con.close()
		##############################################################################groceryyyy


		con = sqlite3.connect('bill_store.db')
		self.entry_val1 =[]
		self.tax_val1=[]
		self.price_val1=[]
		#create curser
		c = con.cursor()
		find_user = ('SELECT tax FROM user_details WHERE category = "Grocery"')	
		c.execute(find_user) 	
		rows=c.fetchall()
		#####
		find_user = ('SELECT price FROM user_details WHERE category = "Grocery"')	
		c.execute(find_user) 	
		rowss=c.fetchall()
		a=self.get_values1()
		b=0
		for i in a:
			if i>0.0:
				self.tax_val1.append(rows[b])
				self.price_val1.append(rowss[b])
				self.entry_val1.append(i)
				b=b+1
			else:
				b=b+1

		################
		#print(self.entry_val1)	###which you submit in entery box
		
		#############
		p_convert=[i[0] for i in self.price_val1]  ########conveert price value in tuple to  list
		#print(p_convert)

		p_multi=list(map(lambda x,y: x*y, self.entry_val1,p_convert))  ##multiplication in entry box value and price value
		#print(p_multi)
		################
		self.cost_val1=sum( p_multi)	##########self.cost_val is a sum of value of @@@@@@@@@cost price
		#print(self.cost_val1)

		p_tax_convert=[i[0] for i in self.tax_val1]    ######cnvert tax tuple to list
		#print(p_tax_convert)

		p_tax_cal=list(map(lambda x,y: x*y,p_multi,p_tax_convert)) ######## multipllication  on tax value and price value
		#print(p_tax_cal)

		self.tax_show1=sum( p_tax_cal)	######## sum of tax which is show
		#print(self.tax_show1)
		##############
		self.grocery_price.set("Rs. "+str((self.cost_val1)))
		#############
		self.c_tax1=round((self.tax_show1),2)
		self.grocery_tax.set("Rs. "+str(self.c_tax1))
		con.commit()						
		con.close()
		
		###############################################################################################3333
		con = sqlite3.connect('bill_store.db')
		self.entry_val2 =[]
		self.tax_val2=[]
		self.price_val2=[]
		#create curser
		c = con.cursor()
		find_user = ('SELECT tax FROM user_details WHERE category = "Cold Drinkss"')	
		c.execute(find_user) 	
		rows=c.fetchall()
		#####
		find_user = ('SELECT price FROM user_details WHERE category = "Cold Drinkss"')	
		c.execute(find_user) 	
		rowss=c.fetchall()
		a=self.get_values2()
		b=0
		for i in a:
			if i>0.0:
				self.tax_val2.append(rows[b])
				self.price_val2.append(rowss[b])
				self.entry_val2.append(i)
				b=b+1
			else:
				b=b+1

		################
		#print(self.entry_val2)	###which you submit in entery box
		
		#############
		p_convert=[i[0] for i in self.price_val2]  ########conveert price value in tuple to  list
		#print(p_convert)

		p_multi=list(map(lambda x,y: x*y, self.entry_val2,p_convert))  ##multiplication in entry box value and price value
		#print(p_multi)
		################
		self.cost_val2=sum( p_multi)	##########self.cost_val is a sum of value of @@@@@@@@@cost price
		#print(self.cost_val2)

		p_tax_convert=[i[0] for i in self.tax_val2]    ######cnvert tax tuple to list
		#print(p_tax_convert)

		p_tax_cal=list(map(lambda x,y: x*y,p_multi,p_tax_convert)) ######## multipllication  on tax value and price value
		#print(p_tax_cal)

		self.tax_show2=sum( p_tax_cal)	######## sum of tax which is show
		#print(self.tax_show2)
		##############
		self.cold_drink_price.set("Rs. "+str((self.cost_val2)))
		#############
		self.c_tax2=round((self.tax_show2),2)
		self.cold_drink_tax.set("Rs. "+str(self.c_tax2))
		con.commit()						
		con.close()
		
		##########################
		self.total_bill=round(float(self.cost_val+
								self.cost_val1+
									self.cost_val2+
									self.c_tax+
									self.c_tax1+
									self.c_tax2
									),2)
		#print(self.total_bill)
		#t_b for storing database---
		self.t_b=self.total_bill
		##########################
	def bill_area(self):
		if self.c_name.get()=="" or self.c_phon.get()=="":
			messagebox.showerror("Error","Customer details must be required..")

		elif self.cosmetic_price.get()=="Rs. 0" and self.grocery_price.get()=="Rs. 0" and self.cold_drink_price.get()=="Rs. 0":
			messagebox.showerror("Error","No product purchased...")
		else:
			
			
			self.welcome_bill() 


			#==========cosmetic============area
			con = sqlite3.connect('bill_store.db')
			#create curser
			c = con.cursor()
			find_user = ('SELECT price FROM user_details WHERE category = "Cosmetics"')	
			c.execute(find_user) 	
			rowss=c.fetchall()
			find_user = ('SELECT item_name FROM user_details WHERE category = "Cosmetics"')	
			c.execute(find_user) 	
			rows=c.fetchall()
			a=self.get_values()
			b=0
			for i in a:
				if i>0.0:
					#print(b)
					rows[b]=rows[b][0]
					rowss[b]=rowss[b][0]
					self.txtarea.insert(END,f"\n{rows[b]}\t\t{i}\t\t{rowss[b]}")

					b=b+1
				else:
					b=b+1
			
			con.commit()						
			con.close()
			#========================grocery================area
			con = sqlite3.connect('bill_store.db')
			#create curser
			c = con.cursor()
			find_user = ('SELECT price FROM user_details WHERE category = "Grocery"')	
			c.execute(find_user) 	
			rowss=c.fetchall()
			find_user = ('SELECT item_name FROM user_details WHERE category = "Grocery"')	
			c.execute(find_user) 	
			rows=c.fetchall()
			a=self.get_values1()
			b=0
			for i in a:
				if i>0.0:
					#print(b)
					rows[b]=rows[b][0]
					rowss[b]=rowss[b][0]
					self.txtarea.insert(END,f"\n{rows[b]}\t\t{i}\t\t{rowss[b]}")

					b=b+1
				else:
					b=b+1
			
			con.commit()						
			con.close()
			#=====================cold drink ====================area
			con = sqlite3.connect('bill_store.db')
			#create curser
			c = con.cursor()
			find_user = ('SELECT price FROM user_details WHERE category = "Cold Drinkss"')	
			c.execute(find_user) 	
			rowss=c.fetchall()
			find_user = ('SELECT item_name FROM user_details WHERE category = "Cold Drinkss"')	
			c.execute(find_user) 	
			rows=c.fetchall()
			a=self.get_values2()
			b=0
			for i in a:
				if i>0.0:
					#print(b)
					rows[b]=rows[b][0]
					rowss[b]=rowss[b][0]
					self.txtarea.insert(END,f"\n{rows[b]}\t\t{i}\t\t{rowss[b]}")

					b=b+1
				else:
					b=b+1
			
			con.commit()						
			con.close()
			##############
			self.txtarea.insert(END,f"\n--------------------------------------")

			if self.cosmetics_tax.get()!="Rs. 0":			
				self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t{self.cosmetics_tax.get()}")

			if self.grocery_tax.get()!="Rs. 0":			
				self.txtarea.insert(END,f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")

			if self.cold_drink_tax.get()!="Rs. 0":			
				self.txtarea.insert(END,f"\n Cold Drink Tax\t\t\t{self.cold_drink_tax.get()}")

			self.txtarea.insert(END,f"\n--------------------------------------")
			self.txtarea.insert(END,f"\n Total Bill :\t\t\tRs. {self.total_bill}")
			self.txtarea.insert(END,f"\n--------------------------------------")

			self.save_bill()
			self.bill_sucess=1
			
		
	################################################################################################
	def show(self):
		#connection of data base --
		bg_color="#074463"
		con = sqlite3.connect('bill_store.db')
		#create curser
		c = con.cursor()
		find_user = ('SELECT item_name FROM user_details WHERE category = "Cosmetics"')	
		c.execute(find_user) 	
		rows=c.fetchall()
		loop=len(rows)
		self.entries = []
		if len(rows)!=0:
			for i in range(loop):
				x=10
				y=15
				a=(rows[i])
				b=a
				lb=Label(self.myframe,text=a,bg="#074463",fg="white",font=("times new roamn",10,"bold"))
				lb.grid(row=i,column=0,padx=20,pady=1,sticky="w")
				entry=Entry(self.myframe,textvariable=(i),width=15,font="arial 13 bold",bd=7,relief=SUNKEN)
				entry.grid(row=i,column=1,padx=x,pady=y)	
				entry.insert(0, '0')
				self.entries.append(entry)
            	
				con.commit()	
		con.close()


	def show1(self):
		#connection of data base --
		con = sqlite3.connect('bill_store.db')
		#create curser
		c = con.cursor()
		#c.execute("SELECT item_name FROM user_details WHERE priority=?", (priority,))
		find_user = ('SELECT item_name FROM user_details WHERE category = "Grocery"')	
		c.execute(find_user) 	
		rows=c.fetchall()
		loop=len(rows)
		self.entries1 = []
		if len(rows)!=0:
			for i in range(loop):
				x=10
				y=15
				a=(rows[i])
				lb1=Label(self.myframe,text=a,bg="#074463",fg="white",font=("times new roamn",10,"bold"))
				lb1.grid(row=i,column=0,padx=x,pady=y)
				entry1=Entry(self.myframe,width=15,font="arial 13 bold",bd=7,relief=SUNKEN)
				entry1.grid(row=i,column=1,padx=x,pady=y)
				entry1.insert(0, '0')	
				self.entries1.append(entry1)
				con.commit()		
		con.close()

	def show2(self):
		#connection of data base --
		con = sqlite3.connect('bill_store.db')
		#create curser
		c = con.cursor()
		#c.execute("SELECT item_name FROM user_details WHERE priority=?", (priority,))
		find_user = ('SELECT item_name FROM user_details WHERE category = "Cold Drinkss"')	
		c.execute(find_user) 	
		rows=c.fetchall()
		loop=len(rows)
		self.entries2 = []
		if len(rows)!=0:
			for i in range(loop):
				x=10
				y=15
				a=rows[i]
				lb2=Label(self.myframe,text=a,bg="#074463",fg="white",font=("times new roamn",10,"bold"))
				lb2.grid(row=i,column=0,padx=x,pady=y)
				entry2=Entry(self.myframe,width=15,font="arial 13 bold",bd=7,relief=SUNKEN)
				entry2.grid(row=i,column=1,padx=x,pady=y)	
				entry2.insert(0, '0')	
				self.entries2.append(entry2)
				con.commit()		
		con.close()


	def show_clear(self):
		#connection of data base --
		bg_color="#074463"
		con = sqlite3.connect('bill_store.db')
		#create curser
		c = con.cursor()
		find_user = ('SELECT item_name FROM user_details WHERE category = "Cosmetics"')	
		c.execute(find_user) 	
		rows=c.fetchall()
		loop=len(rows)
		self.entries = []
		if len(rows)!=0:
			for i in range(loop):
				x=10
				y=15
				a=(rows[i])
				b=a
				lb=Label(self.myframe,text=a,bg="#074463",fg="white",font=("times new roamn",10,"bold"))
				lb.grid(row=i,column=0,padx=20,pady=1,sticky="w")
				entry=Entry(self.myframe,textvariable=(i),width=15,font="arial 13 bold",bd=7,relief=SUNKEN)
				entry.grid(row=i,column=1,padx=x,pady=y)	
				entry.delete(0, END)################check it
				self.entries.append(entry)
				entry.insert(0, '0')

				con.commit()	
		con.close()


	def show_clear1(self):
		#connection of data base --
		con = sqlite3.connect('bill_store.db')
		#create curser
		c = con.cursor()
		#c.execute("SELECT item_name FROM user_details WHERE priority=?", (priority,))
		find_user = ('SELECT item_name FROM user_details WHERE category = "Grocery"')	
		c.execute(find_user) 	
		rows=c.fetchall()
		loop=len(rows)
		self.entries1 = []
		if len(rows)!=0:
			for i in range(loop):
				x=10
				y=15
				a=(rows[i])
				lb1=Label(self.myframe,text=a,bg="#074463",fg="white",font=("times new roamn",10,"bold"))
				lb1.grid(row=i,column=0,padx=x,pady=y)
				entry1=Entry(self.myframe,width=15,font="arial 13 bold",bd=7,relief=SUNKEN)
				entry1.grid(row=i,column=1,padx=x,pady=y)
				entry1.delete(0, END)	
				self.entries1.append(entry1)
				entry1.insert(0, '0')
				con.commit()		
		con.close()


	def show_clear2(self):
		#connection of data base --
		con = sqlite3.connect('bill_store.db')
		#create curser
		c = con.cursor()
		#c.execute("SELECT item_name FROM user_details WHERE priority=?", (priority,))
		find_user = ('SELECT item_name FROM user_details WHERE category = "Cold Drinkss"')	
		c.execute(find_user) 	
		rows=c.fetchall()
		loop=len(rows)
		self.entries2 = []
		if len(rows)!=0:
			for i in range(loop):
				x=10
				y=15
				a=rows[i]
				lb2=Label(self.myframe,text=a,bg="#074463",fg="white",font=("times new roamn",10,"bold"))
				lb2.grid(row=i,column=0,padx=x,pady=y)
				entry2=Entry(self.myframe,width=15,font="arial 13 bold",bd=7,relief=SUNKEN)
				entry2.grid(row=i,column=1,padx=x,pady=y)	
				entry2.delete(0, END)
				self.entries2.append(entry2)
				entry2.insert(0, '0')
				con.commit()		
		con.close()
			

	def settings(self):

		self.root.destroy()
		import userpage

	


	def Logout(self):
		op=messagebox.askyesno("Exit","do you really want Logout?")
		if op>0:
			self.root.destroy()
			import login
	
	
obj=bill_app(root)
root.mainloop()