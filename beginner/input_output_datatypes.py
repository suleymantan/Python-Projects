"""

* Basic String Manipulation: Reverse a string, find its length, etc.
* Vowel Counter: Count the number of vowels in a string.
* Palindrome Checker: Check if a string is a palindrome.
* Word Counter: Count the number of words in a sentence.
* Character Counter: Count the occurrences of each character in a string.
* Data Type Checker: Determine the data type of a user-entered value.
* Number Guessing Game (Basic): The computer generates a number, and the user guesses.
* Rock, Paper, Scissors (Basic): A simple text-based version.
* Mad Libs Generator: A text-based Mad Libs game.
* Unit Converter (Various): Convert between different units (e.g., inches to centimeters, kilograms to pounds)."""

# * Hello World: Print "Hello, World!" to the console.
#print("Hello World")
#print("----------------------------------------------------------------------------------")
""" #* Name and Age: Ask the user for their name and age, then print a greeting.

name = input("What is yot name and surname? ")
age = int(input("How old are you? "))
print(f" Hello my name is {name} and I'm {age} years old )"""


""" # * Simple Calculator: Perform basic arithmetic operations (+, -, *, /) on two user-input numbers.

int1 = int(input("give me number: "))
int2 = int(input("Give me another number: "))
choose = input("choose process   +  -  *  /")

if choose == "+":
    result = int1+int2
    print(result)
elif choose == "-":
    result = int1-int2
    print(result)
elif choose == "*":
    result = int1*int2
    print(result)
elif choose == "/":
    result = int1/int2
    print(result)
else:
    print("transaction invalid")"""

""" #* Area of a Rectangle: Calculate the area of a rectangle given length and width.

rectangle_long = int(input('Give me the long side of the rectangle: '))
rectangle_short = int(input("Give me the short side of the rectangle: "))

area_rectangle = rectangle_long*rectangle_short
print("Area of the rectangle: ", area_rectangle) """


""" # * Perimeter of a Circle: Calculate the perimeter of a circle given the radius.
radius = int(input("give me rzadius of the circle: "))
perimeter_circle = 2 * 3.14*radius

print("Perimeter of a circle: ",perimeter_circle ) """

""" #* Temperature Converter: Convert Celsius to Fahrenheit or vice-versa.

while True:
    print(" 1: Conversion Celsius to Fahrenheit \n 2: Conversion Fahrenheit to Celsius")
    choose_process = input("Choose process: ")
    if choose_process == "1":
        celsius_degrees = float(input("give me Celsius: "))
        result_fahrenheit = (celsius_degrees * 1.8) + 32
        print(f"{celsius_degrees} Celsiusn degrees equal {result_fahrenheit} degrees Fahrenheit")
    elif choose_process == "2":
        fahrenheit_degrees = float(input("give me Fahrenheit: "))
        result_celsius = (fahrenheit_degrees-32)/1.8
        print(f"{fahrenheit_degrees} Fahrenheit degrees equal {result_celsius} degrees Celsius")
    else:
        break """

""" #* Even or Odd: Determine if a number entered by the user is even or odd.

while True:
    a = input("Enter a number: ")
    n = a.isdigit()
    if n ==True:
        a = int(a)
        if (a % 2) == 0:
            print("number is odd")
        else:
            print("Number is even")
    else:
        break """

""" #Largest of Two: Find the larger of two numbers entered by the user.

while True:
    try:
        int1 = int(input("Enter a number: "))
        int2 = int(input("Enter other number: "))
        if int1 > int2:
            print(f"{int1} is greater than {int2}")
        elif int2 > int1:
            print(f"{int2} is greater than {int1}")
        else:
            print(f"{int1} is equal to {int2}")
    except ValueError:
        break """

""" #Simple Interest Calculator: Calculate simple interest.
    # formule = principal*annual_interes*year
while True:
    try:
        annual_interest = 1.5
        money = int(input("How much do you have money: "))
        year = int(input("How many years of maturity do you want: "))

        total = money*year*annual_interest
        print(f"Principal: {money} \nMaturity: {year} \nAnnual Interest: {annual_interest} \n ----------------- \nTotal: {total}")
    except ValueError:
        break"""


