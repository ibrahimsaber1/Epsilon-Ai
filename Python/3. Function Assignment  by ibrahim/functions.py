# Dear Epsilon Students, 
# The More you practice The better You'll Be.
## <p style="color:Yellow;">By : Ibrahim Saber</p>
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
## <p style="color:green;">Q.01 Write a function takes a two-word string and returns True if both words begin with same letter</p>
# > ('Levelheaded Llama') → True

# > ('Crazy Kangaroo') → False
# Answer here part1.
word_1 = input('pleas enter the first word: ')   
word_2 = input('pleas enter the first word: ')

if word_1[0] == word_2[0]:
        print('True')
else:
    print('False')
# Answer here part2.

def dose_first_letters_the_same(word_1,word_2):
    if word_1[0] == word_2[0]:
        return True
    else:
       return False
# Answer here part3.

word_1 = input('pleas enter the first word: ')   #('Levelheaded Llama') → True  ('Crazy Kangaroo') → False
word_2 = input('pleas enter the first word: ')
dose_first_letters_the_same(word_1,word_2)
## <p style="color:green;">Q.02 Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd</p>

# > (2,4) → 2

# > (2,5) → 5
# Answer here part 1.
num1 = 2
num2 = 5

if num1 %2 == 0 and num2 %2 == 0:
    if num1 < num2 :
        print(num1)
    else:
        print(num2)
else:
    if num1 < num2 :
        print(num2)
    else:
        print(num1)
# Answer here part 2.
def return_lesser_num_if_even_bigger_num_if_not_even(num1,num2):
    if num1 %2 == 0 and num2 %2 == 0:
        if num1 < num2 :
            print(num1)
        else:
            print(num2)
    else:
        if num1 < num2 :
            print(num2)
        else:
            print(num1)
# Answer here part 3.
num1 = int(input('pleas enter your first number:')) #2
num2 = int(input('pleas enter your second number:'))  #5
return_lesser_num_if_even_bigger_num_if_not_even(num1,num2)
## <p style="color:green;">Q.03 Write a function that capitalizes the first and fourth letters of a name</p>
# > ('macdonald') → MacDonald
# Answer here 
name = 'macdonald'
name = list(name)
for i in range(len(name)):
    name[0] = name[0].upper()
    name[3] = name[3].upper()
name_new = "".join(name)
name_new
def capitalize_0_and_3_index(name):
    name = list(name)
    for i in range(len(name)):
        name[0] = name[0].upper()
        name[3] = name[3].upper()
    name_new = "".join(name)
    return name_new
name = input('pleas enter the word: ') #'macdonald'
capitalize_0_and_3_index(name)
## <p style="color:green;">Q.04 Given a sentence, return a sentence with the words reversed</p>
# > ('I am home') → 'home am I'
# Answer here part - 1 .
sent1 = 'I am home'
sent2 = sent1.split()
sent2.reverse()
sent3 = ' '.join(sent2)
sent3
# Answer here part - 2 .
def reverse_sentence(sent1):
    sent1 = 'I am home'
    sent2 = sent1.split()
    sent2.reverse()
    sent3 = ' '.join(sent2)
    return sent3
# Answer here part - 3 .
sent1 = input('pleas enter your sentence: ')
reverse_sentence(sent1)
## <p style="color:orange;">Q.05 Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.</p>
# > has_33([1, 3, 3]) → True

# > has_33([1, 3, 1, 3]) → False

# Answer here part 1
# has_33([1, 3, 3]) → True  -------------------- has_33([1, 3, 1, 3]) → False

list1 = [1,2,3,3,4]
counter = 0
for i in range(len(list1)-1):
    if  list1[i] == 3 and list1[i+1] == 3:
        counter += 1
    else:
        counter = counter
if counter == 0:
    print("False") 
else:
    print("True") 
# Answer here part 2 .
def check_if_num_repeated_in_list(list1,num = 3):
    """
    this function help you chech If the number is repeated at least once in the list.
    input the list you want to check as list1 and the number as a second prametar num.
    """
    counter = 0
    for i in range(len(list1)-1):
        if  list1[i] == num and list1[i+1] == num:
            counter += 1
        else:
            counter = counter
    if counter == 0:
        return False
    else:
        return True
# Answer here part 3 .
list1 = [1,2,3,3,4,4,3,4]
check_if_num_repeated_in_list(list1,3)
# Answer here part 4 .
listo = input('pleas enter your number separated by a space: ') #[1,2,3,3,4,4,3,4]
list1 = [int(x) for x in listo.split()]
num = int(input('pleas enter the number you want to chech: '))  #3
check_if_num_repeated_in_list(list1,num)
## <p style="color:orange;">Q.06 BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'¶</p>

# >blackjack(5,6,7) → 18

# >blackjack(9,9,9) → 'BUST'

# >blackjack(9,9,11) → 19
# Answer here part 1 .

