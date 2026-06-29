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
  
std=main("Ayush",9.0) 
print(f"{std.name} has a cgpa = {std.get_cpga()}")

class Student:
  college_name="ABC College"

  def __init__(self,name,cgpa):
    self.name=name
    self.cpga=cgpa
    self.PI=3.14 

print(f"{Std.name} has cgpa= {Std.cpga} and {Std.PI}.")

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

Std=Laptop("16gb", "128gb") 
Std.calc_discount(40_000,100)

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

p1=Online_Store("Phone", 100000) 
p2=Online_Store("Laptop", 300000) 
p1.calc_discount(p1.price, 12)  

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
acc.set_balnc(200_000)
print(acc.account, acc.get_balnc()) 

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

t1=Teacher("Maths") 
t1.change_endTime("5pm") 
print(t1.start_time, t1.end_time)

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
print(ta.name, ta.gpa, ta.salary)

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
lion.make_sound() 

cow=Cow() 
cow.make_sound() 

#Polymorphism  
class Teacher:
  def get_designation(self):
    print("Desination=Teacher") 

class Account:
  def get_designation(self):
    print("Desination=Accountant") 
  
t1=Teacher() 
t1.get_designation() 

acc1=Account() 
acc1.get_designation()

#Assignment
#Problem 1
class Bank_Account:
  def __init__(self,acc_number,owner_name,balance):
    self.acc_number=acc_number 
    self.owner_name=owner_name 
    self.balance=balance 

  def deposit(self,dep):
    self.balance=self.balance+dep
 
  def withdraw(self,wtd):
    self.balance=self.balance-wtd
 
  def get_balnc(self):
    print(f"Balance: {self.balance}")

own=Bank_Account("00091819","Ayush", 25_000)
own.deposit(13000)
own.withdraw(20000)
own.get_balnc()
 
#Problem 2 
class Book:
  count=0

  def __init__(self,author,title):
    self.title=title 
    self.__author=author 
    self.reviews=[] 
   
  def set(self,newAuthor):
    self.__author=newAuthor 
    return print("Auther Set Successfully!")


  def get(self):
    return self.__author 

  def addReviews(self, newReviews):
    self.reviews.append(newReviews) 
    print("Review counted successfully")
    Book.count= Book.count+1 
  
  def get_reviews(self):
    return self.reviews

  @classmethod
  def get_count(cls):
    return cls.count

bk=Book("Ayush","Hell")
bk.addReviews("Excellent")
bk.addReviews("Good")
bk.addReviews("Very Good")
print("Title: ",bk.title)
print("Author: ",bk.get()) 
print("Reviews: ",bk.get_reviews())
print("Count:",bk.get_count()) 


#Problem 3 
class Student:
  def __init__(self):
    self.__name=None
    self.__roll=None
    self.__marks=None

  def set_marks(self,newMarks):
    if(newMarks>0):
      self.__marks=newMarks 
      print("Marks Added Successfully!!")
      return self.__marks
    else:
      return print("Invalid Marks!") 

  def set_name(self,newName):
    if(newName == None):
      return print("Name cannot be empty!")
    else :
      self.__name=newName
      print("Name Added Successfully!!")   
      return self.__name 
    
  def set_roll(self,newRoll):
    if(newRoll>=1 and newRoll <=100):
      self.__roll=newRoll
      print("Roll No Added Successfully!!")   
      return self.__roll
    else :
      return print("Invalid Roll Number.")

  def get_info(self):
    return f"Name: {self.__name} has Roll No: {self.__roll} & Marks: {self.__marks}"
  
std=Student()
std.set_name("Ayush") 
std.set_roll(115)
std.set_marks(67) 

print(std.get_info())


#Problem 4 
class rectangle:
  def __init__(self, length, breadth): 
    self.area=length*breadth  
    return print(f"Area: {self.area}")

class circle:
  def __init__(self,radius):
    self.area=radius*radius*3.14
    return print(f"Area: {self.area}") 
  
class triangle:
  def __init__(self,base, height):
    self.area=0.5 * base* height 
    return print(f"Area: {self.area}")
  
class Shape(rectangle, circle, triangle):
  def __init__(self, length, breadth, radius, base, height):
    super().__init__(length, breadth)
    circle.__init__(self,radius) 
    triangle.__init__(self,base, height)
 
Shape(3,5,6,7,8) 

from abc import ABC, abstractmethod

#Problem 5 
class Vehicle:
  def __init__(self,brand,model):
    self.brand=brand 
    self.model=model 

class Car(Vehicle):
  def __init__(self, brand, model,seats):
    super().__init__(brand,model) 
    self.seats=seats 

class Bike(Vehicle):
  def __init__(self,brand, model, engine_cc):
    super().__init__(brand,model)
    self.engine_cc=engine_cc

