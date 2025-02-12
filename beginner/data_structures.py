"""
Data Structures (Lists, Tuples, Dictionaries) (20 Projects)
* List Manipulation: Add, remove, and modify elements in a list.
* List Sorting: Sort a list of numbers or strings.
* Finding Duplicates: Find duplicate elements in a list.
* Removing Duplicates: Remove duplicate elements from a list.
* List Comprehension Practice: Use list comprehensions for various tasks.
* Tuple Operations: Practice using tuples for storing data.
* Dictionary Creation and Manipulation: Create and manipulate dictionaries.
* Word Frequency Counter: Count the frequency of words in a text file.
* Student Management System (Basic): Store student data in a dictionary.
* Phonebook (Basic): Store contacts in a dictionary.
* Inventory Management (Basic): Manage inventory using dictionaries.
* Shopping List: Create and manage a shopping list using a list.
* Movie List: Store movie information in a list of dictionaries.
* Library Management (Basic): Manage books and members using dictionaries and lists.
* Simple Voting System: Tally votes using a dictionary.
* Anagram Checker: Check if two words are anagrams.
* Common Elements: Find common elements between two lists.
* Merging Lists: Merge two lists into one.
* Stack Implementation: Implement a stack data structure using a list.
* Queue Implementation: Implement a queue data structure using a list.

"""

#* List Manipulation: Add, remove, and modify elements in a list.
"""list = [1,"book",3.14,True]
print(list)
list.append("lesson")
print(list)
list[1] = "one"
print(list)
list[3] = False
print(list)
list[0]= 500
print(list)
list.pop()
print(list)
list.remove("one")
print(list)"""

#* List Sorting: Sort a list of numbers or strings.
"""obje = ["zoo","animal","monkey","donkey","tiger"]
print(obje)
obje.sort()
print(obje)
obje.reverse()
print(obje)

number = [50,250,0.1,2022,0.001,8]
print(number)
number.sort()
print(number)
number.reverse()
print(number)"""

#* Finding Duplicates: Find duplicate elements in a list.

"""again = [2,"non",True,True,False,359,3.14,"me","you","you"]
print(again)
list_repeat = []
no_repeat = []
for i in again:
    if i in no_repeat:
        list_repeat.append(i)
    else:
        no_repeat.append(i)

print(list_repeat)
print(no_repeat)"""

#* Removing Duplicates: Remove duplicate elements from a list.
"""again = [2,"non",True,True,False,359,3.14,"me","you","you"]
print(again)
remove_obje = []
list_ = []
for i in again:
    if i in list_:
        remove_obje.append(i)
        again.remove(i)
    else:
        list_.append(i)

print(again)"""

#* List Comprehension Practice: Use list comprehensions for various tasks.
"""list_ = ["Mercedes","BMW","Volvo","Bugatti","Renault","Citroen","Aston Martin"]
new_list = [i for i in list_ if i !="Citroen"]
print(new_list)

newlist = [x for x in new_list if x =="Bugatti"]
print(newlist)

list_upper = [x.upper() for x in list_] 
print(list_upper)"""

#* Tuple Operations: Practice using tuples for storing data.

"""data_tuple=("banana",1,3.14)
print(data_tuple)

tuple1 = (1,1,2,3,"apple","apple","banana",3.14)
print(tuple1)
print(tuple1[5])
print(tuple1[2:5])
print(tuple1[:4])
print(tuple1[4:])
print(tuple1[::-1])

tuple1_list = list(tuple1)
tuple1_list[3] = 5
tuple1 = tuple(tuple1_list)
print(tuple1)

del tuple1
print(tuple1)

tuple1 = ("Bakur","Basur","Rojava","Rojhilat")
tuple2 = ("=","Kurdistan")
tuple3 = tuple1 + tuple2
print(tuple3)

tp = (1,2,3)
tp1 = (2,3,4,5)
tp2 = tp + tp1
print(tp2)
print(tp2.count(2))
print(tp2.index(5))"""

# * Dictionary Creation and Manipulation: Create and manipulate dictionaries.
"""mydict = {
    "computer":"ordinateur",
    "car":"voiture",
    "hello":"Salut",
    "sunday":"Dimanche"
}

print(mydict)
print(mydict["hello"])
print(len(mydict))
print(type(mydict))

mydict2 = dict(name="Qazi", surname = "Muhammed", country = "Kurdistan", age = 50)
print(mydict2)
print(type(mydict2))
print(mydict2.get("surname"))
print(mydict2.keys())
print(mydict2.values())
mydict2["age"]= 55
print(mydict2)
print(mydict2.items())

age = False
if "age" in mydict2:
    age = True
    print(age)

mydict2.update({"age": 60})
print(mydict2)

mydict2["mission"] = "Free Kurdistan"
print(mydict2)
mydict2.update({"love":"Kurdistan"})
print(mydict2)

dict1 = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
}
print(dict1)
dict1.pop("two")
print(dict1)
dict1.popitem()
print(dict1)

#del dict1
#print(dict1)
dict1.clear()
print(dict1)

dict1 = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
}
for i in dict1:
    print(i)

for i in dict1:
    print(dict1[i])

for i in dict1.values():
    print(i)
for i in dict1.keys():
    print(i)
print("----------------------------------------")
for i,j in dict1.items():
    print(i,j)

print("*************************")
copy_dict1 = dict1.copy()
print(dict1)
print("----------------------------------------")
print(copy_dict1)

students = {
    "students1" :{
        "name": "Zozan",
        "age":2004
    }, 
    "students2": {
        "name": "Berfin",
        "age":2005
    }, 
    "students3" :{
        "name": "Bercem",
        "age":2006
    },           
}
print(students)

print(students["students2"]["name"])

for i,obje in students.items():
    print(i)
    for x in obje:
        print(x + ":" , obje[x]) 

    """
