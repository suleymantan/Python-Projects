"""
Control Flow & Loops (20 Projects)
 * Multiplication Table: Print the multiplication table for a given number.
 * Factorial Calculator: Calculate the factorial of a number.
 * Fibonacci Sequence: Print the Fibonacci sequence up to a given number.
 * Prime Number Checker: Check if a number is prime.
 * Number Series: Print various number series (e.g., arithmetic, geometric).
 * Sum of Natural Numbers: Calculate the sum of natural numbers up to a given number.
 * Average of Numbers: Calculate the average of a set of numbers entered by the user.
 * Grade Calculator: Calculate a student's grade based on their scores.
 * Simple Quiz: A simple quiz with a few questions.
 * Guess the Number Game (Enhanced): Give hints (higher/lower) to the user.
 * Hangman (Basic): A text-based hangman game.
 * Pattern Printing: Print various patterns using loops (e.g., triangles, squares).
 * Countdown Timer: A program that counts down from a given number.
 * Dice Rolling Simulator: Simulate rolling a dice multiple times.
 * Coin Flip Simulator: Simulate flipping a coin multiple times.
 * Password Generator (Basic): Generate a random password of a given length.
 * Calendar (Basic): Display the calendar for a given month.
 * Simple To-Do List (Text-Based): Add, view, and remove tasks.
 * ATM Simulator (Basic): Simulate basic ATM transactions.
 
"""

# * Multiplication Table: Print the multiplication table for a given number.
"""a = int(input("Enter a number: "))
i= 1
j = 1
for i in range(a + 1):
    for j in range(a + 1):
        x = i*j
        print(f"{i} * {j} = {x}")"""

# * Factorial Calculator: Calculate the factorial of a number.
"""fac_input = int(input("Enter a number: "))
b = 1
for i in range(1,(fac_input+1)):
    b = i * b
    i +=1
    print(b)"""

# * Fibonacci Sequence: Print the Fibonacci sequence up to a given number.

"""fib_input = int(input("Enter a number: "))
n1 = 0
n2 = 1
count = 0
for i in range(fib_input+1):
    n = n1 + n2
    n1 = n2
    n2 = n
    
    print(n)"""

# * Prime Number Checker: Check if a number is prime.
"""not_prime = []
prime = []
prime_number = int(input("Enter a number: "))
for i in range(2,prime_number):
    for j in range(2,i):
        if (i % j) == 0:
            not_prime.append(i)
            break
    else:
        prime.append(i)
            

print(not_prime)
print(prime)"""

# * Number Series: Print various number series (e.g., arithmetic, geometric).
"""num = int(input("enter a number: "))
for i in range(1,num):
    square = i * i
    print(square)

for i in range(1,num):
    cube = i*i*i
    print(cube)
"""


# * Sum of Natural Numbers: Calculate the sum of natural numbers up to a given number.
"""sum_num = []
total = 0
for i in range(10):
    num = int(input("Enter a number: "))
    sum_num.append(num)
    total +=num
    
print(sum_num)
print(total)"""

#* Average of Numbers: Calculate the average of a set of numbers entered by the user.
"""sum_num = []
total = 0
for i in range(10):
    num = int(input("Enter a number: "))
    sum_num.append(num)
    total +=num
    
print(sum_num)
print(total)
avarage = total/len(sum_num)
print(avarage)"""

# * Grade Calculator: Calculate a student's grade based on their scores.

"""exam1 = int(input("Enter scores for 1. Exam: "))
exam2 = int(input("Enter scores for 2. Exam: "))
grade_calcute = (exam1 * 0.30) + (exam2 * 0.7)

if (grade_calcute >= 90) & (grade_calcute <= 100):
    print(f'Your scores: {grade_calcute} and your letter grade: AA')
elif (grade_calcute >= 85) & (grade_calcute < 90):
    print(f'Your scores: {grade_calcute} and your letter grade: BA')
elif (grade_calcute >= 80) & (grade_calcute < 85):
    print(f'Your scores: {grade_calcute} and your letter grade: BB')
elif (grade_calcute >= 70) & (grade_calcute < 80):
    print(f'Your scores: {grade_calcute} and your letter grade: CB')
elif (grade_calcute >= 60) & (grade_calcute < 70):
    print(f'Your scores: {grade_calcute} and your letter grade: CC')
elif (grade_calcute >= 50) & (grade_calcute < 60):
    print(f'Your scores: {grade_calcute} and your letter grade: DC')
elif (grade_calcute >= 45) & (grade_calcute < 50):
    print(f'Your scores: {grade_calcute} and your letter grade: DD')
else:
    print(f'Your scores: {grade_calcute} and your letter grade: FF')"""

# * Simple Quiz: A simple quiz with a few questions.
"""import random
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
while True:
    rand_int = random.randint(1,4)
    print(f"Question {rand_int}: {question_dictionarie[rand_int]["q"]}\n{question_dictionarie[rand_int]['option']}")
    print("---------------------------------------")
    your_answer = input("Enter your answer: ")
    if your_answer == question_dictionarie[rand_int]["answer"]:
        print("correct")
    else:
        print("Your correct is not true")

"""
#* Hangman (Basic): A text-based hangman game.
"""import random
hangman = ["ELEPHANT", "ASTRONAUT","PYRAMID","VOLCANO","CHAMELEON","SPAGHETTI","LIBRARY","HOSPITAL","UNIVERSITY","REFRIGERATOR"]
ran = random.choice(hangman)

ran_hang=[]
for i in ran:
    ran_hang.append("_")
print(ran_hang)

chance = 0
len_ran = len(ran)

for i in (ran):
    letter = input('Enter a letter: ')
    for index,cha in enumerate(ran):
        if cha == letter:
            a = index
            chance +=1
            ran_hang[a]= letter
            print(ran_hang)
            if (chance - len_ran) == -3:
                ask = input("Do you have idea? ")
                if (ask == "yes") or (ask == "y") or (ask == "YES") or (ask == "Y"):
                    guess = input("Tell me your idea: ")
                    if guess == ran:
                        print(f"Congrulations \nYour ide is correct \nWord: {ran}")
                else:
                    letter = input('Enter a letter: ')"""

