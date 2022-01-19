#This program is for find some strng in set of files in a folder
#Specify the search string in keyword section
#You can add multiple OR condtion for defferent file extensions
#This program will perform a search with the keyword in all the files with the specific extension filter in the given folder path
import re
import hjson
import os


for subdir, dirs, files in os.walk("<<Folder path contains files to search>>"):
    for file in files:
        fileName=os.path.join(subdir, file)
        if(fileName.endswith("<<file extension>>") or fileName.endswith("<<File extensions>>") ):
            f1 = open(fileName, "r", encoding='utf-8')
            code = f1.read()
            result = re.findall("<<Keyword to search>>", code)
            if (result):
                print(fileName)
