#a="Arun"
#word="hello {}"
#new_word = word.format(a)
#print(new_word)

#using format keyword to replace value
Monday = "monday"
name = input("Enter your name\n")
word ="Today is {} and I am very excited to announce that {} is in the house"
new_word = word.format(Monday,name)
print(new_word)


#using f-string to replace values

friends = ["Ashwin","Darshana","Vaishnavi","Roly"]
for friend in friends:
	print(f"{friend} is my friend")

#lambda functions in python



###################################################

add = lambda x,y: x+y

sum=add(5,6)
print(sum)


multiply = (lambda x,y : x*y)

product = multiply(5,7)
print(product)

#lambda is useful while operating with lists as shown below

def double(x):
	return x*2

sequence = [1,2,3,4]
doubled = [double(x) for x in sequence]
print(doubled)

#the above code can be reqritten in one line as
doubled2=[(lambda x:x*2)(x) for x in sequence]
print(doubled2)
#Also can be written as
doubled1=map(double,sequence)
print(list(doubled1))


#collecting multiple arguments in a functions
def multiply(*args):
	total = 1
	for arg in args:
		total = total * arg

	return total

print(multiply(3,6,9))  # 3 X 6 X 9 = 162

#provide a list of values to an add function
def add(*args):
	total = 0
	for arg in args:
		total+=arg

	return total

list1=[1,2,3,4,5,6]  # 1 + 2 + 3 + 4 + 5 + 6 = 21

print(add(*list1))    #notice the list is given as arguments by adding the *


#Now if we have a dictionary with 2 keys and the function add has the same number of arguments then we can pass the arguments
#using **
#see below

def add2(x,y):
	return x+y

dict1={'x':1,'y':2}

print(add2(**dict1))

#this is same as

print(add2(dict1['x'],dict1['y']))

#also same as

print(add2(x=dict1['x'],y=dict1['y']))


#now we will define an apply function that will add or multiply depending on the operator used.

def apply(*args,operator):
	if operator=="+":
		return add(*args)
	elif operator=="*":
		return multiply(*args) #notice that args is passed as *.
		#this is because inside multiply function,
		#it will otherwise multiply 1 with a tuple which will end up giving us the tuple back.
		#We need to multiply each value in the tuple so it has to be provided individually and not as a tuple
	else:
		return "No valid  operator provided to apply()"

print(apply(1,2,3,4,operator="*"))
print(apply(1,2,3,4,operator="+"))
print(apply(1,2,3,4,operator="/"))


#keyword arguments kwargs.....this is very important. It is basically used to perform operations on dictionaries.

def named(**kwargs):
	print(kwargs)
	for arg,value in kwargs.items():
		print(f"{arg} : {value}")


named(name="Arun",surname="Menon")  # calling named with keyword arguments. It will print a dictionary
#note that kwargs is a dictionary, so we can use kwargs.items() function
#similarly we can unpack the arguments from a dictionary into a named function

def named1(name,age):
	print (name,age)


details={'name':"Arun", 'age':26}

named1(**details)  #similar to line 86
