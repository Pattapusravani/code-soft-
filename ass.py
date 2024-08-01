def add(a,b):
    ad=int(a)+int(b)
    print("addition is",ad)
def sub(a,b):
    s=a-b
    print("subtraction is ",s)
def multi(a,b):
    m=a*b
    print("multiplication is",m)
def div(a,b):
    d=a/b
    print("division is",d)
num1=int(input("enter first number"))
num2=int(input("enter second number"))
sel=int(input("enter 1-addition \n 2-subtraction\n3-multiplication\n 4-division"))
if(sel==1):
    add(num1,num2)
if(sel==2):
       sub(num1,num2)

if(sel==3):

       multi(num1,num2)
    
if(sel==4):
        div(num1,num2)
 else:
    
    
    print(" enter correct operation")
