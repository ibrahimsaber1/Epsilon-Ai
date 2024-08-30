# > # Dear Epsilon Students, 
# > # The More you practice The better You'll Be.
# > # <p style="color:yellow;">By : Ibrahim Saber</p>
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
## <p style="color:green;">Q.01 Open a file, name it 'test.txt' and write 'hello world' for 5 times in it then close it.</p>
# Answer here 

letter = "hello world\n"*5

fd = open("F:/EPSILON AI/files/text.txt",mode = "w")
fd.write(letter)

fd = open("F:/EPSILON AI/files/text.txt",mode = "r")
fd.read()

fd.close()
## <p style="color:orange;">Q.02 Read the contents of the file, then make content in upercase then write the result again to the file.</p>

# Answer here 
fd = open("F:/EPSILON AI/files/text.txt",mode = "r")
fd.read()
#fd.close()

# Answer here 
fd = open("F:/EPSILON AI/files/text.txt",mode = "w")
letter = letter.upper()
fd.write(letter)
fd.close()


## <p style="color:red;">Q.03 Read the third line of the file then update it to its capital case using `capitalize`.</p>

# Answer here part 1.
letter_new = letter.split("\n")
letter_new[2] = letter_new[2].capitalize()   #'Hello world'

letter_new = "\n".join(letter_new)
letter_new
# Answer here part 2.
fd = open("F:/EPSILON AI/files/text.txt",mode = "w")
fd.write(letter_new)
fd.close()

## <p style="color:green;">Q.04 Using With Statement open this file and append 'I Love python' to it.</p>

# Answer here 
with open("F:/EPSILON AI/files/text.txt",mode = "a") as fd :
    fd.write("I Love Python")
    
# <center> Thank's for your effort ❤️ </center> 