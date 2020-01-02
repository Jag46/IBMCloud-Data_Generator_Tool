from tkinter import *
import time
import os
import sys
import faker
import barnum
from tkinter import messagebox
from configparser import ConfigParser

module_path = os.path.abspath(os.getcwd())
if module_path not in sys.path:
    sys.path.append(module_path)

from  FileOperations import SaveFile
from Data_Set import FakeData


#Create a window object
app = Tk()
app.title("Test_Data_Generator_Tool By PythonChamps")
app.geometry('900x650')



#Time
localtime = time.asctime(time.localtime(time.time()))

#****Header lines***********
lblInfo = Label(app, font=('arial',30, 'bold'), text="Test Data Generator Tool", fg='Steel Blue')
lblInfo.grid(row=0,column=1)
lblInfo = Label(app, font=('arial',15, 'bold'), text="**** Nationwide Furlough Project ****", fg='Steel Blue')
lblInfo.grid(row=1,column=1)
lblInfo = Label(app, font=('arial',10, 'bold'), text=localtime, fg='Steel Blue',bd=10, anchor='w')
lblInfo.grid(row=2,column=1)

#************adding sections for tool************
records_text = StringVar()
records_label = Label(app, font=('arial',14, 'bold'), text="Please enter number of records *  ", fg='Steel Blue')
records_label.grid(row=4,column=0)
records_entry = Entry(app, font=('arial',14, 'bold'),textvariabl=records_text, bd=10, insertwidth=4,
                    bg="Powder blue")
records_entry.grid(row=4,column=1)

file_text = StringVar()
file_label = Label(app, font=('arial',14, 'bold'), text="Please enter your File name *        ", fg='Steel Blue')
file_label.grid(row=7,column=0)
file_entry = Entry(app, font=('arial',14, 'bold'), textvariabl=file_text, bd=10, insertwidth=4,
                    bg="Powder blue")
file_entry.grid(row=7,column=1,)


columns_text = StringVar()
columns_label = Label(app, font=('arial',14, 'bold'), text="Please enter your columns number *", fg='Steel Blue')
columns_label.grid(row=8,column=0)
columns_entry = Entry(app, font=('arial',14, 'bold'), textvariabl=columns_text, bd=10, insertwidth=4,
                    bg="Powder blue")
columns_entry.grid(row=8,column=1)
info_label = Label(app, font=('arial',10,), text="(* indicates mandatory fields)", fg='Steel Blue')
info_label.grid(row=9,column=0)

#*****columns list*********
columns_list = Listbox(app, height = 30, width = 100, border = 0)
columns_list.grid(row = 13, column = 0, columnspan = 2, rowspan = 8, pady = 20)

scrollbar = Scrollbar(app)
scrollbar.grid(row=13, column=2)

columns_list.configure(yscrollcommand=scrollbar.set)
config = ConfigParser()
config.read("Configuration.cfg")
msg = "**** Please enter your data column numbers in the field- Enter more than 1 by using ',' (comma)****"
columns_list.insert(END, msg)
for data in config.items('DataDetails'):
    msg1 = (data[0] + " =  " + (data[1].replace("_"," ").replace("get","").replace('()','')).capitalize())
    columns_list.insert(END, msg1)
scrollbar.configure(command = columns_list.yview)
def select_item(event):
    global selected_item
    index = columns_list.curselection()[0]
    selected_item = columns_list.get(index)
    columns_entry.insert(selected_item[1])
#Bind select
columns_list.bind('<<ListBoxSelect>>', select_item)


# *********************Take number of records****************************#
def take_number_of_records():
    count = records_text.get()
    try:
        count = int(count)
        
    except:
        messagebox.showerror('Required Fields','Your Number is incorrect, please try again..!')
        exit(0)
    
    return count

def savefilename():
    filename = file_text.get()
    return filename


def take_column_details():
    dataname = columns_text.get()
    allColumns = dataname.split(",")
    for z in range (0, len(allColumns)):
        allColumns[z] = allColumns[z].strip()
    return allColumns

def maindata_loop():
    FakeData.generatedata_data()  

def clear_data():
    records_entry.delete(0,END)
    file_entry.delete(0,END)
    columns_entry.delete(0,END)
    messagebox.showinfo("Info message","Data has been cleared..please try again..!")


#*****adding button function****
generate_button = Button(app, text = 'Clear_Data', width = 12, command = clear_data)
generate_button.grid(row=11, column = 0, pady = 10, padx=50)


generate_button = Button(app, text = 'Generate_Data', width = 12, command = maindata_loop)
generate_button.grid(row=11, column = 1, pady = 10)

app.mainloop()

