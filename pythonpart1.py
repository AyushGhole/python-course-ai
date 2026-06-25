#variables
a=10
b=5 

#print(type(isPrime)) type and how single line comment is written in python
''' this is a multi-line comment '''


#Arthimetic Operators
(a+b) #sum 
(a-b) #subtract 
(a*b) #multiply
(a/b) #division 
(a%b) #modulo 
(a**b) #power 

#Relational Operators 
(a>b)
(a==b) 
(a!=b)
(a>=b) 


#Assignment Operators
a=b
a+=b
a-=a
a*=2
a/=3


#Logical Operators 
isCheck = False 
(not isCheck) #not
((3>2) and (5>3)) #and 
((3<4) or (3<2)) #or 


#Type Conversion 
sum=int(5 + 10.0) 
a=bool(12)
type(a)


#How to take Input  
#input function always contains a str  
# a= float(input("Enter a number: "))
# b= float(input("Enter a number : "))
avg = (a+b)/2 
sum= a+b 
diff= a-b
mul= a*b
div= a/b
quo= a//b 


#Assignment problems 
#problem1
#first_name=input("Enter your name: ")
#age=input("Enter your age: ") 
#print("Hello", first_name,", you are", age,"years old!") 

#problem 3 
# int1=int(input("Enter 1st integers: ")) 
# int2=int(input("Enter 2nd integers: ")) 
# float1=float(input("Enter a floating number:")) 
# float(int1)
# float(int2) 
# print((int1 + int2 + float1)/3)

#problem 4 
# num=input("Enter a number: ") 
# print(type(num), num)
# num=int(num)
# print(type(num), num)  
# num=float(num) 
# print(type(num), num) 

#problem 5
# x=10+3*2**2
# print(x) 

#problem 6 
# a=input("Enter 1st number: ") 
# b=input("Enter 2nd number: ") 
# print("Before Swapping: A =" ,a, ", B=",b)
# temp=a 
# a=b 
# b=temp 
# print("After Swapping: A =",a,", B =",b) 

#problem 7 
# temp=float(input("Enter temperature:"))
# FahrenheitTemp= (temp * (9/5)) + 32
# print("Fahrenheit Temperature:", FahrenheitTemp) 

# problem 8 
# radius=float(input("Enter a radius: ")) 
# pi=3.14 
# Area=pi * radius * radius 
# print("Area : ", Area)


#problem 9 
# principal= float(input("Enter principle: ")) 
# rate= float(input("Enter rate: ")) 
# time= float(input("Enter time: ")) 
# SI= (principal * rate * time)/100 
# print("Simple Interest: ", SI) 

#problem 10 
# num=45.78 
# integer=int(num // 1)
# fract=(num - integer)
# print("Integer :", integer," Fractional :",fract)