"""

* Function for Area Calculation: Create functions for calculating the area of different shapes.
* Function for Prime Checking: Create a function to check if a number is prime.
* Recursive Functions: Practice writing recursive functions (e.g., factorial, Fibonacci).
* Function for String Reversal: Create a function to reverse a string.
* Function for Palindrome Checking: Create a function to check for palindromes.
* Function for Calculating Average: Create a function to calculate the average of a list of numbers.
* Function for Generating Random Numbers: Create a function to generate random numbers within a range.
* Function for Converting Units: Create functions for converting between different units.
* Function for Password Generation: Create a more robust password generator function.
* Function for Validating Input: Create functions to validate user input.
* Calculator with Functions: Implement a calculator using functions for each operation.
* Hangman with Functions: Implement the Hangman game using functions.
* Rock, Paper, Scissors with Functions: Implement the game using functions.
* Number Guessing Game with Functions: Implement the game using functions.
* To-Do List with Functions: Implement the to-do list using functions.
* ATM Simulator with Functions: Implement the ATM simulator using functions.
* Simple Quiz with Functions: Implement the quiz using functions.
* Function for Searching in a List: Create a function to search for an element in a list.
* Function for Filtering a List: Create a function to filter a list based on a condition.
"""
import math
"""def square_area(x):
    area = x*x
    return area
print(square_area(7))

def rectangle_area(x,y):
    area = x * y
    return area
print(rectangle_area(7,6))


def triangle_area(x,y):
    area = (x * y)/2
    return area
print(triangle_area(7,6))

def parallelogram(x,y):
    area = x * y
    return area
print(parallelogram(7,6))

def trapezoid(x,y,h):
    area = ((x+y)*h)/2
    return area
print(trapezoid(7,6,5))

def circle(r, pi=3.14):
    area = r*r*pi
    return area

print(circle(6))"""

#* Function for Prime Checking: Create a function to check if a number is prime.
"""def prime_check(x):
    prime =[]
    for i in range(2,x):
        for j in (range(2,i)):
            if (i % j) == 0:
                break
        else:
            prime.append(i)
    return prime

print(prime_check(24))"""

#* Recursive Functions: Practice writing recursive functions (e.g., factorial, Fibonacci).
"""def fac(x):
    fact = 1
    for i in range(1,x):
        fact *= i
    return fact
print(fac(6))

def fib(x):
    n1 = 0
    n2 = 1
    for i in range(x+1):
        n = n1 + n2
        n1 = n2
        n2 = n
    return n

print(fib(10))"""

#** Function for String Reversal: Create a function to reverse a string.
"""def reverse_string(x):
    x = x[::-1]
    return x
print(reverse_string("This is not problem"))"""

# * Function for Palindrome Checking: Create a function to check for palindromes.
"""def palindrom(x):
    y = x[::-1]
    if x == y:
        return (f"{x} is palindrome word")
    else:
        return (f"{x} is not palindrome word")
    
print(palindrom("racecar"))"""

#* Function for Calculating Average: Create a function to calculate the average of a list of numbers.
"""def average(*x):
    average = sum(x)/len(x)
    return average
print(average(20,10,30,45,35))"""

#* Function for Generating Random Numbers: Create a function to generate random numbers within a range.
"""import random
def random_numbers(x, y=1,z=9999999):
    
    #You need to give 3 number
    #first number: for how many do you want random number
    #Second number: for which number function will start
    #Third number: for which number function will end

    #if you give 1 number, function choses random number between 1-9999999
    
    rand_no = []
    for i in range(x):
        r_n = random.randint(y,z)
        rand_no.append(r_n)
    return rand_no
    
print(random_numbers(5))"""

#* Function for Converting Units: Create functions for converting between different units.
"""def convert_units(x):
    
    def cel(x):
        
        fahrenheit = (x-32)/1.8
        return (f"{x}° Celsius equal to {fahrenheit} Fahrenhiet")
    

    def fah(x):
        
        celsius = (x+32)*1.8
        return (f"{x} Fahrenheit equal to {celsius}° Celsius")
    return (f"{cel(x)} \n{fah(x)}")


a =convert_units(100)
print(a)

def meter(x):

    def km(x):
        m_km = x/1000
        return (f"{x} meter is equal to {m_km} kilometer")
    def hm(x):
        m_hm = x/100
        return (f"{x} meter is equal to {m_hm} hectometer")
    def dm(x):
        m_dm = x/10
        return (f"{x} meter is equal to {m_dm} decameter")
    def dsm(x):
        m_dsm = x*10
        return (f"{x} meter is equal to {m_dsm} decimeter")
    def cm(x):
        m_cm = x*100
        return (f"{x} meter is equal to {m_cm} centimeter")
    def mm(x):
        m_mm = x*1000
        return (f"{x} meter is equal to {m_mm} millimeter")
    return (f"{km(x)} \n{hm(x)}\n{dm(x)}\n{dsm(x)}\n{cm(x)}\n{mm(x)}")

print(meter(25))"""

