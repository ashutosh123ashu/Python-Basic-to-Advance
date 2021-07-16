# write a program to create a dictionary of Hindi words with values  as their english translation 
# Provide user with an option to look it up


# myDict = {
#     "Pankha":"Fan",
#     "Dabba":"Box",
#     "Vastu":"Item"
# }

# print()
#****************************************************Important for interview************************
# write a program with "20" as int flloat and string and find its length.

# test = {20, 20.0, "20"}

# print(len(test))

# create a empty dictionary allow 4 friends to enter their favourite languahe as values and use keys
# as their names. Assume that the names are unique.



a = input("Enter your favourite language Raju\n")
b = input("Enter your favourite language Milan\n")
c = input("Enter your favourite language Ashutosh\n")
d = input("Enter your favourite language Sonali\n")

# s = {
#     "Raju":a,
#     "Milan":b,
#     "Ashutosh":c,
#     "Sonali":d
# }

s = {}
s['Raju']=a
s['Milan']=b
s['Ashutosh']=c
s['Sonali']=d

print(s)

#********************* Important******************

# We can not define a list inside a set. Because set is hashable and list is not hashable.
# Only hashable things can come inside set.
















