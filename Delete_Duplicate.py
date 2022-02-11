#import Statement if necessary
from sys import * 
import os
import hashlib
import datetime
import time
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import schedule

def ChkLength(x):
	if(len(x) > 1):
		return x;

def DeleteFiles(dict1,Dir_Name):

	OriginalDict = dict1
	results = list(filter(ChkLength,dict1.values()))
	#results = list(filter(lambda x : len(x)>1,dict1.values()))
	iCnt = 0;
	print(len(results))
	if(len(results) > 0):

		for result in results:
			
			for subresult in result:
				iCnt = iCnt + 1;
				
				if(iCnt >= 2):
					
					os.remove(subresult);
			iCnt = 0;
	else:
		print("No Duplicates Are Found")

	PrintResultInFile(OriginalDict,Dir_Name)


def HashFile(path):

	blocksize = 1024;
	afile = open(path,"rb")
	hasher = hashlib.md5()
	buf = afile.read(blocksize);

	while(len(buf) > 0):
		hasher.update(buf)
		buf = afile.read(blocksize)
	afile.close()

	return hasher.hexdigest();


def Travel_Files(FileName,Dir_Name):

	dups = {}
	flag = os.path.isabs(FileName);
	

	if(flag == False):
		path = os.path.abspath(FileName);

	exists = os.path.isdir(path);
	if(exists):

		for dirName,subdirs,fileList in os.walk(path):
			print("Current Folder : ",dirName);
			for filen in fileList:
				path = os.path.join(dirName,filen)
				file_hash = HashFile(path);

				if file_hash in dups:
					dups[file_hash].append(path);
				else:
					dups[file_hash] = [path]
				
	else:
		print("Invalid Path")

	#print(dups)
	DeleteFiles(dups,Dir_Name)


def Sending_Mail(log_path):
	fromaddr = "sharemarket2503@gmail.com"
	toaddr = "omkargodase0@gmail.com"

	msg = MIMEMultipart()
	msg['sharemarket2503@gmail.com'] = fromaddr
	msg['omkargodase0@gmail.com'] = toaddr
	msg['subject'] = "Delete Duplicates Project Information!!"

	body = """
Hello ,
My Name is Omkar Rajendra Godase,
And Herewith, i am sending you a log file and 
In that file, all the Deleted Duplicates
File Names information are Written.

This is the Automatic Generated Mail.
Please Do Not Reply the Same Mail.🙏️

Thanks and Regards,
Omkar Rajendra Godase.😍️

"""
	msg.attach(MIMEText(body, 'plain'))

	attachment = open(log_path, "rb")

	p = MIMEBase('application', 'octet-stream')

	p.set_payload((attachment).read())

	encoders.encode_base64(p)

	p.add_header('Content-Disposition', "attachment; filename= %s" % log_path)

	msg.attach(p)

	s = smtplib.SMTP('smtp.gmail.com', 587)

	s.starttls()

	s.login(fromaddr, "Your Mail Password")

	text = msg.as_string()

	s.sendmail(fromaddr, toaddr, text)

	s.quit()


def PrintResultInFile(dict,DirName):
	results = list(filter(ChkLength,dict.values()))

	
	'''
	if(len(results) > 0):
		print("Duplicate Files Was Present in the Directory");
		print("The List of these Duplicates are : ")
		
		print(FileName)
		str = os.path.abspath(FileName)
		print(str)
		for result in results:
			for subresult in result:
				print("\t%s"%subresult)
	else:
		print("No Duplicates files are Found")

	'''

	
	name = datetime.datetime.now()
	Day = (str)(name.day)
	month = (str)(name.month)
	year = (str)(name.year);
	hour = (str)(name.hour);
	minute = (str)(name.minute);
	second = (str)(name.second);

	FileName = ("Created_File_@"+Day+"-"+month+"-"+year+" "+hour+"-"+minute+"-"+second+".log");
	
	separator = "-" * 85
	File_path = os.path.join(DirName,FileName)
	fd = open(File_path,'w')	
	fd.write(separator+"\n\n");
	fd.write("                              Omkar Godase's Deleted Duplicates File List... \n ");
	fd.write("                              Created @ : "+time.ctime()+"\n\n")
	fd.write(separator+"\n\n")

	if(len(results) > 0):
		
		i = 1;
		for result in results:
			for subresult in result:
				stri = (str)(i); 
				fd.write(" "+stri+"] "+json.dumps(subresult)+"\n\n")
				i = i + 1

		
	else:
		fd.write("\n        No Duplicates files are Found")

	fd.close()
	Sending_Mail(File_path0)
	

def Schedule_Script(Dir_Name,Dir_Name1):
	print("Scheduler starts...");

	schedule.every(1).minute.do(lambda : Travel_Files(Dir_Name,Dir_Name1))

	while (True):
		schedule.run_pending()
		time.sleep(1)


# Entry point of Automation Script
def main():
	print("-------------- Omkar Godase's Automation -------------------")

	print("Script Name : ",argv[0]);
	print("Number of arguments accepted : ",len(argv)-1);

	if(len(argv) >= 3 and len(argv) < 2):
		print("Invalid Number of Arguments");
		exit()

	if(argv[1] == "-u" or argv[1] == "-U"):
		print("Usage : Script is Used to Perform the addition of Two Numbers");

		exit()

	if(argv[1] == "-h" or argv[1] == "-H" ):
		print("Help : Name_of_Script First_Argument Second_Argument");
		print("First_Argument : Name of Directory")
		print("Second_Argument : Name of Directory That we want store record of duplicate files")
		exit()

	try:
		Schedule_Script(argv[1],argv[2])

	except Exception as e:
		print("Error : ",e);


# Starter of the Automation Script
if __name__ == "__main__":
	main()