#* Function for Password Generation: Create a more robust password generator function.
"""import random
import string
def password(x):
    character = string.ascii_letters + string.digits + string.punctuation
    pass_word = "".join(random.choice(character) for i in range(x))
    
    return pass_word
    
print(password(12))"""

#* Function for Validating Input: Create functions to validate user input.
"""def validating_input(username,password):
    nickname = "python2025"
    pass_ = "Pyton00"
    
    if (username == nickname) or (pass_ == password):
        return ("Login is succesfull")
    elif (username != nickname) & (pass_ != password):
        return ("username or password is wrong")
    
print(validating_input("python2025","Pyton00"))"""

#* Calculator with Functions: Implement a calculator using functions for each operation.
"""from functools import reduce
from operator import sub,truediv,mul
def calcute(*args):
    def sum_(*args):
        summ = sum(args)
        return summ
    def sub_(*args):
        sub_ = reduce(sub,args)
        return sub_
    def mult(*args):
        multi = reduce(mul,args)
        return multi
    def div(*args):
        divi = reduce(truediv,args)
        return divi
    return (f"{sum_(*args)} \n{sub_(*args)} \n{mult(*args)} \n{div(*args)}")
    
print(calcute(5,6,7,24))"""

#* Hangman with Functions: Implement the Hangman game using functions.
"""import random
def hagman():
    words = ["ELEPHANT", "ASTRONAUT","PYRAMID","VOLCANO","CHAMELEON","SPAGHETTI","LIBRARY","HOSPITAL","UNIVERSITY","REFRIGERATOR"]
    word = random.choice(words)
    secret_word = ("_") * (len(word))
    guess_letter = []
    chance = 6
    print("Welcome to Game")
    
    while "_" in secret_word and chance > 0:
        guess = input("enter a letter: ").upper()
        if guess in guess_letter:
            print('You guess this letter')
            continue
        else:
            guess_letter.append(guess)
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    secret_word = secret_word[:i] + guess + secret_word[i+1:]
            print(secret_word)
        else:
            chance -= 1
            print("Wrong letter. Your Chance: {}".format(chance))
    if "_" not in secret_word:
        print("Conguralations You win. Word: {}".format(word))
        
    else:
        print("You lost. Word: {}".format(word))
        

hagman() """

# * Rock, Paper, Scissors with Functions: Implement the game using functions.
"""import random
def rps():
    option = ["Rock","Paper","Scissors"]
    machine =random.choice(option) 
    game = int(input("Hpw many times do you want to play? "))
    machine_skor = 0
    player_skor = 0
    while game > 0:
        machine =random.choice(option) 
        player = input("Rock,Paper,Scissors: ").capitalize()
        if (machine == "Rock") and (player == "Scissors"):
            machine_skor += 1
            print("Machine win \nYour choses: {} \nMachine: {}".format(player,machine))
            game -=1
        elif (player == "Rock") and (machine == "Scissord"):
            player_skor += 1
            print("Player win\nYour choses: {} \nMachine: {}".format(player,machine))
            game -=1
        elif (machine == "Paper") and (player == "Rock"):
            machine_skor += 1
            print("Machine win \nYour choses: {} \nMachine: {}".format(player,machine))
            game -=1
        elif (player == "Paper") and (machine_skor == "Rock"):
            player_skor += 1
            print("Player win \nYour choses: {} \nMachine: {}".format(player,machine))
            game -=1
        elif (machine == "Scissors") and (player == "Paper"):
            machine_skor += 1
            print("Machine win \nYour choses: {} \nMachine: {}".format(player,machine))
            game -=1
        elif (player == "Scissors") and (machine == "Paper"):
            player_skor += 1
            print("Player win \nYour choses: {} \nMachine: {}".format(player,machine))
            game -=1
        else:
            print("The match is draw \nYour choses: {} \nMachine: {}".format(player,machine))
    print("Your Scors: {} \nMchine Scors: {}".format(player_skor,machine_skor))

rps()
"""

#* Number Guessing Game with Functions: Implement the game using functions.
"""import random 
def guess_number():
    random_number = random.randint(1,1000)
    chance  = 10
    while chance >0:
        your_number = int(input("Guess number: "))
        if random_number == your_number:
            print("Congrulation \nYour guess is correct \nRandom Number: {}".format(random_number))
            break
        elif random_number > your_number:
            print("Random number is grater than your number...")
            chance -=1
        else:
            print("Random Number is smaller than your number: ")
            chance -=1
    print("Random Number: {} \nChance: {}".format(random_number,chance))

guess_number()"""

