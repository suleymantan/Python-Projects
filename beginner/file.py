"""
Reading from a File: Read data from a text file.
Writing to a File: Write data to a text file.
Copying a File: Copy the contents of one file to another.
Counting Words in a File: Count the number of words in a text file.
Finding Specific Words in a File: Find specific words in a text file.
Storing Data in a File: Store data (e.g., from a program) in a file.
Reading and Writing CSV Files: Work with CSV files.
Reading and Writing JSON Files: Work with JSON files.

"""
#Reading from a File: Read data from a text file.
#f = open("text.txt","r")
#print(f.read())
#print(f.read(5))
#print(f.readline())
#for i in f:
#   print(i)

#print(f.readlines())
    
#f.close()

#Writing to a File: Write data to a text file.
#f = open("file2.txt", "a")
#f.write("This is first .txt")
#f.close()

#f = open("file2.txt","r")
#print(f.read())

# 'x' return error if file is exist
#x = open("file2.txt",'x')
#x = open("flie3.txt","x")

# delete file
#import os
#if os.path.exists("file3.txt"):
 #   os.remove("file3.txt")
#else:
#    print("The file does not exist")

# if use this mode , it will close automatic
"""with open("openclosed.txt","w+") as file:
    content = file.write("If we usu this mode, this mode will closed automatic")
    
with open("openclosed.txt","r+") as file:
    read_content = file.read()
    print(read_content)
    
try:
    file = open("openclosed.txt","r")
    read_file = file.read()
    print(read_file)
finally:
    file.close()"""


#Copying a File: Copy the contents of one file to another.
"""import os
import shutil

path = "D:/new/"
print(os.listdir(path))

fname = "text.txt"
fdest = "D:/new_copy/"
froot = path+fname
try:
    shutil.copy(froot,fdest)
except Exception as e:
    print(e)"""
"""*************************************************************************************"""
"""with open("text.txt", "r+") as file:
    for i in file:
        with open("text_copy.txt","a") as file_copy:
            file_copy.write(i)"""

#Counting Words in a File: Count the number of words in a text file.
"""count_word = 0
with open("text.txt",'r+') as file:
    re = file.read()
    re = re.split()
    for i in re:
        count_word +=1
print(count_word)

count_word1 = 0
with open("text.txt",'r+') as file:
    re = file.read()
    re = re.split()
    count_word1 +=len(re)

print(count_word1)"""

#Finding Specific Words in a File: Find specific words in a text file.
"""from collections import Counter
a = ["this","the","their","data",'file']
words = []
with open("text.txt","r") as file:
    re = file.read()
    re = re.split()
    for i in re:
        i= i.lower()
        if i in a:
            words.append(i)

print("Count: {} \nWords: {}".format(len(words), words))       
words = Counter(words)
print(words)"""

#Reading and Writing CSV Files: Work with CSV files.
"""data = ["python","java","c#","c++","julia","php","c","javascript","rust"]
def storing_data(filename,data):
    def write_csv(filename,data):
        with open(filename,"w+") as file:
            for i in data:
                file.writelines(f"{i} \n")
    write_csv(filename,data)
    def read_csv(filename):
        with open(filename) as file:
            rd = file.read()
            print(rd)

    read_csv(filename)

       
    
storing_data("deftext.csv",data)"""

#Reading and Writing JSON Files: Work with JSON files.
"""data = ["python","java","c#","c++","julia","php","c","javascript","rust"]
def storing_data(filename,data):
    def write_csv(filename,data):
        with open(filename,"w+") as file:
            for i in data:
                file.writelines(f"{i} \n")
    write_csv(filename,data)
    def read_csv(filename):
        with open(filename) as file:
            rd = file.read()
            print(rd)

    read_csv(filename)

       
    
storing_data("deftext.json",data)"""

