#File O/P
# f=open("sample.txt", "r")  #Open file in read mode  
# f=open("sample.txt", "w")  #Open file in write mode  
# f=open("sample.txt", "a")  #Open file in append mode 
# f=open("sample1.txt", "x")  #Open file in create new file mode 
# f=open("sample1.txt", "w+")  #Open file allowing to enter numbers as well 
# data = f.read()  #Read file 
# data=f.readline()  #Read file line by line.
# f.write("Text 2 overwrite \n the complete data.")  # overwrites the file data 
# f.write("123")
# print(f.read())
# f.close()  #Close file

# with open("sample.txt", "r") as f:
  # print(len(f.read()))

# import os 
# os.remove("sample1.txt")  #to delete files 

data=True
line=0
with open("sample.txt", "r") as f:
  while data:
   data=f.readline() 
   if("python" in data):
     print(f"Word found at line={line}")
     break
   line+=1