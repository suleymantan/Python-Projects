"""
Object-Oriented Programming (OOP)

Creating Classes: Create basic classes (e.g., Dog, Car, Book).
Inheritance: Implement inheritance (e.g., creating a subclass of Animal).
Polymorphism: Implement polymorphism (e.g., different shapes with a common area method).
Encapsulation: Practice encapsulation by making attributes private.
Bank Account Class: Create a BankAccount class with methods for deposit and withdrawal.
Student Class: Create a Student class with attributes and methods.
Car Class: Create a Car class with attributes like model, make, and speed.

Library Management System (OOP): Implement a more advanced library system using OOP concepts.
"""

#Creating Classes: Create basic classes (e.g., Dog, Car, Book).
"""class Students():
    def __init__(self,name,birth_day,contact_number):
        self.name = name
        self.birth_day = birth_day
        self.phone_number = contact_number

student1 = Students("Elon Must","01/04/1956","+16758495854949486980") 
print(student1.name)
print(student1.birth_day)
print(student1.phone_number)
print(student1.__dict__)"""


#Inheritance: Implement inheritance (e.g., creating a subclass of Animal).

"""class Students:
    def __init__(self,student_name,year,class_name):
        self.student_name = student_name
        self.year = year
        self.class_name = class_name

class ResponsibleTeacher(Students):
    def __init__(self,student_name,year,class_name,teacher_name,teacher_email,teacher_number):
        super().__init__(student_name,year,class_name)
        self.teacher_name = teacher_name
        self.teacher_email = teacher_email
        self.teacher_phone = teacher_number

    def responsible_student(self):
        return (f"{self.teacher_name}, is responsible for {self.student_name}, who is from the {self.class_name}")



teacher1 = ResponsibleTeacher("Messi","28","11/A","Pep Guardiola","pep@gmail.com","+349999999999")
print(teacher1.student_name)
print(teacher1.year)
print(teacher1.class_name)
print(teacher1.teacher_name)
print(teacher1.teacher_email)
print(teacher1.teacher_phone)
print(teacher1.__dict__)

print(teacher1.responsible_student())"""


#Polymorphism: Implement polymorphism (e.g., different shapes with a common area method).

"""class LoginSystem:
    def __init__(self,name_personel,username,password):
        self.name_personel = name_personel
        self.username = username
        self.password = password

    def login(self):
        print(f"{self.username} logged into the system")

    def logout(self):
        
        print(f"{self.username} logout into the system ")


class Manager(LoginSystem):
    def __init__(self, name_personel, username, password):
        super().__init__(name_personel, username, password)

class AsistanManger(LoginSystem):
    def __init__(self, name_personel, username, password):
        super().__init__(name_personel, username, password)

personels = [
    Manager("Elon Musk","spacex","tesla00"),
    AsistanManger("Asistan Elon","asistan_spacex","asistanspacex")
]

for personel in personels:
    if isinstance(personel,LoginSystem):
        print(f"Login {personel.username} ({type(personel).__name__})")
        personel.login()
        personel.logout()
    else:
        raise Exception("Wrong info")"""

# Encapsulation: Practice encapsulation by making attributes private.

"""class Manager:
    def __init__(self, name,enter_code):
        self.name = name
        self._enter_code = enter_code
    @property
    def get_enter_code(self):
        return self._enter_code
    @email.setter
    def set_enter_code(self,entercode):
        self._enter_code = entercode

manager1 = Manager("Elon Musk","SpacexTesla")
print(manager1.name)
print(manager1.get_enter_code())
manager1.set_enter_code("spacex01")
print(manager1.get_enter_code())
"""

#Bank Account Class: Create a BankAccount class with methods for deposit and withdrawal.
"""import random
class CashBank:
    balance = 0.0
    code_iban = "US"
    number_iban = random.randint(10000000000000000000000000,99999999999999999999999999)
    iban = code_iban+str(number_iban)

    def __init__(self,name,iban = iban,balance = balance):
        self.name = name
        self._iban = iban
        self._balance = balance

    
    def get_iban(self):
        return self._iban
    
    def get_balance(self):
        return self._balance
    
    def deposite(self,amount):
        self._balance += amount
        print(f"You deposite ${amount} into your account \nTotal Balance: {self.get_balance()}")

    def withdraw(self,amount):
        if amount > self._balance:
            print(f"Not enough limit: \n Your Limit: {self.get_balance} ")
            with_amount = input("Do you want to withdraw all your money: 'yes' or 'no  ").lower()
            if with_amount == 'yes':
                self._balance -= self._balance
                print(f"Your balace: {self.get_balance()}")
            else:
                raise Exception("Exit")
        else:
            self._balance -= amount
            print(f"Your balace: {self.get_balance()}")
            

account1 = CashBank("Elon Musk")
print(account1.get_iban())
account1.deposite(500)
#account1.withdraw(600)
account1.withdraw(400)"""

#Student Class: Create a Student class with attributes and methods.
"""class Students:
    def __init__(self,name,school_number, contact_number):
        self._name = name
        self._school_number = school_number
        self._phone_number = contact_number

        def get_name(self):
            return self._name
        
        def get_school_number(self):
            return self._school_number
        
        def get_phone_number(self):
            return self._phone_number
        

class ContactFamily(Students):
    def __init__(self, name,school_number,contact_number, nom_mother,mom_phone,nom_father,dad_phone):
        super().__init__(name,school_number,contact_number)
        self.student_mother = nom_mother
        self.mom_number = mom_phone
        self.student_father = nom_father
        self.dad_phone = dad_phone

student1 = ContactFamily("elon musk",3.14,"+19640945974050","Elon Mother","+54975490054","Elon Father","+19649749040940")
print(student1.__dict__)
print(student1._school_number)"""

# Car Class: Create a Car class with attributes like model, make, and speed.

"""class Car:
    car_count = 0
    def __init__(self,brand,model,year,speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed
        Car.car_count +=1

    

car1 = Car("Bugatti","B1",2023,400)
car2 = Car("BMW","X1",2023,300)
car3 = Car("Mercedes","M1",2022,300)
car4 = Car("Aston Martin","A1",2024,350)
print(Car.car_count)"""

#Library Management System (OOP): Implement a more advanced library system using OOP concepts.
"""import random

class Library:
    book_count = 0
    author_list=[]
    def __init__(self,book_name,author,publicatin_date):
        self.book_name = book_name
        self.author = author
        self.publication_date = publicatin_date
        
        Library.book_count += 1
        Library.author_list.append(author)


class GenreLangue(Library):
    langue_list = []
    registration_number = random.randint(1000000000,9999999999)
    def __init__(self, book_name, author, publicatin_date,genre,langue, registration_number=registration_number):
        super().__init__(book_name, author, publicatin_date)
        self.genre = genre
        self.langue = langue
        self.registration_number = registration_number

book1 = GenreLangue("try book","Elon Musk",2024,"Scary","English")
book2 = GenreLangue("my dream","Cristiano Ronaldo",2007,"Biogrzfi","English")
book3 = GenreLangue("my dream3","Cristiano Ronaldo",2007,"Biogrzfi","English")

print(book1.__dict__)
print(Library.book_count)
a = set(Library.author_list)
print(a,len(a))
print(Library.diff_author)"""