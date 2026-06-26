
age=int(input("Enter the age: "))  

if(age >= 1 and age<=13): 
  print("Child") 
elif(age>13 and age<=18):
  print("Teenager") 
elif(age>18 and age<=60): 
  print("Adult")  
elif(age > 60 and age <=100): 
  print("Senior Citizen")
else: 
  print("Invlid age")
