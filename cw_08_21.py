# Python: Loops Classwork

### Exercise 1:
Print -20 to and including 50. Use any loop you want.
for indx in range (-20,51):
    print (indx)


#
# ### Exercise 2:
# Create a loop that prints even numbers from 0 to and including 20.
# Hint: You can find multiples of 2 with (whatever_number % 2 == 0)
#

for i in range (0,21,2):
    print(i)
#


# ### Exercise 3:
# Prompt the user for 3 numbers. Then print the 3 numbers along with their average after the 3rd number is entered.
# Refer to example below replacing ```NUMBER1```, ```NUMBER2```, ```NUMBER3```, and ```THEAVERAGE``` with the actual values.
#
# Ex.Output
# ```
# The average of NUMBER1, NUMBER2, and NUMBER3 is THEAVERAGE
# ```

#
NUMBER1 = int(input("Enter first number: "))
NUMBER2 = int(input("Enter second number: "))
NUMBER3 = int(input("Enter third number: "))

THEAVERAGE= (NUMBER1+NUMBER2+NUMBER3)/3
str(NUMBER1)
str(NUMBER2)
str(NUMBER3)
str(THEAVERAGE)
print ("The average of", NUMBER1, NUMBER2, "and", NUMBER3 ,"is" ,THEAVERAGE)



# ### Exercise 4:
# Use any loop to print all numbers between 0 and 100 that are divisible by 4.
for x in range(0,100):
    if x % 4==0:
        print(x)


#
# ### Challenge:
# Password Checker - Ask the user to enter a password. Ask them to confirm the password.
# If it's not equal, keep asking until it's correct or they enter 'Q' to quit.

password= input ("Enter a password ")
passCheck= input ("What is the password? ")
while passCheck != 'q':
    if passCheck == password:
        print("Good Job!")
        passCheck= input("Enter q to Quit or Try again Enter the password: ")
