from tkinter import *
import tkinter as tk
from tkinter.ttk import Treeview
from tkinter import messagebox
from tkinter import ttk
from tkinter import Label
from tkinter.ttk import Combobox
import mysql.connector
import tkinter.messagebox
from tkinter import PhotoImage,OptionMenu, StringVar
from PIL import ImageTk,Image 
import tkinter as tk
from tkinter import ttk, messagebox, Toplevel, BOTH

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '0806@sree',
	database='unitrade'
)
conn1 = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '0806@sree',
	database='categories'
)
cursor = conn.cursor()
cursor.execute('create database if not exists unitrade')
cursor.execute('use unitrade')

cursor1 = conn1.cursor()
cursor1.execute('create database if not exists categories')
cursor1.execute('use categories')

root = Tk()
root.title("Home Screen")

x = (root.winfo_screenwidth() - 500 )// 2
y = (root.winfo_screenheight() - 500) // 2
x=-10
y=0
root.geometry(f"1550x840+{x}+{y}")
global flag
flag = 0
def hii():
	buywin.destroy()
from tkinter import messagebox

# ... (previous code)
def show_next_page(item_name):
	next_page = Toplevel(root)
	next_page.title("Item Selected")
	next_page.geometry(f"1550x840+{x}+{y}")
	img11=Image.open('thankyou.jpg')
	temp11=img11.resize((1600,1000))
	photo11=ImageTk.PhotoImage(temp11)
	Lb11=Label(next_page,image=photo11)
	Lb11.image=photo11
	Lb11.place(x=0,y=0)
	label = Label(next_page, text=f"Your item '{item_name}' is selected for purchasing.Please contact admin for further information", font=("Helvetica", 16))
	label.pack(pady=20)
	button = Button(next_page, text="OK", command=next_page.destroy)
	button.pack(pady=10)

def buy_item(tree, cate, selected_item):
    if selected_item:
        item_name = tree.item(selected_item, "values")[0]
        confirmation = messagebox.askyesno("Confirm Purchase", f"Do you want to buy {item_name}?")
        if confirmation:
            show_next_page(item_name)
          #tree.item(selected_item, tags=('sold',))
            # Additional code for deleting item from database and updating UI if needed
          #messagebox.showinfo("Success", f"{item_name} has been bought.")
			
			
			# cursor1.execute(f"DELETE FROM {cate} WHERE item_name = '{item_name}'")
            # conn1.commit()
            # messagebox.showinfo("Success", f"{item_name} has been bought.")
            # tree.delete(selected_item)
        else:
            messagebox.showinfo("Cancelled", "Purchase cancelled.")
    else:
        messagebox.showinfo("No Item Selected", "Please select an item before buying.")


# def proceeds(e):
# 	global drop_down2
# 	cate = drop_down2.get()
# 	drop_down2.destroy()
# 	cursor1.execute(f"select * from {cate}")
# 	t = cursor1.fetchall()
# 	# columns = ("Name", "Price", "Description","email")
# 	columns = ("Name", "Price", "Description","email","username")
	
# 	style = ttk.Style()
# 	#style.configure("Treeview", highlightthickness=0, bd=1)
# 	style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))
# 	#style.map("Treeview", background=[("selected", "#BFBFBF")], fieldbackground=[("selected", "#BFBFBF")])

# 	tree = ttk.Treeview(buyframe, columns=columns, show="headings")
# 	for col in columns:
#     		tree.heading(col, text=col)
# 	for i in range(0,4):
#     		tree.column(columns[i], width=100)
# 	for i in t:
# 		it = i + (tree.column(columns[4]),)
# 		tree.insert('', 'end', values=it)
# 	tree.column("Description", width=500)
# 	tree.column("email", width=150)
# 	def on_item_selected(event):
# 		selected_item = tree.selection()
# 		buy_item(tree, cate, selected_item)
# 	tree.bind("<ButtonRelease-1>", on_item_selected)
# 	tree.pack()
# 	buywin.protocol("WM_DELETE_WINDOW",hii)