car=Bike("Mercedes","Benz", 4) 
print(f"Car: {car.brand}, Model: {car.model}, Engine:{car.engine_cc}")


#Problem 6 
from abc import ABC , abstractmethod 

class Employee:
  @abstractmethod
  def calculate_salary(self):
    pass 

class Intern(Employee):
  def calculate_salary(self, salary): 
    self.salary=salary 
    return print(f"Salary of Intern:{self.salary}")

class FullTimeEmployee(Employee): 
  def calculate_salary(self,salary): 
    self.salary=salary 
    return print(f"Salary of Employee: {self.salary}") 
  
class ContractEmployee(Employee):
  def calculate_salary(self,salary):
    self.salary=salary 
    return print(f"Salary of Contract Employee: {self.salary}") 

emp=ContractEmployee()
emp.calculate_salary(35_000)

#Problem 7 
class Person:
  name="Ayush" 

  def __init__(self,age,address):
    self.age=age 
    self.address=address  
  
  @classmethod
  def get_name(cls):
    return cls.name
  
n=Person(21,"Chembur") 
print(f"{n.get_name()} is {n.age} years and stays at {n.address}.")


#Problem 8 
class Player:
  player_count=0 

  def __init__(self,name,level):
    self.name=name  
    self.level=level
    Player.player_count+=1 
  
  def get_info(self):
    print(f"Name: {self.name} and level: {self.level}.") 
  
  @classmethod 
  def get_count(cls):
    return print(f"Count: {cls.player_count}") 

p1=Player("Ayush", 3)  
p2=Player("Sanchia", 1)  
p3=Player("Tanushree", 2)   
p1.get_count() 


#Problem 9 
class Herbivore:
  def __init__(self, food1):
    self.food=food1 
  
class Carnivore: 
  def __init__(self,food2):
    self.carni=food2

class Omnivore:
  def __init__(self,food3):
    self.omni=food3

class Bear(Herbivore, Carnivore, Omnivore):
  def __init__(self, food1,food2, food3):
    super().__init__(food1) 
    Carnivore.__init__(self, food2) 
    Omnivore.__init__(self, food3) 
    
b=Bear("Grass", "Meat", "Both") 
print(f"Herbivore: {b.food} Carnivore: {b.carni} Omnivore: {b.omni}")


#Problem 10 
#---------------------------------------------- 
# Message Class  
#----------------------------------------------
class Message: 
  message_counter=1  #simple counter  

  def __init__(self,sender,content):
    self.sender=sender 
    self.content=content
    self.id=Message.message_counter 
    Message.message_counter+=1 

  def __str__(self):
    return f"({self.id}){self.sender.username}:{self.content}" 


#---------------------------------------------- 
# User Class 
#----------------------------------------------
class User: 
  def __init__(self,username):
    self.username=username
    self.chatroom=None

  def join_chatroom(self, chatroom):
    if self.chatroom:
      print(f"{self.username} is already in chatroom.") 
    else:
      chatroom.add_user(self) 
      self.chatroom=chatroom  
      print(f"{self.username} joined {chatroom.name}")  
  
  def  leave_chatroom(self):
    if not self.chatroom:
      print(f"{self.username} is not in chatrooom.") 
    else:
      self.chatroom.remove_user(self)
      print(f"{self.username} left {self.chatroom.name}") 
      self.chatroom=None 
  
  def send_message(self, content):
    if not self.chatroom :
      print(f"{self.username} cannot send a message(not a chatroom)")
    else:
      self.chatroom.broadcast(self, content) 


#-------------------------------------------------
#ChatRoom Class 
#-------------------------------------------------
class ChatRoom:
  def __init__(self,name):
    self.name=name
    self.users=[] 
    self.messages=[]

  def add_user(self, user):
    self.users.append(user) 
  
  def remove_user(self, user):
    self.users.remove(user) 
  
  def broadcast(self, sender, content):
    message=Message(sender, content) 
    self.messages.append(message) 
    print(message)   #Show message to all users  
  
  def show_chat_history(self):
    print(f"\nChat History of {self.name}:") 
    for msg in self.messages:
      print(msg)
      print() 

#----------------------------------------------
#Example Usage  
#----------------------------------------------
if __name__=="__main__":
  room=ChatRoom("Python Lounge") 
  u1=User("Alice") 
  u2=User("Bob") 
  u3=User("Charlie") 

  u1.join_chatroom(room) 
  u2.join_chatroom(room) 

  u1.send_message("Hello everyone") 
  u1.send_message("Hi Alice")

  u3.join_chatroom(room) 
  u3.send_message("Hey guys, what's up?") 

  room.show_chat_history() 

  u1.leave_chatroom() 
  u2.leave_chatroom() 
  u3.leave_chatroom() 
 