# Pattern Printing: Print various patterns using loops (e.g., triangles, squares).

"""row = 5
for i in range(row + 1):
    for j in range(i):
        print("*", end="")
    print("")

for i in range(1, row + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')"""
            
# Countdown Timer: A program that counts down from a given number.
"""import time
timer = int(input("What time should the counter start from? "))
for i in range(timer):
    print(timer)
    timer -= 1
    time.sleep(1)
"""
# * Dice Rolling Simulator: Simulate rolling a dice multiple times.
"""import random
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
for i in range(20):
    dice = random.randint(1,6)
    if dice == 1:
        one += 1
    elif dice == 2:
        two +=1
    elif dice == 3:
        three +=1
    elif dice == 4:
        four +=1
    elif dice == 5:
        five +=1
    else:
        six += 1

print(f"Dice Simulator \n-------------------------")
print(f"Dice 1: {one} \nDice 2: {two} \nDice 3: {three} \nDice 4: {four} \nDice 5: {five} \nDice 6: {six} \n")"""

# * Coin Flip Simulator: Simulate flipping a coin multiple times.
"""import random
heads,tails = 0,0
coin = ["heads","tails"]
for i in range(20):
    flip = random.choice(coin)
    if flip == "heads":
        heads +=1
    else:
        tails +=1

print("Heads: ",heads)
print("Tails: ",tails)"""


# * Password Generator (Basic): Generate a random password of a given length.
"""import random
alpha_pass ="ABCDEFGHIJKLMNOQPRSTUXWYZabcdefghijklmnoqprstuxwyz1234567890.,:;!&#@*<>"
password = random.choices(alpha_pass,k = 12)
print(password)"""

#  * Calendar (Basic): Display the calendar for a given month.
"""import calendar

year = 2011
months = 12
print(calendar.month(year,months))

print(calendar.calendar(2012))

print(calendar.calendar(2035))"""

#* Simple To-Do List (Text-Based): Add, view, and remove tasks.
"""to_do = []
while True:
    print("1: Show me To do List: \n2: Add something To do List: \n3: Remove from To do List: ")
    choses = input('Chose option: ')
    if choses == "1":
        print(to_do)
        if len(to_do) < 1:
            print("Your To do list is empty \n---------------------")
            ask =input("Do you want to add a task? 'yes' or 'no'  ")
            if ask == "yes":
                how_many = int(input("How many do you want to add task? "))
                for i in range(how_many):
                    task = input("Add Task: ")
                    to_do.append(task)
                
        else:
            print(to_do)
    elif choses == "2":
        how_many = int(input("How many do you want to add task? "))
        for i in range(how_many):
            task = input("Add Task: ")
            to_do.append(task)
    elif choses == "3":
        for index,task in enumerate(to_do):
            print(index,task)
        how_many = int(input("How many do you want to add task? "))
        for i in range(how_many):
            ask = int(input("Which task do you want delete? Enter index number: "))
            del to_do[ask]

    else:
        break"""


# * ATM Simulator (Basic): Simulate basic ATM transactions.
"""import time
import random
money = 0
while True:
    iban = random.randint(10000000000000000000000000,99999999999999999999999999)
    print("1:Account Information: \n2: Deposit Money: \n3: Withdraw Money: \n4: Exit: ")
    choses = input("Select Action: ")
    print("Please wait")
    time.sleep(3)
    if choses == "1":
        print(F"IBAN N°: {iban} \nMoney: {money} €")
        time.sleep(15)
        if money <= 0:
            ask = input("Do you want to deposit money: ('yes' or 'no')  ")
            if ask == "yes":
                depo = int(input("How much do you want to deposit money? "))
                money += depo
                print(F"IBAN N°: {iban} \nMoney: {money} €")
        else:
            time.sleep(10)
            print("Please wait")
            ask = input("for Deposit Money enter '1': \nfor Withdraw Money enter '2': \n for Exit enter 'q': ")
            if ask == "1":
                depo = int(input("How much do you want to deposit money? "))
                money += depo
                time.sleep(3)
                print(F"IBAN N°: {iban} \nMoney: {money} €")
            elif ask == "2":
                depo = int(input("How much do you want to withdraw money? "))
                money -= depo
                time.sleep(3)
                print(F"IBAN N°: {iban} \nMoney: {money} €")
            else:
                time.sleep(3)
                print(F"IBAN N°: {iban} \nMoney: {money} €")
    elif choses == "2":
        time.sleep(3)
        depo = int(input("How much do you want to deposit money? "))
        money += depo
        time.sleep(3)
        print(F"IBAN N°: {iban} \nMoney: {money} €")

    elif choses == "3":
        time.sleep(3)
        depo = int(input("How much do you want to withdraw money? "))
        money -= depo
        time.sleep(3)
        print(F"IBAN N°: {iban} \nMoney: {money} €")
    else:
        time.sleep(3)
        print(F"IBAN N°: {iban} \nMoney: {money} €")
        break
"""


        





        

