#String - Any text
#Int - any integer
#float - decimal
#bool(boolean) - True or False
'''
Comparison opterators:
==  - is equal?
!= - is not equal?
< - is less than?
> - is greater than?
<= - is less than or equal to?
>= - is greater than or equal to?
'''
# x = 5
# y = 5
# if x != y:
#     print("The condition is right.")
#     print("yes")
#     print("This is true")
# else:
#     print("This is else")



# function to convert into int - int()
# function to convert into float - float()
# function to convert into str - str()




n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
operation = input("Enter operation plus/minus/multiply/divide : ")
if operation=="plus":
    print("Answer: ",n1+n2)
if operation=="minus":
    print("Answer: ",n1-n2)
if operation=="multiply":
    print("Answer: ",n1*n2)
if operation=="divide":
    print("Answer: ",n1//n2)
