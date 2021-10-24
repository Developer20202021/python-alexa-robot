# normal print check 
# print('hello bangladeshe')


# condition check
# if(3 > 2):
#     print("I am a big boy")
# else:
#     print('I am not a big boy')    



# data type check
# a = 20
# print(type(a))



# multi variabe declaration
# x, y, z = 2, 3, 4
# print(x)
# print(y)
# print(z)



# one value to multiple variables
# x=y=z=45
# print(x)
# print(z)
# print(y)


# unpacking data like javascript destructuring
# numbers = [1, 2, 3]
# x, y, z = numbers
# print(x)
# print(y)
# print(z)


# add variable 
# x = 'Mahadi Hasan'
# print('Hello I am ' + x)





# add multiple variables
# x = 2
# y = 3
# z = x+y
# print(z)


# add string and a number it will be an error
# x = 'M'
# y = 3
# print(x+y)
#  its give an error. so we can say that python can not add string + number 





# python function creation and check global variable

# x = 'hello'

# function declaration
# def add():
#     print(x + ' bangladesh')

# function calling
# add()

# print(x) check the global variable




# Global variable access from function and outside
# x = "awesome"

# def myfuction():
#     x = "my new function"
#     print(x)

# myfuction()

# print(x)



# create a new global variable using global keyword in a function 

# x = 'USA'
# def global_function():
#     global x
#     x = 'bangladesh'
# global_function()
# print(x)



# type check 
# x ='Hello python'
# print(type(x))

# x = 2
# print(type(x))

# x = 20.03
# print(type(x))

# complex data type. it indicates the complex number. j is the sigg fo complex number.
# x = 4j
# print(type(x))


# in a parenthesis number  indicates that it is start from 0 and end to 6. it can take positive and negative value.
# x = range(6)
# x = range(-6) 
# print(x)

# list type like an array 
# x = [2, 3, 4, 5]
# print(type(x))


# tuple type 
# x = (2, 3, 4, 5)
# print(x)
# print(type(x))


# dictonary type  it like a object .it's called dict
# x = {"name":"apple", "price":300000, "memory":"32GB"}
# print(x)
# print(type(x))


# set data type like a methematical set
# x = {1, 2, 3, 4, 5}
# print(x)
# print(type(x))



# frozenset data type like set but at first is used a keyword frozenset

# x = frozenset({1, 2, 3, 4, 5})
# print(x)
# print(type(x))



# bool data type 
# x = False
# print(x)
# print(type(x))

# bytes data type
# x = b"hello"
# print(x)
# print(type(x))



# memory view data type 
# x = memoryview(bytes(5))
# print(x)
# print(type(x))


            # python Numbers

#anny number like -something to + anything 
# x = -5 
# print(x)
# y = 50.09
# print(y)
# z = 2j complex number 
# print(z)

# use e for power of 10 like normal mathematics
# x = 45e3 
# print(x)
# x = 45E6
# print(x)


# complex number 
# x = 3
# y = 3j
# z = x + y
# print(z) answer (3+3j)



# convert from one data type to another
# x = 2
# print(str(x))
# print(float(x)) answer 2.0
# print(complex(x)) answer (2+0j)



# import random module for using random number 
# import random
# x = random.randrange(2,20, 2)
# print(x)
# x = random.randint(2, 10)
# print(x)
# give us a byte data. In randbytes parerthesis number give us each part of byte. But it always to be n-1.
# x = random.randbytes(50)
# print(x)


# Castin
# x = 2
# print(float(x))


# String
# multiline string use triple qoute
# a = """
# i 
# am 
# a 
# boy
# """
# print(a)




        # String

# access element from a string
# a = 'hello world'
# print(a[6])
 

#  for loop on string 
# x = 'hello world'
# for a in x:
#     print(a)

# check length of a string 
# a = "hello world"
# print(len(a))


# check a text in  sentence 
# x = 'It is called String'
# print('s' in x) it return us a bool type True or False.

# check text
# x = 'Hello python'
# if 'python' in x:
#     print('yes')
# else:
#     print('No')




# check not in 
# x = 'hello'
# if 'a' not in x:
#     print('yes')


        # string slicing 

# x = 'hello world'
# print(x[:]) hello world 
# print(x[3:6]) lo 
# print(x[:7]) hello w
# start from end position to start position
# - index indicates the the right to left 
# print(x[-len(x):])

       
       
       
       
       
        # String Modify