# * Word Frequency Counter: Count the frequency of words in a text file.
"""from collections import Counter
text = "The prehistory of the Kurds is poorly known, but their ancestors seem to have inhabited the same upland region for centuries or, as some have argued, millennia. The records of the early empires of Mesopotamia contain references to mountain tribes with names that some have suggested resemble the ethnonym Kurd, such as the Guti of the 3rd and 2nd millennia bce. The Kardouchoi whom the Greek historian Xenophon speaks of in Anabasis (they attacked the “Ten Thousand” near modern Zākhū, Iraq, in 401 bce) may have been Kurds, but some scholars dispute this claim. The name Kurd can be dated with certainty to the time of the tribes’ conversion to Islam in the 7th century ce. Most Kurds are Sunni Muslims, and among them are many who practice Sufism and other mystical sects. Although several historical dynasties have been led by Kurdish rulers, such as the Ḥasanwayhid dynasty, the ʿAnnazid dynasty, and, most famously, the Ayyubid dynasty, the Kurds have never achieved nation-state status in the modern era."

count_word = Counter()
text = text.split()
for i in text:
    count_word[i] += 1
print(count_word)"""


# Student Management System (Basic): Store student data in a dictionary.
"""students = {
    "students1" :{
        "name": "Zozan",
        "age":2004
    }, 
    "students2": {
        "name": "Berfin",
        "age":2005
    }, 
    "students3" :{
        "name": "Bercem",
        "age":2006
    },           
}
print(students)"""

# * Phonebook (Basic): Store contacts in a dictionary.
"""phonebook={
    "mehmet":"+355678493903",
    "ahmet":"+4556784446903",
    "murat":"+6656784935653",
    "kerem":"+63897643730",
    "ayse":"+15678è760903"
}  
print(phonebook)"""

#* Inventory Management (Basic): Manage inventory using dictionaries.
"""inventory = {
    "apple":{
        "iphone16":33,
        "iphone16 plus":54,
        "iphone16 Pro": 12,
        "iphone16 Promax": 10
    },
    "samsung":{
        "S24":35,
        "S24 Ultra":9,
        "S25":30,
        "S25 Ultra":22,
    },
    "xiaomi":{
        "14T":25,
        "14T Pro":19,
        "15T":10,
        "16T Pro":22,
    }
}
print(inventory)"""

#* Shopping List: Create and manage a shopping list using a list.
"""shopping_list = {
    "legumes": ["potato","beans","cucmber","celery","carrot","onion"],
    "fruits": ["strawberry", "apple","pear", "watermelon","grape"],
    "breakfast": ["cheese", "salami","eggs","goats cheese","milk"],
    "meat": ["turkey", "veal","lamb","chicken"],

}
print(shopping_list)"""

# * Movie List: Store movie information in a list of dictionaries.
"""movie_list = {
    "The Shawshank Redemption":{
        "year":1994,
        "Dure": "2h 22m",
        "Director": "Frank Darabont",
        "Stars": ["Tim Robbins","Morgan Freeman","Bob Gunton"],
        "Genre":["Drama"],
         "Rate": "9.3/10"

    },
    "The Godfather":{
        "year":1972,
        "Dure": "2h 55m",
        "Director": "Francis Ford Coppola",
        "Stars": ["Marlon Brandon","Al Pacino","James Caan"],
        "Genre":["Drama","Crime"],
        "Rate": "9.2/10"

    },
    "Angry Man":{
        "year":1957,
        "Dure": "1h 36m",
        "Director": "Sidney Lunet",
        "Stars": ["Henry Fonda","Lee J. Cobb","Martin Balsam"],
        "Genre":["Drama","Crime"],
        "Rate": "9.0/10"

    }
}
print(movie_list)"""

# * Anagram Checker: Check if two words are anagrams.
"""from collections import Counter
while True:
    print("For exit enter 'q' ")
    word1 = input("Enter 1. Word: ")
    if (len(word1))< 2:
        break
    else:
        word2 = input("Enter 2. Word: ")
        if (Counter(word1) == Counter(word2)):
           print(f"{word1} and {word2} are anagrams.")
        else:
            print(f"{word1} and {word2} aren't anagrams.")"""

# * Common Elements: Find common elements between two lists.

"""list1 = ["try",2,"python","pandas","machine learning","deep learning",3.14]
list2 = ["machine learning",4,1000,"deep learning","python",3.14]

some_value = []
for i in list1:
    for j in list2:
        if i == j:
            some_value.append(i)
print(some_value)"""

# * Merging Lists: Merge two lists into one.

"""list1 = ["try",2,"python","pandas","machine learning","deep learning",3.14]
list2 = ["machine learning",4,1000,"deep learning","python",3.14]

list3 = list1+list2
print(list3)

list4 = ["try",2,"python","pandas","machine learning","deep learning",3.14]
list5 = ["machine learning",4,1000,"deep learning","python",3.14]

list4.extend(list5)
print(list4)

from itertools import chain
list_chain = list(chain(list1,list2))
print(list_chain)"""


# * Stack Implementation: Implement a stack data structure using a list.
"""stack = []
count_stack = int(input("How many do you want to add obje? "))
for i in range(count_stack):
    obje = input("Enter obje: ")
    stack.append(obje)
print(stack)

for i in range(count_stack):
    stack.pop()
print(stack)"""


# * Queue Implementation: Implement a queue data structure using a list.
"""list1 = ["python","machine learning","deep learning","robotic","artifical intellengence"]
while True:
    add_queue = input("enter object: ")
    if len(list1) < 5:
        list1.append(add_queue)
        
    else:
       print(list1)
       del list1[0]
       list1.append(add_queue)
       print(list1)
"""
