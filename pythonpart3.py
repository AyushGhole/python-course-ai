#String
word1='I love'   
word2='python'  
a=5
b=3
sum=a+b

#concatecate 
# print(word1+word2)

#lenght
# print(len(word1)) 

#Slicing  
# print(word1[0:3])

#placeholder 
# print("{} {}".format(word1, word2)) 
# print("Sum of {1} & {0} is {2}.".format(a,b,sum)) 

#lists
marks=[22,52,65,89,73,90,99] 

#slicing 
# print((marks[1:5]))

#lists methods 
marks.append(55) #insert at last 
marks.insert(2,95) #insert the value at particular idx
marks.sort() #sort the marks in ascending orders  
marks.reverse() #sort in the reverse 

#loops on lists
# for val in marks:
#   if(val==99): 
#     print("Found")
#     break
#   else:
#     print("Finding...") 

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
# a.clear() #clears all the val of a set and create a empty set
# a.pop() #removes a random value
a.union(b) #combines two sets
(a.intersection(b)) #provides intersection btw two sets 

# info={
#  ("Alice","Maths"),
#  ("Bob","Science"),
#  ("Alice","Science"),
#  ("Charlie","Maths"),
#  ("Bob","Maths"),
#  ("Alice","English"),
#  ("Charlie","English")
# } 

# courses = set()
# std=set()
# students={}
# for name,course in info:
#   if(students.get(name)==None):
#     students.update({name:set()})
#     students[name].add(course)
#   else:
#     students[name].add(course)
# print(students)