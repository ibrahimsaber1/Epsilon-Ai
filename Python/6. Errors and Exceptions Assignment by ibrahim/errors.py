# > # Dear Epsilon Students, 
# > # The More you practice The better You'll Be.
# ## <p style="color:yellow;">By Ibrahim Saber</p>
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
## <p style="color:green;">Q.01 Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks.</p>

# Answer here 
for i in ['a','b','c']:
    print(i**2)
# Answer here 
try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("You can\'t use power on a string, please use a list of numeric values instead")
## <p style="color:green;">Q.02 Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks. Then use a <code>finally</code> block to print 'All Done.'</p>
# Answer here 
x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("can\'t divide a number over zero")
finally:
    print("all done")
## <p style="color:green;">Q.03 Write a function that asks for an integer and prints the square of it. Use a <code>while</code> loop with a <code>try</code>, <code>except</code>, <code>else</code> block to account for incorrect inputs.</p>
# Answer here 
def ask():
    pass
# <center> Thank's for your effort ❤️ </center> 