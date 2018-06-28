

# # Collections 




from collections import Counter

c = Counter('abcdaab')

for letter in 'abcde':
    print ('%s : %d' % (letter, c[letter]))


# one method of Counter Class

Counter('abracadabra').most_common(3)

import time
import datetime

print ("Time in seconds since the epoch: %s" %time.time())
print ("Current date and time: " , datetime.datetime.now())
print ("Or like this: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))


print ("Current year: ", datetime.date.today().strftime("%Y"))
print ("Month of year: ", datetime.date.today().strftime("%B"))
print ("Week number of the year: ", datetime.date.today().strftime("%W"))
print ("Weekday of the week: ", datetime.date.today().strftime("%w"))
print ("Day of year: ", datetime.date.today().strftime("%j"))
print ("Day of the month : ", datetime.date.today().strftime("%d"))
print ("Day of week: ", datetime.date.today().strftime("%A"))


# Time is also useful for checking how long some code block takes to run.

start = time.time()
#some code
end = time.time()

print(end-start)


# # Sys

# We can call functions from the command line --> Sublime Text



import sys
#!conda install --yes --prefix {sys.prefix} numpy
# OR

#!{sys.executable} -m pip install numpy   


# ## OS

import os

#os.chdir(path)
#os.fchdir(fd)
os.getcwd()


#Executing a shell command
os.system()    

#Get the users environment 
os.environ()   

#Returns the current working directory.
os.getcwd()   

#Return the real group id of the current process.
os.getgid()       

#Return the current process’s user id.
os.getuid()    

#Returns the real process ID of the current process.
os.getpid()     

#Set the current numeric umask and return the previous umask.
os.umask(mask)   

#Return information identifying the current operating system.
os.uname()     

#Change the root directory of the current process to path.
os.chroot(path)   

#Return a list of the entries in the directory given by path.
os.listdir(path) 

#Create a directory named path with numeric mode mode.
os.mkdir(path)    

#Recursive directory creation function.
os.makedirs(path)  

#Remove (delete) the file path.
os.remove(path)    

#Remove directories recursively.
os.removedirs(path) 

#Rename the file or directory src to dst.
os.rename(src, dst)  

#Remove (delete) the directory path.
os.rmdir(path)    


# ## Pickle


import pickle

a = ['test value','test value 2','test value 3']

file_Name = "testfile"
# open the file for writing
fileObject = open(file_Name,'wb') 

# this writes the object a to the
# file named 'testfile'
pickle.dump(a,fileObject)   

# here we close the fileObject
fileObject.close()
# we open the file for reading
fileObject = open(file_Name,'rb')  
# load the object from the file into var b



b = pickle.load(fileObject)  

print(a == b)