def proceeds(e):
    global drop_down2
    cate = drop_down2.get()
    drop_down2.destroy()
    cursor1.execute(f"select * from {cate}")
    t = cursor1.fetchall()
    columns = ("Name", "Price", "Description", "email", "username","ID")

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))

    tree = ttk.Treeview(buyframe, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    tree.column("Description", width=500)
    tree.column("email", width=150)
    
    for i in t:
        tree.insert('', 'end', values=i)

    def on_item_selected(event):
        selected_item = tree.selection()
        buy_item(tree, cate, selected_item)

    tree.bind("<ButtonRelease-1>", on_item_selected)
    tree.pack()
    buywin.protocol("WM_DELETE_WINDOW", hii)

def buyy():
	global drop_down2,buyframe,buywin
	root.withdraw()
	buywin = Toplevel(root)
	buywin.title("Sell")
	x = -10
	y = 0
	buywin.geometry(f"1550x840+{x}+{y}")
	img14=Image.open('back.jpg')
	temp14=img14.resize((1600,1000))
	photo14=ImageTk.PhotoImage(temp14)
	Lb14=Label(buywin,image=photo14)
	Lb14.image=photo14
	Lb14.place(x=0,y=0)
	

	buyframe=Frame(buywin,bg='white',width='1300',height='670')
	buyframe.place(x=120,y=80)
	
	img16=Image.open('choose.jpg')
	temp16=img16.resize((600,600))
	photo16=ImageTk.PhotoImage(temp16)
	Lb16=Label(buyframe,image=photo16)
	Lb16.image=photo16
	Lb16.place(x=20,y=0,width=600,height=600)
	
	txt6 = 'Choose category'
	head6=Label(buyframe,text=txt6,font=('yu gothic ui',25,'bold'),bg='white' ,fg='violet')
	head6.place(x=700,y=40,width=500,height=50)
	

	img15 = Image.open('logback.jpg')
	temp15 = img15.resize((600,500))
	photo15=ImageTk.PhotoImage(temp15)
	Lb15=Label(buyframe,image=photo15)
	Lb15.image=photo15
	Lb15.place(x=670,y=105,width=530,height=450)


	cursor1.execute("select * from category")		
	l = cursor1.fetchall()
	categories = [i[0] for i in l]
	drop_down2 = ttk.Combobox(buyframe,values = categories)
	drop_down2.current(0)
	drop_down2.place(x=800,y=200)
	drop_down2.bind("<<ComboboxSelected>>",proceeds)


def selll():
    root.withdraw()
    sellwin = Toplevel(root)
    sellwin.title("Sell")
    x = -10
    y = 0
    sellwin.geometry(f"1550x840+{x}+{y}")
    img11 = Image.open('back.jpg')
    temp11 = img11.resize((1600, 1000))
    photo11 = ImageTk.PhotoImage(temp11)
    Lb11 = Label(sellwin, image=photo11)
    Lb11.image = photo11
    Lb11.place(x=0, y=0)
    
    sellframe = Frame(sellwin, bg='white', width='1300', height='670')
    sellframe.place(x=120, y=80)
    
    img12 = Image.open('choose.jpg')
    temp12 = img12.resize((600, 600))
    photo12 = ImageTk.PhotoImage(temp12)
    Lb12 = Label(sellframe, image=photo12)
    Lb12.image = photo12
    Lb12.place(x=20, y=0, width=600, height=600)
    
    txt4 = 'Choose category'
    head4 = Label(sellframe, text=txt4, font=('yu gothic ui', 25, 'bold'), bg='white', fg='violet')
    head4.place(x=700, y=40, width=500, height=50)
    
    img13 = Image.open('logback.jpg')
    temp13 = img13.resize((600, 500))
    photo13 = ImageTk.PhotoImage(temp13)
    Lb13 = Label(sellframe, image=photo13)
    Lb13.image = photo13
    Lb13.place(x=670, y=105, width=530, height=450)
    
    def addcategory():
        global label1, entry1, addcat
        drop_down.destroy()
        head4.destroy()
        addbutton.destroy()
        reply1 = messagebox.showinfo("", "Category Not found \n No worries Add Yours")
        if reply1:
            label1 = Label(sellframe, text="Specify your Category:", font=("Arial", 15))
            label1.place(x=730, y=200)
            label1.config(bg="#d8b9e2")
            entry1 = Entry(sellframe, width=30)
            entry1.place(x=980, y=210)
            entry1.config(fg="black", bg="lavender", bd=2, relief="raised", highlightbackground="purple1")
            addcat = Button(sellframe, text="ADD", padx="25", pady="15", command=additem)
            addcat.place(x=950, y=340)
            addcat.config(fg="white", bg="purple1", width=15)
    
    global addbutton
    addbutton = Button(sellframe, text="Other", padx="25", pady="8", command=addcategory)
    addbutton.place(x=1020, y=450)
    addbutton.config(fg="white", bg="purple1")

    def additemm():
        id1 = id_entry.get()
        x1 = name_entry.get()
        x2 = price_entry.get()
        x3 = des_entry.get()
        x4 = email_entry.get()
        cursor1.execute(f"INSERT INTO {temp} (item_name, item_prize, item_des, email, name, id) VALUES (%s, %s, %s, %s, %s, %s)", (x1, x2, x3, x4, uname, id1))
        conn1.commit()
        reply = messagebox.showinfo("Success", "Item added!!!")
        if reply:
            sellwin.destroy()
            if flag == 0:
                logwin.destroy()
            else:
                signwin.destroy()
            decwin.deiconify()
    
    def selectitem(itemm):
        global id_entry, name_entry, price_entry, des_entry, email_entry, temp, name_label, price_label, des_label, email_label, addbutton
        temp = itemm
        
        cursor1.execute(f"CREATE TABLE IF NOT EXISTS {temp} (item_name VARCHAR(50), item_prize INT, item_des VARCHAR(200), email VARCHAR(100), name VARCHAR(200), id INT AUTO_INCREMENT PRIMARY KEY)")
        conn1.commit()

        txt6 = 'Please fill in'
        head6 = Label(sellframe, text=txt6, font=('yu gothic ui', 25, 'bold'), bg='white', fg='violet')
        head6.place(x=700, y=40, width=500, height=50)
        
        id_label = Label(sellframe, text="Item ID:", font=("Arial", 15))
        id_label.place(x=750, y=175)
        id_label.config(bg="#d8b9e2")
        id_entry = Entry(sellframe, width=20)
        id_entry.place(x=940, y=175)
        id_entry.config(fg="black", bg="lavender", bd=2, relief="raised", highlightbackground="purple1")

        name_label = Label(sellframe, text="Item name:", font=("Arial", 15))
        name_label.place(x=750, y=260)
        name_label.config(bg="#d8b9e2")
        name_entry = Entry(sellframe, width=20)
        name_entry.place(x=940, y=260)
        name_entry.config(fg="black", bg="lavender", bd=2, relief="raised", highlightbackground="purple1")
        
        price_label = Label(sellframe, text="Item price:", font=("Arial", 15))
        price_label.place(x=750, y=345)
        price_label.config(bg="#d8b9e2")
        price_entry = Entry(sellframe, width=20)
        price_entry.place(x=940, y=345)
        price_entry.config(fg="black", bg="lavender", bd=2, relief="raised", highlightbackground="purple1")
        
        des_label = Label(sellframe, text="Item description:", font=("Arial", 15))
        des_label.place(x=750, y=430)
        des_label.config(bg="#d8b9e2")
        des_entry = Entry(sellframe, width=20)
        des_entry.place(x=940, y=430)
        des_entry.config(fg="black", bg="lavender", bd=2, relief="raised", highlightbackground="purple1")
        
        email_label = Label(sellframe, text="Email:", font=("Arial", 15))
        email_label.place(x=750, y=515)
        email_label.config(bg="#d8b9e2")
        email_entry = Entry(sellframe, width=20)
        email_entry.place(x=940, y=515)
        email_entry.config(fg="black", bg="lavender", bd=2, relief="raised", highlightbackground="purple1")
        
        addbutton = Button(sellframe, text="ADD", padx="25", pady="15", command=additemm)
        addbutton.place(x=1000, y=540)
        addbutton.config(fg="white", bg="purple1", width=13)
    
    def proceedd(e):
        tem = drop_down1.get()
        drop_down1.destroy()
        head5.destroy()
        selectitem(tem)
    
    def additem():
        global drop_down1, head5
        x = entry1.get()
        cursor1.execute(f"INSERT INTO category (category_name) VALUES (%s)", (x,))
        conn1.commit()
        reply = messagebox.showinfo("Success", "Category added!!!")
        if reply:
            label1.destroy()
            entry1.destroy()
            addcat.destroy()

            txt5 = 'Choose category'
            head5 = Label(sellframe, text=txt5, font=('yu gothic ui', 25, 'bold'), bg='white', fg='violet')
            head5.place(x=700, y=40, width=500, height=50)

            cursor1.execute("SELECT category_name FROM category")
            l = cursor1.fetchall()
            categorie = [i[0] for i in l]
            drop_down1 = ttk.Combobox(sellframe, values=categorie)
            drop_down1.current(0)
            drop_down1.place(x=800, y=200)
            drop_down1.bind("<<ComboboxSelected>>", proceedd)
    
    def proceed(e):
        cate = drop_down.get()
        drop_down.destroy()
        addbutton.destroy()
        head4.destroy()
        selectitem(cate)

    global drop_down
    cursor1.execute("SELECT category_name FROM category")
    l = cursor1.fetchall()
    categorie = [i[0] for i in l]
    drop_down = ttk.Combobox(sellframe, values=categorie)
    drop_down.current(0)
    drop_down.place(x=800, y=200)
    drop_down.bind("<<ComboboxSelected>>", proceed)


def close_all_windows():
	root.destroy()
def buyorsell():
	global decwin
	decwin = Toplevel(root)
	decwin.title("Login")
	x = -10
	y=0
	decwin.geometry(f"1550x840+{x}+{y}")

	img5=Image.open('back.jpg')
	temp5=img5.resize((1600,1000))
	photo5=ImageTk.PhotoImage(temp5)
	Lb5=Label(decwin,image=photo5)
	Lb5.image=photo5
	Lb5.place(x=0,y=0)

	decframe=Frame(decwin,bg='white',width='1100',height='600')
	decframe.place(x=200,y=130)
	
	#txt2 = 'Are you interested in buying or selling today??'
	txt2 = 'Wanna buy or sell??'
	head2=Label(decframe,text=txt2,font=('yu gothic ui',25,'bold'),bg='blueviolet' ,fg='white')
	head2.place(x=700,y=50,width=300,height=50)
	#head2.place(x=700, y=50, width=250, height=50)

# Define the position of the "Profile" button

	img6=Image.open('buysell.jpg')
	temp6=img6.resize((600,600))
	photo6=ImageTk.PhotoImage(temp6)
	Lb6=Label(decframe,image=photo6)
	Lb6.image=photo6
	Lb6.place(x=0,y=0,width=600,height=600)

	img7 = Image.open('logback.jpg')
	temp7 = img7.resize((500,500))
	photo7=ImageTk.PhotoImage(temp7)
	Lb7=Label(decframe,image=photo7)
	Lb7.image=photo7
	Lb7.place(x=650,y=120,width=400,height=400)
	profile_button = Button(decframe, text="Profile", width=10, height=2, command=open_profile)
	profile_button.place(x=1000, y=50)

	buy = Button(Lb7,text = "Buy",width = 22,height = 4,command = buyy)
	sell = Button(Lb7,text = "Sell",width = 22,height = 4,command = selll)

	buy.place(x=110,y=100)
	sell.place(x=110,y=200)
	decwin.protocol("WM_DELETE_WINDOW", close_all_windows)
# def open_profile():
# 	global profile_win
# 	profile_win = Toplevel(decwin)
# 	profile_win.title("Profile")
# 	profile_win.geometry("400x400")  # Adjust the size as needed
	
# 	profile_label = Label(profile_win, text="Profile Page", font=('yu gothic ui', 25, 'bold'))
# 	profile_label.pack(pady=20)
# 	profile_info = Label(profile_win, text=f"Hi, {uname}!", font=('yu gothic ui', 25, 'bold'))
# 	profile_info.pack(pady=10)
# 	#profile_info = Label(profile_win,text=f"Hi, {username}!"")
# 	options = ["Sell list", "Buy List", "Request"]
# 	selected_option = StringVar(profile_win)
# 	selected_option.set(options[0])  # Set default value
# 	dropdown_menu = OptionMenu(profile_win, selected_option, *options)
# 	dropdown_menu.pack(pady=10)
	
# 	close_button = Button(profile_win, text="Close", command=profile_win.destroy)
# 	close_button.pack(pady=20)
# def fetch_all_tables():
#     cursor1.execute("SHOW TABLES")
#     tables = cursor1.fetchall()
#     return [table[0] for table in tables]

# def fetch_sell_list(username):
#     tables = fetch_all_tables()
#     sell_items = []
#     print(tables)
#     for table in tables:
#         cursor1.execute(f"DESCRIBE {table}")
#         columns_info = cursor1.fetchall()
#         columns = [col[0] for col in columns_info]
#         print(columns)
#         if "name" in columns:  # Assuming 'username' is the username column
#             cursor1.execute(f"SELECT * FROM {table} WHERE name='{username}'")
#             rows = cursor1.fetchall()
#             for row in rows:
#                 sell_items.append((table, columns, row))  # Include table name and column names
#     return sell_items

# def display_sell_list(sell_items):
#     sell_list_window = Toplevel(profile_win)
#     sell_list_window.title("Sell List")

#     tree = ttk.Treeview(sell_list_window)
#     tree.pack(expand=True, fill=BOTH)


#     if sell_items:
#     # Extract column names from the first item in sell_items
#      columns = ["Table"] + sell_items[0][1]  
#      tree["columns"] = columns

#     # Set column headings and widths
#      for col in columns:
#         tree.heading(col, text=col)
#         tree.column(col, width=100)

#     # Insert data into the treeview
#      for table, columns, row in sell_items:
#         tree.insert('', 'end', values=(table, *row))
#     else:
#         messagebox.showinfo("Info", "No items found.")


def fetch_all_tables():
    cursor1.execute("SHOW TABLES")
    tables = cursor1.fetchall()
    return [table[0] for table in tables]

def fetch_sell_list(username):
    tables = fetch_all_tables()
    sell_items = []
    print(tables)
    for table in tables:
        cursor1.execute(f"DESCRIBE {table}")
        columns_info = cursor1.fetchall()
        columns = [col[0] for col in columns_info]
        print(columns)
        if "name" in columns:  # Assuming 'username' is the username column
            cursor1.execute(f"SELECT * FROM {table} WHERE name='{username}'")
            rows = cursor1.fetchall()
            for row in rows:
                sell_items.append((table, columns, row))  # Include table name and column names
    return sell_items

def on_row_selected(event):
    selected_item = tree.focus()
    item_details = tree.item(selected_item)
    item_values = item_details['values']
    
    response = messagebox.askyesno("Transaction Confirmation", "Is your transaction completed?")
    if response:
        # Deleting the selected item from the Treeview
        # tree.delete(selected_item)

        # Deleting the item from the respective category table in the database
        table_name = item_values[0]
        primary_key_value = item_values[6]  # Primary key value is the sixth item in item_values (index 5)
        username_value = item_values[5]  # Username value is the fifth item in item_values (index 4)
        print(table_name,primary_key_value,username_value)
        cursor1.execute("SHOW TABLES LIKE 'soldlist'")
        if not cursor1.fetchone():
            cursor1.execute(f"CREATE TABLE soldlist AS SELECT * FROM {table_name} WHERE 1=0")

        # Get column names of the original table
        cursor1.execute(f"DESCRIBE {table_name}")
        columns = [col[0] for col in cursor1.fetchall()]

        # Generate placeholders for the values in the INSERT query
        placeholders = ', '.join(['%s'] * len(columns))

        # Insert the sold item into the soldlist table
        insert_query = f"INSERT INTO soldlist ({', '.join(columns)}) VALUES ({placeholders})"
        sold_item_data = tuple(item_values[1:])  # Exclude the table name
        cursor1.execute(insert_query, sold_item_data)
        conn1.commit()
        delete_query = f"DELETE FROM {table_name} WHERE ID = %s AND name = %s"
        cursor1.execute(delete_query, (primary_key_value, username_value))
        conn.commit()

        messagebox.showinfo("Confirmation", "Transaction marked as completed and item removed from the list.")
    else:
        messagebox.showinfo("Confirmation", "Transaction not completed.")


def display_sell_list(sell_items):
    sell_list_window = Toplevel(profile_win)
    sell_list_window.title("Sell List")

    global tree  # Make tree a global variable to access in the on_row_selected function
    tree = ttk.Treeview(sell_list_window)
    tree.pack(expand=True, fill=BOTH)

    if sell_items:
        # Extract column names from the first item in sell_items
        columns = ["Table"] + sell_items[0][1]  
        tree["columns"] = columns

        # Set column headings and widths
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        # Insert data into the treeview
        for table, columns, row in sell_items:
            tree.insert('', 'end', values=(table, *row))
    else:
        messagebox.showinfo("Info", "No items found.")

    # Bind the selection event to the on_row_selected function
    tree.bind("<<TreeviewSelect>>", on_row_selected)

def fetch_sold_list(username):
    cursor1.execute("SELECT * FROM soldlist WHERE name = %s", (username,))
    return cursor1.fetchall(), [desc[0] for desc in cursor1.description]


def display_sold_list(sold_items,columns):
    sold_list_window = Toplevel(profile_win)
    sold_list_window.title("Sold List")

    global tree  # Make tree a global variable to access in the on_row_selected function
    tree = ttk.Treeview(sold_list_window)
    tree.pack(expand=True, fill=BOTH)

    if sold_items:
        # Extract column names from the first item in sell_items
        # columns = ["Table"] + sold_items[0][1]  
        tree["columns"] = columns

        # Set column headings and widths
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        # Insert data into the treeview
        for row in sold_items:
            tree.insert('', 'end', values=row)
    else:
        messagebox.showinfo("Info", "No items found.")

    # Bind the selection event to the on_row_selected function
    tree.bind("<<TreeviewSelect>>", on_row_selected)

# Assuming profile_win is defined elsewhere in your code
# profile_win = tk.Tk()

# Sample call to display_sell_list function
# username = uname # Replace with actual username
# sell_items = fetch_sell_list(username)
# display_sell_list(sell_items)

# profile_win.mainloop()

def open_profile():
	global profile_win
	profile_win = Toplevel(decwin)
	profile_win.title("Profile")
	profile_win.geometry("1500x1500") 
	img12=Image.open('back.jpg')
	temp12=img12.resize((1600,1000))
	photo12=ImageTk.PhotoImage(temp12)
	Lb12=Label(profile_win,image=photo12)
	Lb12.image=photo12
	Lb12.place(x=0,y=0)
	profile_label = Label(profile_win, text="Profile Page", font=('yu gothic ui', 25, 'bold'))
	profile_label.pack(pady=20)
	profile_info = Label(profile_win, text=f"Hi, {uname}!", font=('yu gothic ui', 25, 'bold'))
	profile_info.pack(pady=10)
	options = ["Sell list", "Sold List", "Request"]
	selected_option = StringVar(profile_win)
	selected_option.set(options[0])  # Set default value
	dropdown_menu = OptionMenu(profile_win, selected_option, *options)
	dropdown_menu.pack(pady=10)

	def on_option_selected(*args):
		if selected_option.get() == "Sell list":
			sell_items = fetch_sell_list(uname)
			display_sell_list(sell_items)
		elif selected_option.get() == "Sold List":
			sold_items, columns = fetch_sold_list(uname)
			display_sold_list(sold_items,columns)
    


	selected_option.trace("w", on_option_selected)
	close_button = Button(profile_win, text="Close", command=profile_win.destroy)
	close_button.pack(pady=20)
		

	#def on_item_click(event):
		#selected_item = tree.item(tree.selection())
		#if selected_item:
			#item_name = selected_item['values'][1]  # Assuming item name is in the second column
            ## Display a pop-up message to ask if the item is selected
			#response = messagebox.askyesno("Item Selection", f"Is '{item_name}' selected?")
			#if response:
			#	print(f"'{item_name}' is selected.")
			#else:
			#	print(f"'{item_name}' is not selected.")
		#if selected_option.get() == "Sell list":
			#sell_items = fetch_sell_list(uname)
			#display_sell_list(sell_items)
	#selected_option.trace("w", on_option_selected)
	#close_button = Button(profile_win, text="Close", command=profile_win.destroy)
	#close_button.pack(pady=20)
	#def close_profile():
		#print("Profile window closed.")
		#profile_win.destroy()

    # Your existing code for GUI elements goes here

    # Debug: Check if the option selected is being traced
	#selected_option.trace("w", on_option_selected)
	#close_button = Button(profile_win, text="Close", command=close_profile)
	#close_button.pack(pady=20)
	#tree = Treeview(profile_win)
	#tree.pack(expand=True, fill='both')
	#tree.bind("<ButtonRelease-1>", on_item_click)
		
def signuppage():
	global signwin
	root.withdraw()
	signwin = Toplevel(root)
	signwin.title("Sign Up")
	x = -10
	y = 0
	signwin.geometry(f"1550x840+{x}+{y}")
	def signupfunction():
		global reply
		user = userentry.get()
		pas = passentry.get()
		emai = emailentry.get()

		cursor.execute(f"INSERT INTO users VALUES ('{user}','{pas}','{emai}')")
		conn.commit()
	
		reply = None
		
		reply = messagebox.showinfo("Success","You are in!!!")
		
		if reply :
			flag = 1
			signwin.withdraw()	
			loginpage()
			
			
	def validate(event = None):
		if(conpassentry.get() and passentry.get() and userentry.get() and emailentry.get()):
			signbutton.config(state= NORMAL)
		else:
			signbutton.config(state = DISABLED)
	
	def check(event = None):
		if (passentry.get() != conpassentry.get()):
			messagebox.showerror("Error","oops!! passwords didn't match")
			conpassentry.delete(0,END)
	img8=Image.open('back.jpg')
	temp8=img8.resize((1600,1000))
	photo8=ImageTk.PhotoImage(temp8)
	Lb8=Label(signwin,image=photo8)
	Lb8.image=photo8
	Lb8.place(x=0,y=0)

	signframe=Frame(signwin,bg='whitesmoke',width='1400',height='700')
	signframe.place(x=75,y=75)
	
	txt3 = 'It\'s time to create your account'
	head3=Label(signframe,text=txt3,font=('yu gothic ui',25,'bold'),bg='blueviolet' ,fg='white')
	head3.place(x=800,y=50,width=500,height=50)

	img9=Image.open('signimg.jpg')
	temp9=img9.resize((600,700))
	photo9=ImageTk.PhotoImage(temp9)
	Lb9=Label(signframe,image=photo9)
	Lb9.image=photo9
	Lb9.place(x=0,y=0,width=600,height=700)
		
	img10 = Image.open('logback.jpg')
	temp10 = img10.resize((650,550))
	photo10=ImageTk.PhotoImage(temp10)
	Lb10=Label(signframe,image=photo10)
	Lb10.image=photo10
	Lb10.place(x=680,y=120,width=650,height=550)
	
	username = Label(Lb10,text = "Username: ",font=("Arial",15))
	username.place(x=100,y=100)
	username.config(bg="purple1")
	userentry = Entry(Lb10,width=25)
	userentry.place(x=350,y=100)
	userentry.bind("<KeyRelease>",validate)
	userentry.config(fg="black",bg="lavender",bd=2)
	password = Label(Lb10,text = "Password: ",font=("Arial",15))	
	password.place(x=100,y=170)
	password.config(bg="purple1")
	passentry = Entry(Lb10,width=25,show="*")
	passentry.config(fg="black",bg="lavender",bd=2)
	passentry.place(x=350,y=170)
	conpassword = Label(Lb10,text = "Confirm Password: ",font=("Arial",15))
	conpassword.place(x=100,y=240)	
	conpassword.config(bg="purple1")
	conpassentry = Entry(Lb10,width=25,show="*")
	conpassentry.place(x=350,y=240)
	conpassentry.bind("<KeyRelease>",validate)
	conpassentry.bind("<FocusOut>",check)
	conpassentry.config(fg="black",bg="lavender",bd=2)
	email = Label(Lb10,text = "email: ",font = ("Arial",16))
	email.place(x=100,y=310)
	email.config(bg="purple1")
	emailentry = Entry(Lb10,width = 25)
	emailentry.place(x=350,y=310)
	emailentry.bind("<KeyRelease>",validate)
	emailentry.config(fg="black",bg="lavender",bd=2)
	signbutton = Button(Lb10,text = "SignUp",padx = "25",pady = "8",state=DISABLED,command = signupfunction)
	signbutton.place(x=370,y=380)	
	signbutton.config(fg="black", bg="purple1",width = 15,height = 1)
def loginpage():
	global logwin
	root.withdraw()
	logwin = Toplevel(root)
	logwin.title("Login")
	x = -10
	y=0
	logwin.geometry(f"1550x840+{x}+{y}")
	def logfunction():
		global logwin,reply,uname
		user = userentry.get()
		pas = passentry.get()
		uname = user
		cursor.execute(f"SELECT * FROM users WHERE user_name = '{uname}'")
		user1 = cursor.fetchone()
    
		reply = None
		if(user1):
			if(user1[1] == pas):
				reply = messagebox.showinfo("Success","logged in!!!")
			else:
				messagebox.showerror("Oops !!! Invalid password")
		else:
			messagebox.showerror("Oops !!! Invalid username")
		if reply :
			flag = 0
			logwin.withdraw()
			buyorsell()
	def validate(event=None):
		if(userentry.get()):# and (len(passentry.get()) > 7)):
		    logbutton.config(state=NORMAL)
		else:
			logbutton.config(state=DISABLED)
	img4=Image.open('back.jpg')
	temp4=img4.resize((1600,1000))
	photo4=ImageTk.PhotoImage(temp4)
	Lb4=Label(logwin,image=photo4)
	Lb4.image=photo4
	Lb4.place(x=0,y=0)

	loginframe=Frame(logwin,bg='white',width='1100',height='600')
	loginframe.place(x=200,y=130)
	
	txt1 = 'WELCOME AGAIN'
	head1=Label(loginframe,text=txt1,font=('yu gothic ui',25,'bold'),bg='blueviolet' ,fg='white')
	head1.place(x=600,y=50,width=400,height=80)

	img3=Image.open('logimg.jpg')
	temp3=img3.resize((600,600))
	photo3=ImageTk.PhotoImage(temp3)
	Lb3=Label(loginframe,image=photo3)
	Lb3.image=photo3
	Lb3.place(x=0,y=0,width=600,height=600)
	

	username = Label(loginframe,text = "Username: ",font=('yu gothic ui',25,'bold'),bg='white' ,fg='purple2')
	username.place(x=650,y=257)

	entry_font = ("Arial", 12)
	userentry = Entry(loginframe,width=20)
	userentry.place(x=850,y=275)
	userentry.config(fg="black",bg="lavender",font = entry_font,bd=2)
	password = Label(loginframe,text = "Password: ",font=('yu gothic ui',25,'bold'),bg='white' ,fg='purple2')
	password.place(x=650,y=337)	
	passentry = Entry(loginframe,width=20,show="*")
	passentry.place(x=850,y=351)
	passentry.config(fg="black", bg="lavender",font = entry_font,bd=2)
	passentry.bind("<KeyRelease>",validate)

	logbutton = Button(loginframe,text = "Login",width = 15,height = 1,padx = "25",pady = "8",state = DISABLED,command = logfunction)
	logbutton.place(x=850,y=450)	
	logbutton.config(fg="black", bg="purple1",font = entry_font)


img1=Image.open('back.jpg')
temp1=img1.resize((1600,1000))
photo1=ImageTk.PhotoImage(temp1)
Lb1=Label(root,image=photo1)
Lb1.image=photo1
Lb1.place(x=0,y=0)#,width=1000,height=1000)

homeframe=Frame(root,bg='white',width='1400',height='700')
homeframe.place(x=75,y=70)
txt='WELCOME TO CAMPUS MART'

head=Label(homeframe,text=txt,font=('yu gothic ui',25,'bold'),bg='white' ,fg='violet')
head.place(x=100,y=50,width=500,height=30)

img2 = Image.open('logback.jpg')
temp2 = img2.resize((500,500))
photo2=ImageTk.PhotoImage(temp2)
Lb2=Label(homeframe,image=photo2)
Lb2.image=photo2
Lb2.place(x=50,y=120,width=500,height=500)

login = Button(Lb2,text = "Login",width = 22,height = 4,command = loginpage)
signup = Button(Lb2,text = "Sign Up",width = 22,height = 4,command = signuppage)

login.place(x=180, y=150)
signup.place(x=180, y=250)

img=Image.open('right.jpg')
temp=img.resize((700,500))
photo=ImageTk.PhotoImage(temp)
Lb=Label(homeframe,image=photo,bg='white')
Lb.image=photo
Lb.place(x=700,y=80,width=700,height=500)

root.mainloop()