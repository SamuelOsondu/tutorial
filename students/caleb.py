#data structures
#data structures are the way to store and organize data efficiently so that operationlike searching, inserting,and deleting data can be performed effectively.

#common data structures in python

#1 list (Dynamic arrays)
#2 Tuple(Immutable sequences)
#3 Dictionaries(Key-value pairs)
#there are others like set, stacks ,queues,linked list,Trees & graphs

#LIST
#list are like array but can store different types of data and can grow dynamically.
#list is identified by = []
#example
#creating a list
#fruits = ["apple", "mango", "orange"]

#accessing elements inside the list
#print(fruits[0]) #apple

#list can be modified ie you can add(append) or delete(remove)
#eg
#fruits.append("cola") adds
#fruits.remove("mango")#removes

#iterating through a list
#for fruits in fruits:
    #print(fruit)


#2
#TUPLE
#A tuple can be said to be a list that cannot be modified after created ie immutable.
#tuples are identified by = ()

#creating a tuple
#colors = ("green", "blue", "black")

#accesing a tuple
#print(colors[0])
#tuples are immutable so they cannot be modified eg
#colors = "yellow"... will throw an error but a tuple can be accessed by converting a tuple to list and then be accessd
#eg
#colors_list =(colors)
#colors_list.append("yellow")
#colors = tuple(colors_list)
#print(colors)#output: ('green','blue','black','yellow'.)
#NB tuple is used when you want a fixed data that shouldn't be changed also
#when u need faster access(tuple are faster than list)


#proplems in list and tuple with their solution
#q1
#write a function second _largest(1st)that takes a list of integers and returns the second largest number.
#i
#if the list has has fewer than two unique numbers rtn none
#ii
#do not use sort() or sorted().

#solution
def second_largest(lst):
    first = second = float('-inf') #initializing a negative infinity

    for num in lst:
        if num > first:
            second = first #move first to second
            first = num #update first
        elif first > num > second:
            second = num #update second
    return second
print(second_largest([10, 20, 4, 45, 99, 99]))
# print(second_largest([-2, 2, 3, ]))
