##################################################################################
# Required Python Packages
##################################################################################

import os
from sys import *
import hashlib

##################################################################################
# Function Name : hashfile
# Description 	: To Create The Hashfile Of Input File
# Input 		: File Path & Blocksize
# Output 		: Returns Hashcode 
# Author 		: Omkar Rajendra Godase
# Date 			: 03/03/2022  
##################################################################################

def hashfile(path, blocksize = 1024):
	with open(path, 'rb') as afile:
		hasher = hashlib.md5()
		buf = afile.read(blocksize)
		while len(buf) > 0:
			hasher.update(buf)
			buf = afile.read(blocksize)

		return hasher.hexdigest()

##################################################################################
# Function Name : FindChecksum
# Description 	: To Create The Checksum Of Input File
# Input 		: File Path
# Output 		: Generates Checksum 
# Author 		: Omkar Rajendra Godase
# Date 			: 03/03/2022  
##################################################################################

def FindChecksum(path):
	flag = os.path.isabs(path)

	if flag == False:
			path = os.path.abspath(path)

	Exists = os.path.isdir(path)

	if Exists:
		for foldername,subfolder,filename in os.walk(path):
			print("CURRENT FOLDER IS :"+foldername)
		for filen in filename:
			path = os.path.join(foldername,filen)
			file_hash = hashfile(path)
			print("\n",path)
			print("THE CHECKSUM OF "+filen+" IS :")
			print(file_hash)

		print('')
	
	else:
		print("INVALID PATH")

##################################################################################
# Function Name : Main
# Description 	: Main Function From Where Execution Starts
# Author 		: Omkar Rajendra Godase
# Date 			: 03/03/2022  
##################################################################################



def main():
	print("@@@@@@@@@@ SCRIPT TO CALCULATE MD5 CHECKSUM OF FILE @@@@@@@@@@")

	print("The Name Of Script :",argv[0])

	if(len(argv) != 2):
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

		FindChecksum(argv[1])

	except ValueError:
		print("Error : Invalid Datatype Of Input")

	except Exception as e:
		print(e)

##################################################################################
# Function Name : Starter Of Program
##################################################################################

if __name__ == "__main__":
	main()