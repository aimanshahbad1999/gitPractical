def add(a,b):
     c=a+b
     if c>0:
        print("Addition of two number: "+str(c))
     else:
        print("Addition of two number: "+str(abs(c)))
         
        

def substract(a,b):
     c=a-b
     print("Substraction of two number: "+str(c))


def multiply(a,b):
     c=a*b
     print("Multiplication of two : "+str(c))




no1=int(intput())
no2=int(input())

add(no1,no2)
substract(no1,no2)
multiply(no1,no2)
