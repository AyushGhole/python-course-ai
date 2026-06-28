#OOPS
class student:
  student="Python"  
  college="ABC" 
  year="4th year"

class main:
  def __init__(self):
    print("Constructor was called...")

  def __init__(self,name,cgpa):
    self.name=name     
    self.cgpa=cgpa 

  def get_cpga(self):
    return self.cgpa
  
# std=main("Ayush",9.0) 
# print(f"{std.name} has a cgpa = {std.get_cpga()}")

class Student:
  college_name="ABC College"

  def __init__(self,name,cgpa):
    self.name=name
    self.cpga=cgpa
    self.PI=3.14 

# print(f"{Std.name} has cgpa= {Std.cpga} and {Std.PI}.")

# instance Methods
class Laptop: 
  storage_type="ssd" 

  def __init__(self,RAM,storage): 
    self.RAM=RAM
    self.storage=storage  

#class methods
  @classmethod
  def get_storage_type(cls):
    print(f"storage type= {cls.storage_type}")

  def getinfo(self):
    print(f"Laptop has a {self.RAM} & {self.storage} {self.storage_type}.")

  @staticmethod 
  def calc_discount(price, discount):
    final_price=price-(price-discount*100)
    print(f"Final Price= {final_price}")

# Std=Laptop("16gb", "128gb") 
# Std.calc_discount(40_000,100)

class Online_Store:
  count=0

  def __init__(self, name, price):
    self.name=name
    self.price=price 
    Online_Store.count+=1
  
  #instance methods
  def get_info(self):
    print(f"{self.name} has a Rs.{self.price}")
  
  @classmethod
  def get_count(cls):
    print(f"Total Objects created : {cls.count}")
  
  @staticmethod
  def calc_discount(price,discount):
    final_price = (price - (price*discount/100))
    print(f"Final Price : {final_price}")

# p1=Online_Store("Phone", 100000) 
# p2=Online_Store("Laptop", 300000) 
# p1.calc_discount(p1.price, 12)  

class Bank:
  def __init__(self,account,balance):
    self.account=account 
    self.__balance=balance #encapsulations 
  
  #Getter func 
  def get_balnc(self):
    return self.__balance 
  
  #Setter func 
  def set_balnc(self, newBalncs): 
    self.__balance=newBalncs 
    print(f"{self.__balance}")

acc=Bank("Ayush", 100_000) 
# acc.set_balnc(200_000)
# print(acc.account, acc.get_balnc()) 

#Inheriterance  
class Employee:
  start_time="6am" 
  end_time="9pm" 

  def change_endTime(self, newEndTime): 
    self.end_time=newEndTime
    print(f"{self.end_time}")

class Teacher(Employee):
  def __init__(self, subject):
    self.subject=subject 

# t1=Teacher("Maths") 
# t1.change_endTime("5pm") 
# print(t1.start_time, t1.end_time)

class Teacher:
  def __init__(self, salary): 
    self.salary=salary 
   
class Student:
  def __init__(self,gpa):
    self.gpa=gpa 
    
class TA(Teacher, Student):
  def __init__(self, salary, gpa,name):
    super().__init__(salary)
    Student.__init__(self,gpa) 
    self.name=name 

ta=TA(15_000,9.3,"Ayush")
# print(ta.name, ta.gpa, ta.salary)

# Abstraction 
from abc import ABC , abstractmethod 

class Animal(ABC):
  @abstractmethod
  def make_sound(self):
    pass 

class Lion(Animal):
  def make_sound(self):
    print("Roar") 

class Cow(Animal):
  def make_sound(self):
    print("Meow") 

lion=Lion() 
# lion.make_sound() 

cow=Cow() 
# cow.make_sound() 

#Polymorphism  
class Teacher:
  def get_designation(self):
    print("Desination=Teacher") 

class Account:
  def get_designation(self):
    print("Desination=Accountant") 
  
t1=Teacher() 
# t1.get_designation() 

acc1=Account() 
# acc1.get_designation()

#Assignment
#Problem 1
# class Bank_Account:
#   def __init__(self,acc_number,owner_name,balance):
#     self.acc_number=acc_number 
#     self.owner_name=owner_name 
#     self.balance=balance 

#   def deposit(self,dep):
#     self.balance=self.balance+dep
 
#   def withdraw(self,wtd):
#     self.balance=self.balance-wtd
 
#   def get_balnc(self):
#     print(f"Balance: {self.balance}")

# own=Bank_Account("00091819","Ayush", 25_000)
# own.deposit(13000)
# own.withdraw(20000)
# own.get_balnc()
 
#Problem 2 
# class Book:
#   count=0

#   def __init__(self,author,title):
#     self.title=title 
#     self.__author=author 
#     self.reviews=[] 
   
#   def set(self,newAuthor):
#     self.__author=newAuthor 
#     return print("Auther Set Successfully!")


#   def get(self):
#     return self.__author 

#   def addReviews(self, newReviews):
#     self.reviews.append(newReviews) 
#     print("Review counted successfully")
#     Book.count= Book.count+1 
  
#   def get_reviews(self):
#     return self.reviews

#   @classmethod
#   def get_count(cls):
#     return cls.count

# bk=Book("Ayush","Hell")
# bk.addReviews("Excellent")
# bk.addReviews("Good")
# bk.addReviews("Very Good")
# print("Title: ",bk.title)
# print("Author: ",bk.get()) 
# print("Reviews: ",bk.get_reviews())
# print("Count:",bk.get_count()) 


#Problem 3 
# class Student:
#   def __init__(self):
#     self.__name=None
#     self.__roll=None
#     self.__marks=None

#   def set_marks(self,newMarks):
#     if(newMarks>0):
#       self.__marks=newMarks 
#       print("Marks Added Successfully!!")
#       return self.__marks
#     else:
#       return print("Invalid Marks!") 

#   def set_name(self,newName):
#     if(newName == None):
#       return print("Name cannot be empty!")
#     else :
#       self.__name=newName
#       print("Name Added Successfully!!")   
#       return self.__name 
    
#   def set_roll(self,newRoll):
#     if(newRoll>=1 and newRoll <=100):
#       self.__roll=newRoll
#       print("Roll No Added Successfully!!")   
#       return self.__roll
#     else :
#       return print("Invalid Roll Number.")

#   def get_info(self):
#     return f"Name: {self.__name} has Roll No: {self.__roll} & Marks: {self.__marks}"
  
# std=Student()
# std.set_name("Ayush") 
# std.set_roll(115)
# std.set_marks(67) 

# print(std.get_info())


#Problem 4 
# class rectangle:
#   def __init__(self, length, breadth): 
#     self.area=length*breadth  
#     return print(f"Area: {self.area}")

# class circle:
#   def __init__(self,radius):
#     self.area=radius*radius*3.14
#     return print(f"Area: {self.area}") 
  
# class triangle:
#   def __init__(self,base, height):
#     self.area=0.5 * base* height 
#     return print(f"Area: {self.area}")
  
# class Shape(rectangle, circle, triangle):
#   def __init__(self, length, breadth, radius, base, height):
#     super().__init__(length, breadth)
#     circle.__init__(self,radius) 
#     triangle.__init__(self,base, height)
 
# Shape(3,5,6,7,8)

#Problem 5 
