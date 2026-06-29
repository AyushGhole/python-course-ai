#File O/P
f=open("sample.txt", "r")  #Open file in read mode  
f=open("sample.txt", "w")  #Open file in write mode  
f=open("sample.txt", "a")  #Open file in append mode 
f=open("sample1.txt", "x")  #Open file in create new file mode 
f=open("sample1.txt", "w+")  #Open file allowing to enter numbers as well 
data = f.read()  #Read file 
data=f.readline()  #Read file line by line.
f.write("Text 2 overwrite \n the complete data.")  # overwrites the file data 
f.write("123")
print(f.read())
f.close()  #Close file

with open("sample.txt", "r") as f:
  print(len(f.read()))

import os 
os.remove("sample1.txt")  #to delete files 

data=True
line=0
with open("sample.txt", "r") as f:
  while data:
   data=f.readline() 
   if("python" in data):
     print(f"Word found at line={line}")
     break
   line+=1

#Exception handling
try:
  x=int(input("enter a number:"))
  ans=10/x  

except ZeroDivisionError: 
  print(f"Divide by 0 is not allowed.") 

except ValueError:
  print(f"Invalid Error!!")

else:
  print(f"Answer: {ans}") 

finally:
  print("End of program.")

#list comprehensions
nums=[-1,-2,-4,-5,5,7,7,-3] 
nums=[0 if val < 0 else val for val in nums ]
words=["hello", "python", "apnacollege"] 
words=[val.upper() for val in words] 
print(words)

#Assignments 
#Problem 1 
count=0
with open("names.txt","w") as f:
  while count<5:
   try:
      names=input("enter name: ") 
      f.write(f"{names}\n")
      count+=1 
   except ValueError:
     print("Invalid values") 
f.close()
count=0

with open("names.txt", "r") as f:
  while count<5:
    print(f.readline())
    count+=1
f.close()
count=0

#Problem 2 
with open("sample.txt", "a") as f:
  f.write("Program runs successfully!") 
f.close()

with open("sample.txt", "r") as f: 
  print(f.read()) 
f.close()

#Problem 3
nums=[5 , 10, 15, 20, 25]
nums=[(val-val) if val < 15 else val for val in nums ]
print(nums) 

#Problem 4
import json 

str ={
  "city":["Mumbai", "Chennai", "Kolkata"],
  "isTrue":True
}

# add python dictonary data to json file
with open("cities.json", "w") as f:
  json.dump(str,f)
  print("Data Added Successfully!")
f.close()

# load json data as python dictionary
with open("cities.json", "r") as f:
  data=json.load(f)
  print(data)
f.close()

#Problem 5 
try:
  with open("data.txt", "r") as f:
   print(f.read())
  f.close()
except FileNotFoundError:
  print("File not found!")  
  