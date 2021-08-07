# f = open('F:\Python 12hr course\Chapter-10 File_operations\sample.txt', 'r')
# data = f.read()
# print(data)
# f.close()

# to open file and append some text open it in append mode

f1 = open('F:\Python 12hr course\Chapter-10 File_operations\sample.txt', 'a')
f1.write('I have appended this from visual studion using python code. ')
# data = f1.read()  # This line will not work because the file is opened in append mode.
# print(data)
f1.close()