num1 = 9
num2 = 9
num3 = 11
sumattion = num1 + num2 + num3
if sumattion <= 21 :
    print(sumattion)
elif sumattion > 21 and num1 == 11 or num2 == 11 or num3 == 11:
    print(sumattion-10)
else:
    print("BUST")
# Answer here part 2 .
def blackjack(num1,num2,num3):
    sumattion = num1 + num2 + num3
    if sumattion <= 21 :
        print(sumattion)
    elif sumattion > 21 and num1 == 11 or num2 == 11 or num3 == 11:
        print(sumattion-10)
    else:
        print("BUST")
# Answer here part 3.
num1 = 9
num2 = 9
num3 = 11
blackjack(num1,num2,num3)
# Answer here .
num1 = int(input('pleas enter a number : '))
while num1 not in range(0,12):
    num1 = int(input('pleas enter a number between 0 and 11: '))
num1
# Answer here if you want the user to enter only a numbers between 0 to 11.
num1 = int(input('pleas enter a number : '))
while num1 not in range(0,12):
    num1 = int(input('pleas enter a number between 0 and 11: '))

num2 = int(input('pleas enter a number : '))
while num2 not in range(0,12):
    num2 = int(input('pleas enter a number between 0 and 11: '))

num3 = int(input('pleas enter a number : '))
while num3 not in range(0,12):
    num3 = int(input('pleas enter a number between 0 and 11: '))

blackjack(num1,num2,num3)
## <p style="color:red;">Q.07 SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.</p>
# >summer_69([1, 3, 5]) → 9

# >summer_69([4, 5, 6, 7, 8, 9]) → 9

# >summer_69([2, 1, 6, 9, 11]) → 14
# Answer here part 1 .

sumattion = 0
skip = False  # Flag

for i in range(len(listo)):
    if listo[i] == 6:
        skip = True  # Set the flag 
    elif listo[i] == 9:
        skip = False  # Reset the flag 
    elif not skip:
        sumattion += listo[i]  

print(sumattion)

# Answer here part 2 .
def summer_69(listo):
    sumattion = 0
    skip = False  # Flag

    for i in range(len(listo)):
        if listo[i] == 6:
            skip = True  # Set the flag 
        elif listo[i] == 9:
            skip = False  # Reset the flag 
        elif not skip:
            sumattion += listo[i]  

    return sumattion

# Answer here part 3 .
listo = [ 2, 1, 6, 9, 11]
summer_69(listo)
## <p style="color:red;">Q.08 SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order</p>

# >spy_game([1,2,4,0,0,7,5]) → True

# > spy_game([1,0,2,4,0,5,7]) → True

#  >spy_game([1,7,2,0,4,5,0]) → False

# Answer here 

list1 = [1,0,2,4,5,1,7]

found_first_zero = False # the first flag to detecte the firs zero
found_second_zero = False  # the second flag to detecte the second zero
counter = 0

for num in list1:
    if num == 0 and not found_first_zero:
        found_first_zero = True
    elif num == 0 and found_first_zero and not found_second_zero:
        found_second_zero = True
    elif num == 7 and found_first_zero and found_second_zero:
        counter += 1

if counter != 0:
    print(True)
else:
    print(False)
def spy_game(list1):
    found_first_zero = False # the first flag to detecte the firs zero
    found_second_zero = False  # the second flag to detecte the second zero
    counter = 0

    for num in list1:
        if num == 0 and not found_first_zero:
            found_first_zero = True
        elif num == 0 and found_first_zero and not found_second_zero:
            found_second_zero = True
        elif num == 7 and found_first_zero and found_second_zero:
            counter += 1

    if counter != 0:
        return True
    else:
        return False

#  check the function 
# spy_game([1,2,4,0,0,7,5]) → True -  - :) -  -  spy_game([1,0,2,4,0,5,7]) → True   -  - :) -  -  spy_game([1,7,2,0,4,5,0]) → False

list1 = [1,7,2,0,4,5,0]
spy_game(list1)
## <p style="color:green;">Q.09 Write a function that checks whether a number is in a given range (inclusive of high and low)</p>

# Answer here 
list2 = list(range(9)) #[0, 1, 2, 3, 4, 5, 6, 7, 8]
num = 3
counter = 0
for i in range(len(list2)):
    if list2[i] == num:
        counter += 1

if counter !=0:
    print(f'''the number {num} was foun in your list {counter} times''')
# Answer here 
def check_num(list2,num = 3):
    counter = 0
    for i in range(len(list2)):
        if list2[i] == num:
            counter += 1
    if counter !=0:
       print(f'''the number {num} was foun in your list {counter} times''')
# Answer here 
list2 = [0, 1, 2, 3, 2,4, 5, 6, 3,3,7, 8]
num = 5

check_num(list2,num )
## <p style="color:orange;">Q.10 Write a Python function to multiply all the numbers in a list.</p>
# > Sample List : [1, 2, 3, -4]

