# Dear Epsilon Students, 
# The More you practice The better You'll Be.
## <p style="color:yellow;"Answers By Ibrahim Saber 
### Instructions: 
# - Make sure that you understand this topics before you start.
# - If you found something hard to do, try and try then google it and finally ask someone. 
# - You can divide this work into daily tasks so that you do not feel pressure.
# - After you finish, go to model answer and rate yourself. 
# - If you find something ambiguous, Try to make a hypothesis to solve a problem. 

### Question classification: 
# - Green is level 1 
# - Orange is level 2 
# - Red is level 3 

# <center> Let's start 💪 </center> 
## <p style="color:green;">Q.01 Reassign 'hello' in this nested list to say 'goodbye' instead</p>
list3 = [1,2,[3,4,'hello']]
# Answer here 
list3 = [1,2,[3,4,'hello']]

list3[2][2] = 'goodbye'

print(list3)
## <p style="color:green;">Q.02 Sort the list below</p>
list4 = [5,3,4,6,1]
# Answer here 
list4 = [5,3,4,6,1]
list4.sort()
print(list4)
## <p style="color:orange;">Q.03 Write a Python program to remove duplicates from a list.</p>

#part 1 :)
# this Answer, If you want me to make the list myself :)
#----------*-*-----------*-*-----------*-*---------*-*-----------------*-*-----------*-*--------------*-*

list1 = [1,2,3,4,5,2,6,4,1,2,5,4,2,6,7,8,5]

# Convert the list to a list of unique elements
list2 = list(set(list1))

#printing
print('List of unique values ​​=',list2)
# part 2
# this Answer, If you want the user to input the list :)
#----------*-*-----------*-*-----------*-*---------*-*-----------------*-*-----------*-*--------------*-*


list0 = input("Enter a list of elements separated by spaces: ")

# Convert it into a list of elements
list1 = list0.split()

# Convert it into a list of unique elements.
list2 = list(set(list1))

#printing
print("Original List:", list1)
print("List of unique values ​​=", list2)

## <p style="color:green;">Q.04 Using keys and indexing, grab the 'hello' from the following dictionaries:</p>
d = {'k1':{'k2':'hello'}}


# Answer here no.1:
d = {'k1': {'k2': 'hello'}}

# Using indexing
d2 = d['k1']['k2']

print(d2)

# Answer here no.2:

d = {'k1': {'k2': 'hello'}}
#printing
print(d['k1']['k2'])
## <p style="color:orange;">Q.05 Using keys and indexing, grab the 'hello' from the following dictionaries:</p>
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
# Answer here 

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

d['k1']
d['k1'][0]
d['k1'][0]['nest_key']
d['k1'][0]['nest_key'][1]
d['k1'][0]['nest_key'][1][0]

#The answer is more readable here :)

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

d['k1'][0]['nest_key'][1][0]

## <p style="color:red;">Q.06 Using keys and indexing, grab the 'hello' from the following dictionaries:</p>
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
# Answer here 

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

d['k1']
d['k1'][2]
d['k1'][2]['k2']
d['k1'][2]['k2'][1]
d['k1'][2]['k2'][1]['tough']
d['k1'][2]['k2'][1]['tough'][2]
d['k1'][2]['k2'][1]['tough'][2][0]
#The answer is more readable here :)

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

d['k1'][2]['k2'][1]['tough'][2][0]
## <p style="color:green;">Q.07 Write a Python script to add a key and value to a dictionary.</p>
# Sample Dictionary : {0: 10, 1: 20}

# Expected Result : {0: 10, 1: 20, 2: 30}
# Answer here 
## using --update method.
dict = {0:10,1:20}

dict.update({2:30})

dict
# Answer here

dict = {0:10,1:20}

dict[2]=30

dict
## <p style="color:green;">Q.08 Write a Python program to add an item in a tuple.</p>

# Answer here

tuple1 = (1, 2, 3, 'a', 'b')

tuple2 = tuple1 + ('c','g',)

print(tuple2)

## <p style="color:green;">Q.09 Write a Python program to convert a tuple to a string.</p>

# Answer here 
my_tuple = ( 'a', 'b', 'c')

my_list = list(my_tuple)

my_str = ''.join(my_list)

print(my_str)
# Answer here

my_tuple = (1, 2, 3, 'a', 'b', 'c')


my_str = ''.join(map(str, my_tuple))

print(my_str)

## <p style="color:green;">Q.10 Write a Python program to remove item(s) from a given set.</p>

# Answer here 
my_set = {1,2,3,4,5,6,7}

items_to_remove = {5,7}

my_set -= items_to_remove

print("Set after removing items:", my_set)

# Answer here

my_set = {1, 2, 3, 4, 5, 6, 7}

my_set.remove(5)
my_set.remove(7) 

print("Set after removing items:", my_set)

# Answer here 

my_set = {1, 2, 3, 4, 5, 6, 7}

items_to_remove = {5,7}

my_set.difference_update(items_to_remove)

print("Set after removing items:", my_set)

## <p style="color:orange;">Q.11 Write a Python program to create an intersection of sets.</p>
# > Explanation : In mathematics, the intersection of two sets A and B, denoted by A ∩ B, is the set containing all elements of A that also belong to B (or equivalently, all elements of B that also belong to A).
# Answer here way no.1

set1 = {1,2,3,4,5,6,7}
set2 = {5,6,7,8,9,10,11}

set3 = set1.intersection(set2)

##print(set3)
print("Set 1:", set1)
print("Set 2:", set2)
print("Intersection of sets 1 and 2:", set3)
# Answer here way no.2

set1 = {1,2,3,4,5,6,7}
set2 = {5,6,7,8,9,10,11}

##print(set1 & set2)

print("Set 1:", set1)
print("Set 2:", set2)
print("Intersection of sets 1 and 2:", set1 & set2)
# Answer here way no.3

def set_intersection(set1,set2):
    set3 = set1.intersection(set2)
    return set3

# Example:
set1 = {1,2,3,4,5,6,7}
set2 = {5,6,7,8,9,10,11}
set3 = set_intersection(set1,set2)
##print(set3)

print("Set 1:", set1)
print("Set 2:", set2)
print("Intersection of sets 1 and 2:", set3)
## <p style="color:orange;">Q.12 Write a Python program to create a union of sets.</p>
# > Explanation :In mathematics, The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. 
# Answer here 

set1 = {1,2,3,4,5,6}
set2 = {5,6,7,8,9,10}

set3 = set1.union(set2)

print(set3)
# Answer here 

set1 = {1,2,3,4,5,6}
set2 = {5,6,7,8,9,10}

print(set1.union(set2))
# <center> Thank's for your effort ❤️ </center> 