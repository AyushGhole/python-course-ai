#String
word1='I love'   
word2='python'  
a=5
b=3
sum=a+b

#concatecate 
print(word1+word2)

#lenght
print(len(word1)) 

#Slicing  
print(word1[0:3])

#placeholder 
print("{} {}".format(word1, word2)) 
print("Sum of {1} & {0} is {2}.".format(a,b,sum)) 

#lists
marks=[22,52,65,89,73,90,99] 

#slicing 
print((marks[1:5]))

#lists methods 
marks.append(55) #insert at last 
marks.insert(2,95) #insert the value at particular idx
marks.sort() #sort the marks in ascending orders  
marks.reverse() #sort in the reverse 

#loops on lists
for val in marks:
  if(val==99): 
    print("Found")
    break
  else:
    print("Finding...") 

#Dictionaries 
info={
  "name":"Ayush",
  "age":"21", 
  "city":"Mumbai",
  "subjects":["Maths","Physics"]
  }

info.keys() #To return keys of dictionaries
info.values() #To return values of dictionaries
info.items() #To return key value pairs of dictionaries
info.get("city") #To return key a particular value of dictionaries
info.update({
  "class":"B"  #Update a key value pair ib dictoraries
})


#sets
a={1,2,5,6,7,2} 
b={8,9,10}
empty_set= set()
a.add(15) #add a new value into a set 
a.remove(5) #remove a val from a set' 
a.clear() #clears all the val of a set and create a empty set
a.pop() #removes a random value
a.union(b) #combines two sets
(a.intersection(b)) #provides intersection btw two sets 

info={
 ("Alice","Maths"),
 ("Bob","Science"),
 ("Alice","Science"),
 ("Charlie","Maths"),
 ("Bob","Maths"),
 ("Alice","English"),
 ("Charlie","English")
} 

courses = set()
std=set()
students={}
for name,course in info:
  if(students.get(name)==None):
    students.update({name:set()})
    students[name].add(course)
  else:
    students[name].add(course)
print(students)


#Assignment Problems 
#Problem 1
name=input("enter a string: ") 
na=''
ch=len(name)-1 
while(ch>=0):
  na=na+name[ch]
  ch-=1

if(name == na):
  print("Palindrome.") 
else:
  print("Not a Palindrome.") 

# Problem 2
list=[1,3,5,6,7,8] 
sum=0
for val in list:
  sum=sum+val 

avg = sum/len(list) 
print("AVERAGE:{}".format(avg)) 

#Problem 3 
list1=[]
list2=[]
while(True):
 a=(input("enter list number or enter Quit to stop:")) 
 match a:
  case '1':
   while(True):
    num=input("enter number or enter Quit to stop:")
    if(num=='Quit'):
     break
    list1.append(num)
  case '2':
   while(True):
    num=input("enter number or enter Quit to stop:")
    if(num=='Quit'):
     break
    list2.append(num)
  case 'Quit':
   break
  case _:
   break
for val in list2:
 list1.append(val)
 list1.sort()
 
print((list1))


#Problem 4
tup=(1,2,3,4,5,6,7,8) 
even=set() 
odd=set() 
for i in tup:
  if(i%2 == 0):
    even.add(i) 
  if(i%2 != 0):
    odd.add(i) 

print(even," ", odd) 

#Problem 5 
info={}

while(True):
  press=input("enter (A,B,C,D): ") 
  match press:
      case "A":
        name=input("enter name: ") 
        marks=input("enter marks: ")
        if(info.get(name)==None):
           info.update({name:set()})
           info[name].add(marks)
           print("Added Successfully!")
      case "B": 
        name=input("enter name: ") 
        if(info.get(name)):
          marks=input("enter marks: ")
          info[name].add(marks) 
          print("Marks Added!")
        else:
          print("Oops!Press A to add the student.") 
      case "C":
        name=input("enter name: ")
        print(info.get(name))
      case "D":
        print(info)
      
#Problem 6 
words =["apple","banana","kiwi","cherry","mango"] 
dict={} 
for ch in words:
   a=len(ch) 
   if(dict.get(ch)==None):
    dict.update({ch:a}) 
   else:
     dict[ch].add(a)

print(dict) 

#Problem 7 
word=input("Enter a string:") 
count=0
for i in word:
  if(i==" "):
    count+=1

print("No. of Spaces: ",count)

#Problem 8 
list1 ={1,2,3,4 }
list2 ={5,4,7,8} 

if(list1.intersection(list2)): 
  print("Common elements present.") 
else:
  print("No common elements present.")

#Problem 9 
list1=[1,2,2,2,3,5,4,4,6,6] 
a=0
b=len(list1)-1
count=0
for i in list1:
  while(a<=b):
    if(i == list1[a]):
      count=count+1
    a=a+1
  a=0
  if(count > 1):
    print(i)
    count=0
  count=0 

#Problem 10 
str=input("enter string: ") 
a=0
b=len(str)-1
count=0
uni=0
for ch in str:
  while(a<=b):
    if(ch == str[a]):
      count=count+1
    a=a+1
  a=0
  if(count==1):
    print(ch)
    uni = uni +1 
  count=0
print("Count of unique numbers:",uni)