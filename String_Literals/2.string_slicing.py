name = "HarryIsGood"
Greeting = "Goodmorning "
# print(Greeting + name)


# ***************Slicing a string************

# print(name[6])

# name[3] = "g"  # Does not work because string object does not support item assignment. 
# print(name)
# print(name[0:3])
# 
# print(len(name))

# Why negative index is used --> reason is because sometimes we dont know the length of string
# in such case if we wwnt to access last element then we use negative index.

# print(name[:4])  # is same as name[0:4]
# print(name[0:])  # is same as name[0:4]


# ''''Slicing with Skip value      -----[start : end : skipvalue]'''

d = name[0::3]
print(d)














