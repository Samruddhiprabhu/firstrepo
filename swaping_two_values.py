'''#swapping by using third variable 
x=int(input('enter the value of x:'))

y=int(input('enter the value of y:'))
print("before sorting value of a n b =",x,' ',y)
temp=x
x=y
y=temp
print("after sorting value of a n b =",x,' ',y)'''


#swapping without using third variable
x=int(input('enter the value of x:'))

y=int(input('enter the value of y:'))
print("before sorting value of a n b =",x,' ',y)
x,y=y,x
print("after sorting value of a n b =",x,' ',y)