# > Expected Output : -24
# # Answer here 
listo = [1,2,3,-4]
def multiply(arg1,arg2):
    return arg1 * arg2
from functools import reduce
listo = [1,2,3,-4]
reduce(multiply,listo)
## <p style="color:red;">Q.11 Write a Python function that checks whether a passed string is palindrome or not.</p>
# >Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
# Answer here  part1.
word = 'nurses run'

word = word.replace(' ', '') # Remove spaces 

if word == word[::-1]:
    print("Your word is palindrome")
else:
    print("Your word is not palindrome")
# Answer here  part - 2 .
def is_palindrome(word):
    """
    this function check if a phrase, or sequence that reads the same backward as forward, 
    e.g., madam or nurses run

    this function taks only one argument every time :).............
    """
    word = word.replace(' ', '') # Remove spaces 

    if word == word[::-1]:
        return True
    else:
        return False
# Answer here  part - 3 .

word = input('pleas enter your word: ') #'nurses run'
is_palindrome(word)
## <p style="color:green;">Q.12 Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument

# Answer here 
num = [1]
new_num = (list(map(lambda arg:arg + 15,num)))
new_num
## <p style="color:green;">Q.13 create a lambda function that multiplies argument x with argument y and print the result.</p>

# Answer here 
num1 = [5]
num2 = [2]
list(map(lambda x,y: x * y ,num1,num2))
## <p style="color:orange;">Q.14 Write a Python program to filter a list of integers using Lambda. </p>
# > Original list of integers:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# > Even numbers from the said list:[2, 4, 6, 8, 10]

# > Odd numbers from the said list:[1, 3, 5, 7, 9]

# Answer here 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = list(filter(lambda x: True if x % 2 ==0 else False,numbers))
odd_nums = list(set(numbers).difference(set(even_nums)))

print(f'''Original list of integers: {numbers}
Even numbers from the said list: {even_nums}
Odd numbers from the said list: {odd_nums}
''')
## <p style="color:green;">Q.15 Write a Python program to triple all numbers of a given list of integers. Use Python map.</p>

# Answer here 
list8 = [1,2,3,4,5,6,7]

def triple_of_num(arg):
    return arg * 3
# Answer here 

# Answer here 
list8 = [1,2,3,4,5,6,7]

Triple_nums = list(map(triple_of_num,list8))


print(f'Your list = {list8}\nYour Triple numbers = {Triple_nums}')
## <p style="color:orange;">Q.16 Write a Python program to add three given lists using Python map and lambda.

# </p>

# Answer here 
list1 = [1,2,3]
list2 = [2,3,4]
list3 = [3,4,5]

list(map(lambda x,y,z: x+y+z ,list1,list2,list3))
## <p style="color:orange;">Q.17 Write a Python program to square the elements of a list using map() function.</p>

# Answer here 
list9 = [1,2,3,4,5,6,7]

def power_of_num(arg):
    return arg**2

# Answer here 
list9 = [1,2,3,4,5,6,7]

list9_power = list(map(power_of_num,list9))


print(f'Your list = {list9}\nAfter useng power on the list numbers = {list9_power}')
## <p style="color:green;">Q.18 Using filter() function filter the list so that only negative numbers are left.</p>
# > lst1  [12,-1,9,8,-.5,-.2,-100]

# Answer here 
lst1 = [12,-1,9,8,-.5,-.2,-100]

def return_negative_nums(arg):
    if arg < 0:
        return True
# Answer here

negative_nums_list1 = list(filter(return_negative_nums,lst1))

print(f'Your list = {lst1}\nThe odd numbers = {negative_nums_list1}')
## <p style="color:green;">Q.19 Using filter function, filter the even numbers so that only odd numbers are passed to the new list.</p>
# > lst1  [22,100,19,13,11,1,4,66]

# Answer here
lst1 = [22,100,19,13,11,1,4,66]

def return_odd_nums(arg):
    if arg % 2 == 1:
        return True
# Answer here

odd_list1 = list(filter(return_odd_nums,lst1))

print(f'Your list = {lst1}\nThe odd numbers = {odd_list1}')
## <p style="color:green;">Q.20 Using map() and filter() functions add 2000 to the values below 8000.</p>
# > lst [1000,500,600,700,5000,90000,17500]
# Answer here Part 1 :
lst = [1000,500,600,700,5000,90000,17500]

def filter_below_8000(arg):
    if arg <= 8000:
        return True
    else:
        return False
    
def add_2000(arg):
    return arg + 2000
# Answer here Part 2 :)

lst_below_8000 = list(filter(filter_below_8000,lst))
final_1st = list(map(add_2000,lst_below_8000))

print(f'''Your list = {lst}
The numbers below 8000 = {lst_below_8000}
The numbers after adding 2000 = {final_1st}''')
# <center> Thank's for your effort ❤️ </center> 