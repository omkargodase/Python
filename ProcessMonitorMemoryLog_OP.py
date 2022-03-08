##################################################################################
# Required Python Modules
##################################################################################

import psutil
import os
import time
import datetime
import json
from sys import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import schedule

##################################################################################
# Function Name : ProcessDisplay
# Description   : Automatically Creates Text File & Writes Current Running Process In That File 
# Author        : Omkar Rajendra Godase
# Date          : 18/02/2022  
##################################################################################

def ProcessDisplay(log_dir = "OMII"):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
            print("Dictionary Created")

        except:
            pass

    name = datetime.datetime.now()
    Day = (str)(name.day)
    month = (str)(name.month)
    year = (str)(name.year);
    hour = (str)(name.hour);
    minute = (str)(name.minute);
    second = (str)(name.second);

    FileName = ("Process_Log@"+Day+"-"+month+"-"+year+" "+hour+"-"+minute+"-"+second+".log");
    
    separator = "-" * 85
    File_path = os.path.join(log_dir,FileName)
    fd = open(File_path,'w')    
    fd.write(separator+"\n\n");
    fd.write("                              Omkar Godase's Process Monitor Memory Log... \n ");
    fd.write("                              Created @ : "+time.ctime()+"\n\n")
    fd.write(separator+"\n\n")

    for Proc in psutil.process_iter():
        try:
            Pinfo = Proc.as_dict(attrs = ['pid','name','username'])
            
            vms = Proc.memory_info().vms / (1024 * 1024)
            
            Pinfo['vms'] = vms

            listprocess.append(Pinfo)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    i = 1
    for element in listprocess:
        stri = (str)(i)
        fd.write(" "+stri+"] "+json.dumps(element)+"\n\n")
        i = i + 1
    fd.close()

##################################################################################
# Function Name : Main
# Description   : Main Function From Where Execution Starts
# Author        : Omkar Rajendra Godase
# Date          : 18/02/2022  
##################################################################################

def main():
    print("-------------- Omkar Godase's Process Memory Logger -------------------")

    print("Script Name : ",argv[0]);
    print("Number of arguments accepted : ",len(argv)-1);

    if(len(argv) != 2):
        print("Invalid Number of Arguments");
        exit()

    if(argv[1] == "-u" or argv[1] == "-U"):
        print("Usage : This Script Is Used Log Record Of Running Processes")

        exit()

    if(argv[1] == "-h" or argv[1] == "-H" ):
        print("Help : Please Provide Absolute Path Of Directory")
        exit()

    try:
        ProcessDisplay(argv[1])

    except ValueError:
        print("Error : Invalid Datatype Of Input")

    except Exception as e :
        print(e)

##################################################################################
# Function Name : Starter Of Program
##################################################################################

if __name__ == "__main__":
    main()