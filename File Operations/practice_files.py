# Write a program to read the text from a given file 'poems.txt'
# and find out whether it contains the word 'king'

# with open('F:\Python 12hr course\Chapter-10 File_operations\poems.txt','r') as f:
#     a = f.read()

# if 'king' in a:
#     print("King is present")
# else:
#     print("king is not present")

#Que-2  You need to read a file 'Hiscore.txt' which is either blank or contains the previous Hi-score, You need
# to write a program to update the Hi-score whenever game breaks the Hi-score.

# def game():
#     return 384

# score = game()

# with open('F:\Python 12hr course\Chapter-10 File_operations\hiscore.txt','r') as f:
#     Hi_Score = f.read()

# if(Hi_Score == ''):
#     with open('F:\Python 12hr course\Chapter-10 File_operations\hiscore.txt','w') as f:
#         f.write(str(score))
# elif(int(Hi_Score)<score):
#     with open('F:\Python 12hr course\Chapter-10 File_operations\hiscore.txt','w') as f:
#         f.write(str(score))

#Que-3 Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13 year old.

# for i in range(1,21):
#     with open(f"F:\Python 12hr course\Tables\Table_{i}.txt",'w') as f:
#         for j in range(1,11):
#             f.write(f"{i} * {j} = {i*j}\n")
    
# Que-4  A file contains some bad words like "donkey" , replace these words with ######.

# with open('F:\Python 12hr course\Chapter-10 File_operations\comments.txt', 'r') as f:
#     a = f.read()

# if 'donkey' in a:
#     with open('F:\Python 12hr course\Chapter-10 File_operations\comments.txt','w') as f:
#        a = a.replace('donkey','#######')
#        f.write(a)

# Que-5 In the above question what if we have list of words to replace

# words = ["donkey","kaddu","chutiye"]

# with open('F:\Python 12hr course\Chapter-10 File_operations\comments.txt', 'r') as f:
#     a = f.read()

# for word in words:
#     a = a.replace(word,"##$@**@$##")

# with open('F:\Python 12hr course\Chapter-10 File_operations\comments.txt', 'w') as f:
#     f.write(a)

# Que-6 Write  a program to mine a log file and find whether it contains 'python'.

# with open('F:\Python 12hr course\Chapter-10 File_operations\log.txt','r') as f:
#     content = f.read()
#     # content = f.readline()

# if 'python' in content:
#     print("python is present")
# else:
#     print('python is not present')

# Que-7 Modify the above program and print the line number in which python is present.

with open('F:\Python 12hr course\Chapter-10 File_operations\log.txt','r') as f:
    content = True
    i = 0
    while content:
        i = i+1
        content = f.readline()
        if 'python' in content:
            print(f"python is present in line {i}")
 
        





    

