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


t1=Teacher("Maths") 
t1.change_endTime("5pm") 
print(t1.start_time, t1.end_time)
