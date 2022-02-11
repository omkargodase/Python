from sys import *
import webbrowser
import re
import urllib.request as urllib2

def is_connected():
    try:
        urllib2.urlopen('http://172.217.174.78',timeout=1)
        return True
    except urllib2.URLError as err:
        return False

def Find(string):
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F]))+',string)
    return url

def WebLauncher(path):
    with open(path) as fp:
        for line in fp:
            print(line)
            url = Find(line)
            print(url)
            for str in url:
                webbrowser.open(str, new = 2)

def main():
    print("@@@@@@@@@@@ WEB LAUNCHER BY OMII GODASE @@@@@@@@@@@")

    print("Application Name :"+argv[0])

    if(len(argv) != 2):
        print("INVALID NUMBER OF ARGUMENTS")
        exit()

    if(argv[1] == "-U") or (argv[1] == "-u"):
        print("USAGE : This Script Is Used To Open URL which is written in One File")
        exit()
        
    if(argv[1] == "-H") or (argv[1] == "-h"):
        print("HELP : Please Enter The Name Of File")
        exit()

    try:
        connected = is_connected()

        if connected:
            WebLauncher(argv[1])
        else:
            print("Unable To Connect To Internet...")

    except ValueError:
        print("Error : Invalid Datatype Of Input")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
