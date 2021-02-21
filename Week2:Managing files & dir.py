#practicequiz
Question 1:
  the create_python_script function creates a new python script in the current working directory, 
  adds the line of comments to it declared  by the 'comments' variable, 
  and returns the size of the new file. 
  fill  the gaps to create a script called "program.py".
  
Solution:
import os
def create_python_script(filename):                                     
comments = "# Start of a new Python program"  
with open(filename,"w") as file:    
    file.write(comments)  
filesize =os.path.getsize(filename) 
return(filesize) 
print(create_python_script("program.py"))

Output: 31
***********************************************************************************
Question 2:
the new_directory function creates a new directory inside the current working directory, 
then creates a new empty file inside the new directory, and returns the list of files in that directory.
fill in the gaps to create a file "script.py" in the directory "PythonPrograms". 

Solution:
import os 
def new_directory(directory, filename):  
# Before creating a new directory, check to see if it already exists  
if os.path.exists(directory) == False:    
    os.mkdir(directory)   
# Create the new file inside of the new directory  
os.chdir(directory)  
with open(filename,'w') as file:    
     file.write("")  
os.chdir("..") 
varn=os.listdir(directory)  
# Return the list of files in the new directory  
return varn 

print(new_directory("PythonPrograms", "script.py"))

Output:
  
['script.py']
************************************************************************************
Question 4:
the file_date function creates a new file in the current working directory, 
checks the date that the file was modified, and returns just the date portion 
of the timestamp in the format of yyyy-mm-dd. Fill in the gaps to create a 
file called "newfile.txt" and check the date that it was modified.

Solution:
import os
import datetime
def file_date(filename):  
# Create the file in the current directory  
file=open(filename,'w')  
timestamp = os.path.getmtime(filename)  
# Convert the timestamp into a readable format, then into a string  
times=datetime.datetime.fromtimestamp(timestamp)  
# Return just the date portion   
# Hint: how many characters are in “yyyy-mm-dd”?   
return ("{}".format(times.strftime("%Y-%m-%d"))) 
print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd

Output:
2021-02-21
***********************************************************************************
Question5:
the parent_directory function returns the name of the directory that's located
just above the current working directory. Remember that '..' is a relative path 
alias that means "go up to the parent directory". Fill in the gaps to complete 
this function.

Solution:
import os
def parent_directory():  
# Create a relative path to the parent   
# of the current working directory   
relative_parent = os.path.join(os.getcwd(), "..")   
# Return the absolute path of the parent directory  
return os.path.abspath(relative_parent) 
print(parent_directory())

Output:
/