#* To-Do List with Functions: Implement the to-do list using functions.
"""import time
def todolist():
    to_do =[]
    finish_todo = []
    continue_todo = []
    while True:
        print("CHOSESS TRANCACTION \n-------------------\nFor add to do '1' \nfor show to do '2'\nfor completed projects '3' ")
        choses = input("Choses Transaction: ")
        if choses == "a":
            add_todo = input("Add to do: ")
            to_do.append(add_todo)
            time.sleep(3)
            print("Task added...")
        elif choses == "s":
            if len(to_do) == 0:
                print("To Do List is empty")
                print(len(to_do))
                add_todo = input("Add to do: ")
                to_do.append(add_todo)
                time.sleep(3)
                print("Task added...")
            else:
                for i,j in enumerate(to_do):
                    print("Task List \n------------\n",i,j)
        elif choses == "f":
            time.sleep(3)
            if len(finish_todo) == 0:
                print("There are no completed tasks yet")
                for index,todo in enumerate(to_do):
                    print(index,todo)
                choses = input("Which task did you complete? \nEnter number: ")
                if int(index) == int(choses):
                    finish_todo.append(to_do[int(choses)])
                    to_do.pop(int(choses))
                    time.sleep(3)
                    print("Task added...")                    
            else:
                time.sleep(3)
                print("Completed Tasks")
                for i,j in enumerate(finish_todo):
                    print(i,j)
                print("Continue Tasks \n------------------")
                for index,todo in enumerate(to_do):
                    print(index,todo)
                choses = input("Which task did you complete? \nEnter number: ")
                if index == int(choses):
                    finish_todo.append(to_do[int(choses)])
                    to_do.pop(int(choses))
                    time.sleep(3)
                    print("Task added...")
        
todolist()"""

#* Simple Quiz with Functions: Implement the quiz using functions.
"""import random
def quiz():
    chance = 3
    question_dictionarie = {
    1:{    
        "q":"Where is the capital of England?",
        "option": {"A":"Liverpool","B":"Manchester","C":"London","D":"Leeds"},
        'answer':"C"

    },
    2:{    
        "q":"Where is the capital of France?",
        "option": {"A":"Marseille","B":"Nice","C":"Lyon","D":"Paris"},
        'answer':"D"

    },
   
   3:{    
        "q":"Where is the capital of Italy?",
        "option": {"A":"Milano","B":"Torino","C":"Roma","D":"Napoli"},
        'answer':"C"

    },
   
   4:{    
        "q":"Where is the capital of Kurdistan?",
        "option": {"A":"Amed","B":"Hewler","C":"Mahabad","D":"Kobani"},
        'answer':"A"

    }
      }
    while chance > 0:
        q1 = random.randint(1,4)
        print(f"Question: {question_dictionarie[q1]["q"]} \n{question_dictionarie[q1]["option"]}")
        answer = input("Your answer: ")
        if answer == question_dictionarie[q1]["answer"]:
            print("Correct")
            chance -=1
        else:
            print("Your answer is wrong")
            chance -=1

        
        
quiz()"""

#* ATM Simulator with Functions: Implement the ATM simulator using functions.
"""import random
balance = 2000
def atm(balance):
    iban = random.randint(10000000000000000000000000,99999999999999999999999999)
    

    def info_account(balance):
        if balance == 0:
            ask = input("Do you want to deposite money? 'y' or 'n'").lower()
            if ask == 'y':
                h_much = int(input("How much money do you want to deposite? "))
                balance +=h_much
            return balance
        else:
            print(f"IBAN: {iban} \nBalance: {balance}")
            return balance

    def depose(balance):
        h_much = int(input("How much money do you want to deposite? "))
        balance += h_much
        
        print(f"IBAN: {iban} \nBalance: {balance}")
        return balance

    def withdraw(balance):
        h_much = int(input("How much money do you want to withdraw? "))
        balance -= h_much
        print(f"IBAN: {iban} \nBalance: {balance}")
        return balance

    print("Choose Transaction \n--------------\n1: Account Info \n2:Depose \n3:Withdraw \n4:Exit")
    while True:
        
        process = input("Choose Transaction: ")
        if process == "1":
            balance = info_account(balance)
        elif process == "2":
            balance = depose(balance)
        elif process == "3":
            balance = withdraw(balance)
        else:
            break

atm(balance)"""

#* Function for Searching in a List: Create a function to search for an element in a list.
"""list1= [1,3.14,"pi","square","fibonacci"]
def search(x,y):
    if y in x:
        print(f"The {y} is in list")
    else:
        print(f"The {y} is not in list")

search(list1,"pi")"""

#* Function for Filtering a List: Create a function to filter a list based on a condition
"""list1 = [1,24,65,78,37,66]
def filter(x):
    filt = []
    for i in x:
        if (i % 2) == 0:
            filt.append(i)
    return filt

print(filter(list1))"""

"""lorem = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."
lorem = lorem.split()

def filter(x,y):
    filt = []
    for i in x:
        if i.startswith(y):
            if i in filt:
                continue
            else:
                filt.append(i)
    return filt
            
print(filter(lorem,"c"))"""
