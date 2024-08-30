# Dear Epsilon Students, 
# The More you practice The better You'll Be.
## <p style="color:yellow;">Answers By Ibrahim Saber
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
## <p style="color:orange;">Q.01 print out words that start with 's' in the following sentence.</p>
# Answer here 

st = 'Print only the words that start with s in this sentence'

my_st = st.split()

for word in my_st:
    if word.startswith("s"):
        print(word)

# Here I wanted to print the words on the same line just to use join :)..

st = 'Print only the words that start with s in this sentence'
my_st = st.split()

my_st1 = []
for word in my_st:
    if word.startswith("s"):
        my_st1.append(word)

final_st = ' '.join(my_st1)

print(final_st)

# Answer here 

st = 'Print only the words that start with s in this sentence'

st1 = [word for word in st.split() if word.startswith('s')]

print(st1)

## <p style="color:orange;">Q.02 create a list of all numbers between 1 and 50 that are divisible by 3.</p>
# Answer here 

list1 = []
for num in range(1,51):
    if num %3 == 0 :
        list1.append(num)

print(f'''list of all numbers between 1 and 50 that are divisible by 3 is :
       {list1}''')
list1 = [num for num in range(1, 51) if num % 3 == 0]

print(list1)
## <p style="color:green;">Q.03 Given X which is a password. Print "Wrong" if the password is incorrect otherwise, print "Correct".</p>
# > The "Correct" password is the number 1999.
# Answer here

x = int(input('pleas enter your password'))

if x == 1999:
    print('correct')

else:
    print('wronge')
## <p style="color:red;">Q.04 Given a number N Print the factorial of number N.</p>
# > For information about factorial: https://en.wikipedia.org/wiki/Factorial
# Answer here 

N = int(input("pleas enter a number"))

if N > 0:
    num = 1
for i in range(2, N + 1):
    num = num * i
print(num)

## <p style="color:orange;">Q.05 - Write a Python program to construct the following pattern.</p>

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# Answer here 

for x in range(1,6):
    print('* ' * x)
# Answer here , i was trying something :)..


for x in range(1,7):
    print('* ' * x)
    
for i in range(7, 0, -1):
    print('* ' * i)

## <p style="color:green;">Q.06 Timon has a number of candies and his friend, Pumbaa, has b number of candies candies, so Pumbaa asked Timon to tell him the value of a−b. However, Timon will tell him the value of a−b if the value is ≥0; otherwise, he will lie and say 0. Since it was a hard task for Timon, he's asking for your help.</p>

# Answer here 
a = int(input('pleas enter timon candies number'))
b = int(input('pleas enter pummaa candies number'))

if a-b >= 0 :
    print(a-b)
else:
    print("0")
## <p style="color:green;">Q.7 Given a list. Replace every positive number by 1, Replace every negative number by 2.</p>
# > [19, 20, 21, 10, -53, -23, 10]
# Answer here 

list1 = [19, 20, 21, 10, -53, -23, 10]

list2 = []
for x in list1:
    if x > 0:
        x = 1
        list2.append(x)
    else:
        x = 2
        list2.append(x)

print(list2)

## <p style="color:green;">Q.8 Write a Python program to convert temperatures to and from celsius, fahrenheit.</p>
# >[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Answer here : 
# 1. from celsius to fahrenheit...
c = float(input('pleas enter the degree in Celsius ')) 

f = c * (9/5)+32

print(f"{c} Celsius is equal to {f} Fahrenheit")

# 2. from fahrenheit to celsius...
f = float(input('pleas enter the degree in fahrenheit ')) 

c = (f - 32)*(5/9)

print(f"{f} Fahrenheit is equal to {c} Celsius")

## <p style="color:orange;">Q.9 Write a Python program to create the multiplication table (from 1 to 10) of a number.</p>
# Expected Output:

# Input a number: 6                                                       
# 6 x 1 = 6                                                               
# 6 x 2 = 12                                                              
# 6 x 3 = 18                                                              
# 6 x 4 = 24                                                              
# 6 x 5 = 30                                                              
# 6 x 6 = 36                                                              
# 6 x 7 = 42                                                              
# 6 x 8 = 48                                                              
# 6 x 9 = 54                                                              
# 6 x 10 = 60 
# Answer here 

n = int(input('pleas enter a number :'))

for i in range (1,11):
    print(f' {n} x {i} = {n*i}')
# <center> Thank's for your effort ❤️ </center> 