""" #* Compound Interest Calculator: Calculate compound interest.
# formule = principal*(1+ annual_interes)*year

while True:
    try:
        annual_interest = 0.7
        money = int(input("How much do you have money: "))
        year = int(input("How many years of maturity do you want: "))

        total = money*(1+ annual_interest)*year
        print(f"Principal: {money} \nMaturity: {year} \nAnnual Interest: {annual_interest} \n ----------------- \nTotal: {total}")
    except ValueError:
        break"""

""" # * Basic String Manipulation: Reverse a string, find its length, etc.
sentence = input("Enter a sentence: ")
print(sentence)
print(sentence[::-1])
print(len(sentence)) """

""" #* Vowel Counter: Count the number of vowels in a string.
sentences = input("Enter sentences: ")
vowel = "aeiouAEIOU"
vowel_sentence = []
counter = 0
for i in sentences:
    if i in vowel:
        counter += 1
        vowel_sentence.append(i)
print(vowel_sentence)
print(counter) """

""" # * Palindrome Checker: Check if a string is a palindrome.
while True:
    print("for exit enter exit")
    word = input("Enter a word: ")
    if word == "exit":
        break
    else:
        if word == word[::-1]:
            print(f"{word} is Palindrome word")
        else:
            print(f"{word} is not Palindrome word")"""

""" #* Word Counter: Count the number of words in a sentence.
sentence = input("Enter sentences: ")
word_counter = 0
word = []
for i in sentence.split(" "):
    word_counter += 1
    word.append(i)

print(word)
print(word_counter) """

""" # Character Counter: Count the occurrences of each character in a string.
sentence = input("Enter sentences: ")
character_counter = 0
character = []
for i in sentence:
    if i == " ":
        continue
    else:
        character_counter += 1
        character.append(i)

print(character)
print(character_counter) """

""" # * Data Type Checker: Determine the data type of a user-entered value.
data = input('enter a data: ')
print(type(data))
data_digit = data.isdigit()
if data_digit == True:
    data_int = int(data)
    data_float = float(data)
    print(f"Converter int:{data_int} \nConverter float: {data_float}")
else:
    print(type(data)) """

""" # Number Guessing Game (Basic): The computer generates a number, and the user guesses
import random
rand_int = random.randint(0,10)
print(rand_int)
chance = 0
right_guess = 3
while True:
    chance += 1
    if chance <= right_guess:
        guess = int(input("Guess a number: "))
        if guess > rand_int:
            print("Your guess is greater than random number")
            
        elif guess < rand_int:
            print("Your guess is smaller than random number")
            
        else:
            print("-----------------------------------------------")
            print(f"Your guess is correct \nCongurelations \nyour number: {guess} \nrandom number: {rand_int}")
            break
    else:
        print("------------------------------------------------------")
        print("You dont have right guess \nGame Over")
        break
 """

#* Rock, Paper, Scissors (Basic): A simple text-based version.
import random

game = ["Rock","Paper","Scissors"]

game_count = 0
game_right = 10
machine_skor = 0
player_skor = 0

while True:
    rand_game = random.choice(game)
    game_count += 1
    if game_count <= game_right:
        guess = input("Rock  \nPaper  \nScissors  \nChoose:   ")
        if rand_game == guess:
            print("The game is a draw")
        elif (rand_game == "Rock") & (guess == "Scissors"):
            machine_skor += 1
        elif (rand_game == "Rock") & (guess == "Paper"):
            player_skor += 1
        elif (rand_game == "Paper") & (guess == "Scissors"):
            player_skor += 1
        elif (rand_game == "Paper") & (guess == "Rock"):
            machine_skor += 1
        elif (rand_game == "Scissors") & (guess == "Paper"):
            machine_skor += 1
        elif (rand_game == "Scissors") & (guess == "Rock"):
            player_skor += 1
    else:
        print("game over")
        break

print("Machine Skor: ",machine_skor)
print("Player Skor: ",player_skor)
    
        

    
   



