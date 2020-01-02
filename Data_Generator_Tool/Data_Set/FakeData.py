import os
import sys
import faker
from tkinter import messagebox

module_path = os.path.abspath(os.getcwd())
if module_path not in sys.path:
    sys.path.append(module_path)
from  FileOperations import SaveFile
from  Generator import AddressDetails
from  Generator import CreditCardDetails
from  Generator import PersonalData
from  Generator import ProfessionalDetails
from  Generator import RandomDetails
from  Generator import BankCustomer
from configparser import ConfigParser
from Data_generator import data_generator
import time

# *********************Configurable Data ******************************** #
config = ConfigParser()
config.read("Configuration.cfg")
configmethod = ConfigParser()
configmethod.read("MethodMapping.cfg")


def generatedata_data():
# *********************Take number of records****************************#
    count= data_generator.take_number_of_records()

#  Take File Name from User
    filename= data_generator.savefilename()

#  Connect with File
    SaveFile.connect_with_file(filename)


    start = time.perf_counter()

    allColumns = data_generator.take_column_details()
    columnCount=len(allColumns)
    counter=0

    for j in allColumns:
        counter=counter+1
        try:
            methodName = config.get('DataDetails',str(j))
            methodName = str(methodName).replace("get_","").replace("()","")
        except:
            messagebox.showerror("error log", "ALERT -  Column number is incorrect")
            exit(0)
        methodName = methodName.capitalize()
        SaveFile.writeDatatoFile(methodName)
        if(counter!=columnCount):
            SaveFile.addLineSeperator()
    SaveFile.switchline()
    SaveFile.saveFile()

    for i in range(1,count+1):
        counter = 0
        for j in allColumns:
            counter = counter + 1
            try:
                methodName = config.get('DataDetails',str(j))
                methodName=configmethod.get('DataDetails',methodName)
            except:
                messagebox.showerror("error log", "ALERT -  Column number is incorrect")
                exit(0)
            result=eval(methodName)
            SaveFile.writeDatatoFile(result)
            if (counter != columnCount):
                SaveFile.addLineSeperator()
        SaveFile.switchline()
    SaveFile.saveFile()
    SaveFile.closeFile()
    print("Time Taken by Script(in seconds) : "+ str(time.perf_counter() - start))
    print( "**************Thanks for using Data Generator tool**************************")
    messagebox.showinfo("Success Message", "Data generated successfully in :"+ str(time.perf_counter() - start))
    time.sleep(10)
