#Assignment 2

#Q1
org_string= "Python is a case sensitive language"
# Find length
print(len(org_string))
# Reverse the order
print(org_string[::-1])
# Storing "a case sensitve " in new string using slicing
new_string= org_string[10:26]
# Replacing string
org_string= org_string.replace("a case sensitive", "object oriented")
#Finding the index of "a"
print(org_string.find("a"))
#Removing the white spaces
org_string = org_string.replace("","")


#Q2
SID = 21107017
name = "Adesh Pal Singh Chhina "
department = "Mechanical "
CGPA = 8.5

print("Hey," + name + "Here! ")
print("My SID is %d" %SID)
print("I am from " +department+ "department and my CGPA is",CGPA)

#Q3
a = 56
b = 10
print("a&b = ", a&b)
print("a|b ", a|b)
print("a^b = ", a^b)
print("a << 2 : ", a << 2, " and b << 2: ", b << 2)
print("a >> 2 : ", a >> 2, " and b >> 4: ", b >> 4)

#Q4
input_string = input("Enter the string: ")
check_name = input_string.find("name")
if(check_name == -1):
    print("NO")
else:
    print("YES")    

#Q5
side_1 = int(input("Enter side 1: "))
side_2 = int(input("Enter side 2: "))
side_3 = int(input("Enter side 3: "))

a = side_1 + side_2
b = side_2 + side_3
c = side_3 + side_1

x = (side_1 < b)
y = (side_2 < c)
z = (side_3 < a)

answer =str( x & y & z)
answer = answer.replace("True","yes")
answer = answer.replace("False","no")
print(answer)

#Q6
a = 10
b = 30

c = (a^b)
d = bin(c)

count = 0
for i in d[2:]:
    if i == "1":
         count += 1

print(count)