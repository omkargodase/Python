##################################################################################
# Required Python Packages
##################################################################################

import os
from sys import *

##################################################################################
# Function Name : TraverseDir
# Description 	: Travels Whole Directory Including Subdirectories & Files
# Input 		: Absolute Path Of Directory Through Command Line
# Output 		: Names Of Folders, Subfolders & Files 
# Author 		: Omkar Rajendra Godase
# Date 			: 07/03/2022  
##################################################################################

def TraverseDir(path):
	flag = os.path.isabs(path)

	if flag == False:
		path = os.path.abspath(path)

	Exists = os.path.isdir(path)


	if Exists:

		for foldername,subfolder,filename in os.walk(path):
			print("CURRENT FOLDER IS :"+foldername)

			for subf in subfolder:
				print("SUBFOLDER OF "+foldername+" IS :"+subf)

			for filen in filename:
				print("FILE INSIDE "+foldername+" IS :"+filen)
			print('')

	else:
		print("NO SUCH DIRECTORY FOUND")

##################################################################################
# Function Name : Main
# Description 	: Main Function From Where Execution Starts
# Author 		: Omkar Rajendra Godase
# Date 			: 07/03/2022  
##################################################################################

def main():
	print("@@@@@@@@@@ SCRIPT TO TRAVERSE DIRECTORY @@@@@@@@@@")

	print("The Name Of Script :",argv[0])

	if(len(argv)  > 3) or (len(argv) < 2):
		print("INVALID DIRECTORY NAME")
		print("Note : You Trying To Enter More Than One Directory Path")
		exit()

	if(argv[1] == "-U") or (argv[1] == "-u"):
		print("USAGE : This Script Is Used To Traverse Directory")
		exit()
		
	if(argv[1] == "-H") or (argv[1] == "-h"):
		print("HELP : Please Enter The Path Of Directory Inside Double Quotes")
		exit()

	try:
		TraverseDir(argv[1])

	except ValueError:
		print("Error : Invalid Datatype Of Input")

	except Exception as e:
		print(e)
		
##################################################################################
# Function Name : Starter Of Program
##################################################################################

if __name__ == "__main__":
	main()