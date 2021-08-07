with open('F:\Python 12hr course\Chapter-10 File_operations\sample.txt','r') as f:
    a = f.read()
print(a)

with open('F:\Python 12hr course\Chapter-10 File_operations\sample.txt','w') as f2:
    f2.write("This line is written by using with keyword.")