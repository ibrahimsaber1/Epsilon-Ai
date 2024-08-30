# > # Dear Epsilon Students, 
# > # The More you practice The better You'll Be.
# ### Instructions: 
# - Make sure that you understand this topics before you start.
# - If you found something hard to do, try and try then google it and finally ask someone. 
# - You can divide this work into daily tasks so that you do not feel pressure.
# - After you finish, go to model answer and rate yourself. 
# - If you find something ambiguous, Try to make a hypothesis to solve a problem. 
# ### Question classification: 
# - Green is level 1 
# - Orange is level 2 
# - Red is level 3 
# <center> Let's start 💪 </center> 
## <p style="color:green;">Q.01 Write a Python program to select a random element from a list. Use random.choice()</p>

# Answer here 
from random import choice

list_1 = list(range(100))

rand_num = choice(list_1)
rand_num
## <p style="color:green;">Q.02 Write a Python program to shuffle the elements of a given list. Use random.shuffle() </p>
# Answer here 
from random import shuffle

mylist = ["apple", "banana", "cherry","mango"]
shuffle(mylist)

print(mylist)
## <p style="color:orange;">Q.03 Write a Python program to print yesterday, today, tomorrow.</p>
# Answer here 
import datetime

today_date = datetime.date.today()

one_day_after = datetime.timedelta(days= 1)

one_day_before = datetime.timedelta(days=-1)

print(f"""Today Date = {today_date}\nYesterday Date = {today_date + one_day_before}
Tomorrow Date = {today_date + one_day_after}""")
# today_date = datetime.date.today()

# today_year = today_date.year
# today_month = today_date.month
# today_day = today_date.day

# print(f'{today_year} / {today_month} / {today_day}')
# bday = datetime.date(2000,7,15)

# till_days = today_date - bday

# print(till_days.total_seconds())
# dd = datetime.datetime.today()

# dd
## <p style="color:red;">Q.04 Write a Python program to print next 5 days starting from today. </p>
# Answer here 

import datetime

today_date = datetime.date.today()

one_day_after = datetime.timedelta(days= 1)

for i in range(1,6):
    one_day_after = datetime.timedelta(days= i)

    print(today_date + one_day_after)
## <p style="color:green;">Q.05 Write a Python program to get current time in milliseconds in Python.</p>
# Answer here 
dt = datetime.datetime.today()



print(f"""Teh currant time = {dt.hour}:{dt.minute}:{dt.second}  And {dt.microsecond} Milliseconds.""")
## <p style="color:green;">Q.06 Write a Python program to get the name of current working directory.</p>

# Answer here 
import os

print(os.getcwd())
# <center> Thank's for your effort ❤️ </center> 