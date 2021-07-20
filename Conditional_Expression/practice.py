# Que 1. Write a program to find greatest of four numbers. input from user
# num_1 = int(input("Enter number1: "))
# num_2 = int(input("Enter number2: "))
# num_3 = int(input("Enter number3: "))
# num_4 = int(input("Enter number4: "))


# if(num_1 > num_4):
#     f1 = num_1
# else:
#     f1 = num_4

# if(num_2 > num_3):
#     f2 = num_2
# else:
#     f2 = num_3

# if(f1>f2):
#     print(f1 , "is greatest number." )
# else:
#     print(f2 , "is greatest number.")

# Que 2. Write a program to find whether a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass. 
# Assume 3 subjects and taks marks as input from user.

# sub1 = int(input("Enter subject 1 marks: "))
# sub2 = int(input("Enter subject 2 marks: "))
# sub3 = int(input("Enter subject 3 marks: "))

# if(sub1<33 or sub2<33 or sub3<33):
#     print("You are fail, since your marks is less than 33% in one or more subject.")
# elif(sub1 + sub2 + sub3)/3 <40:
#     print("Sorry you have failed your total is less than 40%.")
# else:
#     print("Congratulations! You have passed the exam.")

#***********Important**********************

# WAP to filter out spam comments. A comment is defined as spam if it caontains the following words.
#  make a lot of money,  subscribe this,   click this,  buy now..

# comment = input("Enter the comment:  ")



# spam = False
# if("make a lot of money" in comment):
#     spam = True
# elif("buy now" in comment):
#     spam = True
# elif("subscribe now" in comment):
#     spam = True
# elif("click this" in comment):
#     spam = True
# elif("click to earn" in comment):
#     spam = True
# else:
#     spam = False


# if(spam is True):
#     print("It is a spam comment.")
# else:
#     print("Not a spam")


# Que 4. WAP to find whether a name is present ina list or not

list = ["ashu", "rohan","aditi","rahul","shristi"]

name = input("Enter your name: ")

if(name in list):
    print("You name is present in the list.")
else:
    print ("Youer name is not present in the list.")











