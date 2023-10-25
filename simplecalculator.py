#simple calculator
a=int(input('Enter the first number:'))
b=int(input("Enter the second number:"))
c=input("Enter the operator:")
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=="/":
    print(a/b)
else:
    print('Enter the correct operator!!!')