# x = 'hello world' 
# print(x.upper()) HELLO WORLD
# print(x.lower()) hello world
# print(x.strip()) remove white space from start or end side
# x = '      hello world' 
# print(x)       hello world
# print(x.strip()) hello world

# split by white space 
# print(x.split(' ')) ['hello', 'world']



# Replace a character by another character
# print(x.replace('h', 'j')) jello world


        # string Concatanation


# x = 'hello'
# y = 'World'
# z = x + y
# print(z) helloWorld
# z = x+" " +y
# print(z) hello World


        # Python Format String 

# x = 'I am {}'
# age = 23
# print(x.format(age)) I am 23



# add many number in a sentence 
# x = "I am {}. my Roll Number is {}. My class {}"
# age = 23
# roll = 1
# Class = 11
# y = x.format(age, roll, Class) 
# print(y) I am 23. my Roll Number is 1. My class 11




# test for a new line
# name = 'mahadi \n'
# print(name*4) mahadi
# mahadi
# mahadi
# mahadi


# if you declare a new string and it is very eassential for use same quotation in a string. Follow this instruction. use \ symbol before quotation , tab , new line etc  escape character
# text = 'hello world in \'python\' '
# print(text) hello world in 'python'

# use tab 
# x = 'hello \t'
# print(x*5) hello   hello   hello   hello   hello


# x = 'hello \b'
# print(x*5)









        #Python - String Methods

# capitalized 
# x = 'hello{}'
# print(x.capitalize()) Hello

# it will be return Hello to hello. first letter small
# x = 'Hello'
# print(x.casefold()) hello
# print(x.center(0))
# it counts the string basis of a pass as an argument in the count method 
# print(x.count('l')) 2
# if x string is ended by o character| return true or false
# in this case it will return True 
# print(x.endswith('o'))  True

# it will add the value which we will pass as a format method argument and it will sit in the x string placeholder. in python placeholder symbol {}
# print(x.format(' hello'))

# it returns index number of a character from a string
# print(x.index('o'))


# it returns that  string is included alphanumeric character 
# print(x.isalnum()) false 
# print(x.isalpha()) false 
# print(x.isascii()) True


# condition check
# print(7>6 and 3<6)






# boolean check
# x = ('')
# print(bool(x)) False
# x = 0
# print(bool(x)) False except 0 anny number True 
# x = {}, x=[], x=()
# print(bool(x)) False 
# x = None
# print(bool(x)) False 


# isinstance like type it return true or false basis of data type

# x = 20
# print(isinstance(x,str)) False



                # Operator

# print(1+3) 4
# print(1-3) -2
# print(3*3) 9
# print(3/9)  0.3333333333333333
# print(int(0.3333333333333333)) 0


# "is " is used for check object that is it located same location in memory?
# x = {'a':3, 'b':4}
# y = x
# print(y is x) True if we put variable (which contains object) in a new variable it will be true because they are located in the same location in memory

# y = {'a':3, 'b':4}
# print(y is x) False but we declare a new variable and set a new object same as first object .the print funcftion return False.Because it is reapted.and it is created again as a new object though it looks like same but memory location is deffirent.






thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# thislist[2:6] it takes from index no 2 to (6-1)
# print(thislist[2:6])

# it  takes from 0 index to (5-1)
# print(thislist[:5])

# it takes from 1 to end 
# print(thislist[1:])

# it takes from 0 to end 
# print(thislist[:])

# In python when we use negative index . it must be started from last index 

# print(thislist[-4:-1]) ['orange', 'kiwi', 'melon']



# if "apple" :
#         print(thislist.index("apple" ))
# else:
#         print('No')
     

        # Python - Change List Items  
        
         
# add a new value in 4 index 
# thislist[4] = "blackcurrant"
# print(thislist) ['apple', 'banana', 'cherry', 'orange', 'blackcurrant', 'melon', 'mango']



# add multiple value by use range 
# thislist[1:3] = ["a", "b"]
# print(thislist) ['apple', 'a', 'b', 'orange', 'kiwi', 'melon', 'mango']





# insert method takes two values first index number and second value 
# thislist.insert(2, "banana")
# print(thislist) ['apple', 'banana', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
# thislist.insert(len(thislist), 'End')
# print(thislist) ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'End']



                # Python - Add List Items

