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
		   		    
		   		    
###############################

class user_page:

	def __init__(self,root):
		self.root=root
		self.root.geometry("1525x1500+0+0")

		self.root.title("admin page")
		bg_color="orange"

		title=Label(self.root,text="User Data Panel",bd=15,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=1)
		title.pack(side=TOP,fill=X)
		########################All variabls###########################

		self.name_var=StringVar()
		self.cata_var=StringVar()
		self.para_var=StringVar()
		self.item_name_var=StringVar()
		self.price_var=IntVar()
		self.item_quan_var=IntVar()
		self.tax_var=StringVar()

		self.search_by=StringVar()
		self.search_txt=StringVar()

		####################################################

		F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="customer details",font=("times new roman",20,"bold"),fg="red",bg=bg_color)
		F1.place(x=0,y=80,relwidth=1,height=110)
		
		cname_lbl=Label(F1,text="Shop Owner Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
		cname_txt=Entry(F1,textvariable=self.name_var,width=20,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

		btn_btn=Button(F1,text="Billing Page",command=self.billing_window,width=15,bd=8,font="arial 15 bold").grid(row=0,column=2,padx=13,pady=8)

		#btn_btn=Button(F1,text="submit",width=10,bd=8,font="arial 12 bold").grid(row=0,column=2,padx=13,pady=10)


		#manege frame###############################3
		Manage_frame=LabelFrame(self.root,bd=4,text="ITEM DETAILS",relief=RIDGE,bg=bg_color,fg="red",font=("times new roman",20,"bold"))
		Manage_frame.place(x=20,y=200,width=455,height=560)


		lbl_cata=Label(Manage_frame,text="Item category",font=("times new roman",18,"bold"),bg=bg_color,fg="red")
		lbl_cata.grid(row=0,column=0,pady=15,padx=20,sticky="w")

		self.cmb_question_cata = ttk.Combobox(Manage_frame,textvariable=self.cata_var, font=("times new roman",15),state='readonly',justify=CENTER) 
		self.cmb_question_cata['values']=("Select","Cosmetics","Grocery","Cold Drinkss")
		self.cmb_question_cata.place(x=217,y=26,width=180)
		self.cmb_question_cata.current(0)

		lbl_para=Label(Manage_frame,text="Item paramiter",font=("times new roman",18,"bold"),bg=bg_color,fg="red")
		lbl_para.grid(row=1,column=0,pady=15,padx=20,sticky="w")

		self.cmb_question_para = ttk.Combobox(Manage_frame,textvariable=self.para_var, font=("times new roman",15),state='readonly',justify=CENTER) 
		self.cmb_question_para['values']=("Select","Packet","kg","Liter")
		self.cmb_question_para.place(x=217,y=86,width=180)
		self.cmb_question_para.current(0)


		lbl_item=Label(Manage_frame,text="Item name",font=("times new roman",18,"bold"),bg=bg_color,fg="red")
		lbl_item.grid(row=2,column=0,pady=15,padx=20,sticky="w")
		item_txt=Entry(Manage_frame,textvariable=self.item_name_var,width=15,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=20)	


		lbl_value=Label(Manage_frame,text="Item price",font=("times new roman",18,"bold"),bg=bg_color,fg="red")
		lbl_value.grid(row=3,column=0,pady=15,padx=20,sticky="w")
		value_txt=Entry(Manage_frame,textvariable=self.price_var,width=15,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)	


		lbl_qun=Label(Manage_frame,text="Item quantity",font=("times new roman",18,"bold"),bg=bg_color,fg="red")
		lbl_qun.grid(row=4,column=0,pady=15,padx=20,sticky="w")
		qun_txt=Entry(Manage_frame,textvariable=self.item_quan_var,width=15,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)	


		lbl_tax=Label(Manage_frame,text="tax price",font=("times new roman",18,"bold"),bg=bg_color,fg="red")
		lbl_tax.grid(row=5,column=0,pady=15,padx=20,sticky="w")
		tax_txt=Entry(Manage_frame,textvariable=self.tax_var,width=15,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)	

		# button freame##########################
		but_frame=Frame(Manage_frame,bd=4,relief=RIDGE,bg=bg_color)
		but_frame.place(x=7,y=400,width=430,height=60)

		add_btn=Button(but_frame,text="add",command=self.add_data,width=11).grid(row=0,column=0,padx=10,pady=10)
		update_btn=Button(but_frame,text="update",command=self.updata_data,width=11).grid(row=0,column=1,padx=10,pady=10)
		delet_btn=Button(but_frame,text="delete",command=self.delete_row,width=11).grid(row=0,column=2,padx=10,pady=10)
		clear_btn=Button(but_frame,text="clear",command=self.clear,width=11).grid(row=0,column=3,padx=10,pady=10)


		
		
		#details frame#######################################

		Details_frame=Frame(self.root,bd=4,relief=RIDGE,bg=bg_color)
		Details_frame.place(x=500,y=200,width=990,height=560)		


		lbl_search=Label(Details_frame,text="Search By",bg="orange",fg="white",font=("times new roman",20,"bold"))
		lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

		self.cmb_search = ttk.Combobox(Details_frame,textvariable=self.search_by,width=15,font=("times new roman",15),state='readonly',justify=CENTER) 
		self.cmb_search['values']=("owner_name","category","paramiter","item_name")
		self.cmb_search.grid(row=0,column=1,padx=20,pady=10)
		self.cmb_search.current(0)

		txt_search=Entry(Details_frame,textvariable=self.search_txt,width=15,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=2,padx=10,pady=20)

		search_btn=Button(Details_frame,text="Search",width=15,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
		show_btn=Button(Details_frame,text="show all",width=15,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)
		#table frame############################

		table_frame=Frame(Details_frame,bd=4,relief=RIDGE,bg=bg_color)
		table_frame.place(x=15,y=70,width=950,height=470)


		scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
		scroll_y=Scrollbar(table_frame,orient=VERTICAL)
		self.details_table=ttk.Treeview(table_frame,columns=("id","name","category","paramiter","item_name","value","quantity","tax rate"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)
		scroll_x.config(command=self.details_table.xview)
		scroll_y.config(command=self.details_table.yview)
		self.details_table.heading("id",text="ID.")
		self.details_table.heading("name",text="C_NAME.")
		self.details_table.heading("category",text="Category.")
		self.details_table.heading("paramiter",text="Paramiter.")
		self.details_table.heading("item_name",text="Item Name.")
		self.details_table.heading("value",text="Value.")
		self.details_table.heading("quantity",text="Quantity.")
		self.details_table.heading("tax rate",text="Tax Rate.")
		self.details_table['show']='headings'
		self.details_table.column("id",width=100)
		self.details_table.column("name",width=100)
		self.details_table.column("category",width=100)
		self.details_table.column("paramiter",width=100)
		self.details_table.column("item_name",width=100)
		self.details_table.column("value",width=100)
		self.details_table.column("quantity",width=100)
		self.details_table.column("tax rate",width=100)
		self.details_table.pack(fill=BOTH,expand=1)
		self.fetch_data()
		self.details_table.bind("<ButtonRelease-1>",self.get_curser)

	#insert into tabel database billl-information---------------
	def add_data(self):
		#connection of data base --
		con = sqlite3.connect('bill_store.db')
		#create curser
		c = con.cursor()
		c.execute("INSERT INTO user_details VALUES (:id, :owner_name, :category, :paramiter, :item_name, :price, :quantity, :tax)",
			{    
				'id': None,
				'owner_name':self.name_var.get(),	
				'category':self.cata_var.get(),
				'paramiter': self.para_var.get(),
				'item_name': self.item_name_var.get(),
				'price':self.price_var.get(),
				'quantity':self.item_quan_var.get(),
				'tax':self.tax_var.get()

					
			})
		con.commit()
		self.fetch_data()
		self.clear()				
		con.close()
		messagebox.showinfo("Success","Data Insert Successfull..",parent=self.root)
		
			
    
	def fetch_data(self):
		#connection of data base --
		con = sqlite3.connect('bill_store.db')
		#create curser
		c = con.cursor()
		c.execute("SELECT * FROM user_details")
		rows=c.fetchall()
		if len(rows)!=0:
			self.details_table.delete(*self.details_table.get_children())
			for row in rows:
				self.details_table.insert('',END,values=row)
			con.commit()
		con.close()

	#########clear function-----------------------	

	def clear(self):
		self.name_var.set(" ")
		self.cata_var.set("select")
		self.para_var.set("select")
		self.item_name_var.set(" ")
		self.price_var.set(0)
		self.item_quan_var.set(0)
		self.tax_var.set(0)

	#fectch data using curser-----------------

	def get_curser(self,ev):
		curser_row=self.details_table.focus()
		contents=self.details_table.item(curser_row)
		row=contents['values']
		self.a=self.id_store=row[0]
		#print(self.id_store)
		self.name_var.set(row[1])
		self.cata_var.set(row[2])
		self.para_var.set(row[3])
		self.item_name_var.set(row[4])
		self.price_var.set(row[5])
		self.item_quan_var.set(row[6])
		self.tax_var.set(row[7])

	def updata_data(self):
		#connection of data base --
		con = sqlite3.connect('bill_store.db')
		#create curser
		c = con.cursor()
		c.execute('UPDATE user_details SET  owner_name=? , category=? , paramiter=?, item_name=?, price=?, quantity=?, tax=? WHERE id=?', (self.name_var.get(),self.cata_var.get(),self.para_var.get(),self.item_name_var.get(),self.price_var.get(),self.item_quan_var.get(),self.tax_var.get(),self.a))
		con.commit()
		self.fetch_data()
		self.clear()				
		con.close()
		messagebox.showinfo("Success","Data updated Successfully..",parent=self.root)
		
	def delete_row(self):
		#connection of data base --
		con = sqlite3.connect('bill_store.db')
		#create curser
		c = con.cursor()
		c.execute("DELETE FROM user_details WHERE id=?", (self.a,))
		con.commit()
		self.fetch_data()				
		con.close()
		messagebox.showinfo("Success","Data Deleted Successfully..",parent=self.root)
		

	def search_data(self):
		#connection of data base --
		con = sqlite3.connect('bill_store.db')
		#create curser
		c = con.cursor()
		c.execute("SELECT * FROM user_details WHERE {} LIKE '%{}%'".format(self.search_by.get(), self.search_txt.get()))

		rows=c.fetchall()
		if len(rows)!=0:
			self.details_table.delete(*self.details_table.get_children())
			for row in rows:
				self.details_table.insert('',END,values=row)
			con.commit()
		con.close()


	def billing_window(self):
		self.root.destroy()
		import bill
		
obj=user_page(root)
root.mainloop()