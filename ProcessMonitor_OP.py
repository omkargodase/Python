##################################################################################
# Required Python Packages
##################################################################################

import psutil

##################################################################################
# Function Name : ProcessDisplay
# Description   : Display Current Running Process On Local Machine
# Author        : Omkar Rajendra Godase
# Date          : 17/02/2022  
##################################################################################

def ProcessDisplay():
    listprocess = []

    for Proc in psutil.process_iter():
        try:
            Pinfo = Proc.as_dict(attrs = ['pid','name','username'])

            listprocess.append(Pinfo)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listprocess

##################################################################################
# Function Name : Main
# Description   : Main Function From Where Execution Starts
# Author        : Omkar Rajendra Godase
# Date          : 07/01/2022  
##################################################################################

def main():
    print("OMII GODASE : PYTHON AUTOMATION AND MACHINE LEARNING")

    print("Process Monitor")

    listprocess = ProcessDisplay()

    for Elem in listprocess:
        print(Elem)

##################################################################################
# Function Name : Starter Of Program
##################################################################################

if __name__ == "__main__":
    main()