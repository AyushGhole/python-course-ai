#if elif else
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
num = int(input("Enter a number: ")) 
if(num % 2 == 0): 
  print("Even") 
else:
  print("Odd")


# match case
color = input("Enter color: ")  
match color: 
  case "Red":
    print("Stop") 
  case "Yellow":
    print("Look") 
  case "Green": 
    print("Go")  
  case _: 
    print("Wrong input") 


#while loop 
count=1 
while count <=5:
  print("Hello World!") 
  count += 1 
num=int(input("Enter number: ")) 
count=1 
while (count <=10):
  print(num,"x",count,"=", num*count) 
  count += 1 
name="Hello" 
for var in name:
  print(var)
for i in range(5):
  print(i+1) 

word ='artificial intellignece' 
ans=0
for ch in word: 
  if(ch == 'i'):
    ans +=1 
print(ans) 

word='artificial'  
ans=0
for ch in word:
  if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
    ans += 1 
print("Vowel Count: ",ans) 
for i in range(2,11,2): 
  print(i) 
n=5
sum=0
for i in range(1,n+1):
  sum += i 
print(sum) 

#functions 
def calc_avg(a,b,c):
  avg=(a+b+c)/3 
  return avg 
a=5
b=6
c=5 
print(calc_avg(a,b,c))  
def calc_fact(n):
  fact=1
  i=1
  while (i <= n):
    fact=fact*i 
    i+=1
  return fact 
print("Factorials:",calc_fact(3))

#Assignment Questions 
#problem 1  
salary=int(input("Enter your salary: ")) 
if (salary <=30000):
  print("Final Tax Rate is 5%") 
elif (salary>30000 and salary<=70000):
  print("Final tax Rate is 15%") 
elif (salary > 70000):
  print("Final Tax Rate is 25%") 
else:
  print("Invalid Number")

#problem 2 
a=int(input("enter 1st number: ")) 
b=int(input("enter 2nd number: "))
for i in range(a, b+1):
  if(i % 2 == 0):
    print(i)
if (a>b):
  print("1st number should not be greater than 2nd number.")

#problem 3 
a=(input("enter digits:")) 
for i in a:
  print(i)

#problem 4 
a=int(input("enter number:")) 
count=0 
while a>0:
  b=a%10
  count+=1 
  a=int(a/10) 
print(count)

#problem 5 
def calc_sum(n):
  sum=0
  i=0
  while (i<=n):
    sum += i 
    i+=1
  return sum
n=int(input("enter number: "))
print("Sum :", calc_sum(n))

#problem 6
for i in range(1, 101):
  if(i % 3 == 0 ):
    print(i," is divisible by 3.")
  if(i % 5 == 0):
    print(i," is divisible by 5.")  

#problem 7 
while True:
  n=(input("Enter number:"))
  if((n) == 'Quit'):
    break
  elif(n>'0'):
    print("Positive") 
  else:
    print("Negative")

#problem 8 
def calculator(a,b,operations):
  match operations:
    case "+":
      print("Results:",a + b) 
    case "-":
      print("Results:",a - b)
    case "*":
      print("Results:",a * b) 
    case "/":
      print("Results:",a / b) 
    case _:
      print("invalid operations.")
a=int(input("enter 1st number:")) 
b=int(input("enter 2nd number:")) 
operation=input("enter operands:") 
calculator(a,b,operation) 

#problem 9 
n=int(input("enter a number:")) 
for i in range(2,n-1):
  if(n % i != 0):
    print("Prime number.")
 

#problem 10 
num=15  
while (True): 
  a=int(input("enter number: "))  
  if(a > num):
    print("Too high!") 
  elif(a<num):
    print("Too low!") 
  else:
    print("Correct!") 
    break