# use append method to insert a new item in list at the end position

# thislist.append('end')
# print(thislist) ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'end']


# extend method is used for add new list item to another list

# price = [23, 33, 44, 45, 67, 34]
# thislist.extend(price)
# print(thislist)
# ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 23, 33, 44, 45, 67, 34]



# an error occured. solve it
# price = (23, 33, 44, 45, 67, 34)
# thislist.extend(price)
# price(thislist)




# Remove an specific item 
# thislist.remove('banana')
# print(thislist) ['apple', 'cherry', 'orange', 'kiwi', 'melon', 'mango']


# in python pop method is used for a specific indexed data remove from a list.
# pop method takes an argument as a index number.
# thislist.pop(1)
# print(thislist) ['apple', 'cherry', 'orange', 'kiwi', 'melon', 'mango']



# if you do not give any argument as a number it remove the last item from a list 
# thislist.pop()
# print(thislist) ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon']


# del keyword is used for delete an specific item from a list 
# del thislist[0]
# print(thislist) ['banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']


# clear method delete all item from a list 
# thislist.clear()
# print(thislist) []




                # Python - Loop Lists

# Loop throw on a list 

# for x in thislist:
#         print(x)
# apple
# banana
# cherry
# orange
# kiwi
# melon
# mango

# range always give us to n-1 
# if we pass 120 it will give us 0 to 119
# beacause 0 to 119 length is 120
# for i in range(len(thislist)):
#         print(thislist[i])
# apple
# banana
# cherry
# orange
# kiwi
# melon
# mango


# while loop 

# i = 0
# while i < len(thislist):
#         print(thislist[i])
#         i+=1

# apple
# banana
# cherry
# orange
# kiwi
# melon
# mango





        # Python - List Comprehension
        # List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# sortting the list by character 
# thislist.sort()
# print(thislist) ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'melon', 'orange']

# sort descending 
# thislist.sort(reverse=True)
# print(thislist)
# ['orange', 'melon', 'mango', 'kiwi', 'cherry', 'banana', 'apple']


# newlist = []
# for x in thislist:
#         if "a" in x:
#                 newlist.append(x)
#                 print(newlist)
#         else:
#                 print("No")
# print(newlist) 
# ['apple', 'banana', 'orange', 'mango'] for "a"
# ['banana'] for "b"



# sortcut 
# newlist = [x for x in thislist]
# print(newlist)
# ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']



# copy a list 
# newlist = thislist.copy()
# print(newlist)
# ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']

# newcopylist = thislist.copy()
# newcopylist.extend(thislist)
# print(newcopylist)

# for x in range(20):
#         print('x'*x)
#         for a in range(20):
#                 print('*'*a)




        # `Tupple`
        # tupple unchangeable 
# newtupple = (1, 2, 3)
# print(newtupple)
# access item 
# print(newtupple[0])
# newtupple[1] = 13
# print(newtupple) 'tuple' object does not support item assignment


# access last item  in tupple
# print(newtupple[-1])

# you can not add new value in a tupple but if you convert the tupple to list you can add a new value then you convert to the tupple
# list =list(newtupple)
# list[1] = 29
# tupple = tuple(list)
# print(tupple) (1, 29, 3)

# delete tuple 
# del newtupple
# print(newtupple) #this will raise an error because the tuple no longer exists
# (r,*c) = newtupple
# print(r)1
# print(c) [2, 3]
# print(newtupple*3) (1, 2, 3, 1, 2, 3, 1, 2, 3)



        # Declare a new Set 
# set unchanged, unordered, duplicate not allowted 

# new_set = {1, 2, 3, 4}
# # print(new_set)
# print(len(new_set)) 4

newset = set((1, 2, 3, 4))
# print(newset) {1, 2, 3, 4}

# newList = list((1, 2, 3, 4))
# print(newList) [1, 2, 3, 4]
# newset.add(55)
# print(newset) {1, 2, 3, 4, 55}

# newset.remove(3)
# print(newset){1, 2, 4}
# newset.discard(2)
# print(newset) {1, 3, 4}

# pop delete the last item . But we can not see which item is deleted. so we must write below this code 
# popitem = newset.pop()
# print(popitem)

# clear the set 
# newset.clear()
# print(newset) set()

