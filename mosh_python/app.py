age = 20

price = 19.95

first_name = "aaryan"

is_online = True

is_online = False

# Input 

# name = input('What is your name? ')

# birth_year = input('Enter your bith year ')

# age = 2026 - int(birth_year)

# print("Hello " + name) 

# print(age)

#
# first = input('First : ')
# second = input("Second: ")

# sum = float(first) + float(second)

# print("Sum " + str(sum))

##
# course= "Python for beginners"

# print(course.upper())

# print(course.lower())

# print(course.find("for"))

# print(course.replace("for", '4'))

# print("Python" in course)

# print(course)

##Artithmatic operations

print(10+3)

print(10-3)

print(10//3) #double slash return in single / return float

print(10 ** 3) #power

x = 10

x= x+3

x+=3 #Agmented assign operator

x-=3

print(x)

#Comparison operator
x = 3 > 2

x = 3 < 2

x = 3 >= 2

x = 3 <= 2

x = 3!=2

x = 3==2


print(x)

# Logical Operator

price = 25

print(price > 10 and price < 30)

print(price > 10 or price < 30)

print(not price > 10 )

temperature = 25

if temperature > 30:
    print("It's a hot day")
    print('Drink plenty of water')
elif temperature > 20: # [20 : 30]
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's cold")
print('Done')

# weight = int(input('Weight: '))
# unit = input("(K)g or (L)bs: ")

# if unit.upper() == "K":
#     converted = weight / 0.45
#     print("Weight in Lbs:" + str(converted))
# else:
#     converted = weight * 0.45
#     print('Weight in Kgs:' + str(converted))

# i = 1

# while i <= 10:
#     print(i * "*")
#     i = i+1

# List
names = ["John", "Bob", "Mosh", "Sam", "Mary"]

names[0] = "Jon"

print(names[0 : 3])

numbers = [1,2,3,4,5]

numbers.append(6)

numbers.insert(0,-1)

numbers.remove(3)

print(1 in numbers)

print(len(numbers))

for i in numbers:
    print(i)

print(numbers)

numbers = range(5, 10, 2)

for number in numbers:
    print(number)

numbers = (1,2,3,3)

print(numbers.count(3))