# loop throw on set 
# for x in newset:
#         print(x)
# 1
# 2
# 3
# 4



# join two set 
# oldset = {10, 12, 14, 16}
# newset.update(oldset)
# print(newset)
# {1, 2, 3, 4, 10, 12, 14, 16}
# print(newset.union(oldset))
# {1, 2, 3, 4, 10, 12, 14, 16}

# use intersection on set 

# oldset = {1, 3, 5}
# print(newset.intersection(oldset)) {1, 3}
# newset.intersection_update(oldset)
# print(newset) {1, 3}



# fruits = {"apple", "banana", "cherry"}
# more_fruits = ["orange", "mango", "grapes"]
# fruits.update(more_fruits[:])
# print(fruits)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# print(thisdict["brand"])

# print(thisdict.get("year"))
# print(thisdict.keys())
# print(thisdict.items()) it's return a tupple
# print(thisdict.values())

# thisdict.pop("model")
# print(thisdict)



# nested dictonary 

# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }
# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }
# myfamily2 = myfamily.copy()
# print(myfamily2)




# ternary operator 


# a = 1
# b = 2

# # print('ok') if a>b else print('something') if a==b else print("not ok")
# if 5 > 2: print("Five is greater than two!")


# for loop
# third parameret control the increment 
# for x in range(2, 30, 3):
#   print(x)




# class Person :
#        def __init__(self, fname, lname):
#            self.fname = fname
#            self.lname = lname
        

#          If I use underscore underscore at first of a method in a class .That means It can not be accessable by outside of the class 
#        def __get_lname(self):
#                return self.lname




#        def get_property(self):
#                return self.lname
#                  print(f"my first name {self.fname} and my last name is {self.lname}")


#  inheritence 


# # pass actually when used. when We want to all properties from a superclass which is called parent and we can not set any property in the sub class if we use pass keyword.

# class Student(Person) :
#         pass

# class Student(Person):
#         def __init__(self, fname, lname,age:int, tshirt:bool=True):
#             super().__init__(fname, lname)
#             self.age = age
#             self.tshirt = tshirt
#         def get_property(self):
#             return (f"my first name {self.fname} and my last name {self.lname} and my age is {self.age} and I have not any new T-shirt{self.tshirt} ")

#              you can pass any string in this case you would not access any method .directly you can print the class based object 

#         def __str__(self) :
#            return (f"my first name {self.fname} and my last name {self.lname} and my age is {self.age} and I have not any new T-shirt{self.tshirt} ")


# s = Student("mahadi", "hasan",23,False)
# print(s)
# print(s.get_property())
# my first name mahadi and my last name hasan and my age is 23 and I have not any new T-shirtFalse
# p = Person("mahadi", "hasan")
# print(p.get__property())





# import platform 
# # to get all the functions as a list from a module by using the dir keyword
# print(dir(platform))


import datetime as dt

# print(dir(dt))
# ['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

# x = dt.datetime.now()

# print(x.strftime("%j"))


# import math
# print(math.pi)


# import json
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# json to python convert way 
# print(json.loads(x))
# convert python to json 
# print(json.dumps(x))







# import pyttsx3 as tts

# speaker = tts.init()
# file = open("hello.txt")

# for read a file .Read() method takes one parameter. that is that how many characters it will read from a file
# readable = file.read()

# for only one line reading 
# readable = file.readline()
# print(readable)
# speaker.say(readable)
# speaker.runAndWait()
# print(dir(tts))

# f = open("hello.txt", "rt")
# readable = f.read()
# print(readable)


# a for append. it is used to append a new line. it does not delete any character from this file. but when you will use w method it's overwrite your file and delete the whole value from then it will write this text.
# f = open("hello.txt", "a")
# f.write("thanks for writting")
# f.close()
# hello my name is mahadi You can return one line by using the readline() method:thanks for writting



# use the w method 
# f = open("hello.txt", "w")
# f.write("ows it is already deleted for my mistake")
# # f.close() it is a good practice 
# # ows it is already deleted for my mistake
# f = open("hello.txt")
# print(f.read())


# create a new file 
# x method is used for creating a new file 
# f = open("common.txt", "x")
# f.write("hello from python")
# f.close()
# f = open("common.txt","rt")
# print(f.read())




# to remove a file 
# import os
# if os.path.exists("common.txt"):
#         os.remove("common.txt")







        

