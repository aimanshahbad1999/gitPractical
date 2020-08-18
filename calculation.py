def add(a,b):
     c=a+b
     if c>0:
        print("Addition of two number: "+str(c))
     else:
        print("Addition of two number: "+str(abs(c)))

        

def substract(a,b):
     c=a-b
     if c>0:
        print("Substraction of two number: "+str(c))
     else:
        print("Substraction of two number: "+str(abs(c)))
        
        

def multiply(a,b):
     c=a*b
     if c>0:
        print("Multiplication of two number: "+str(c))
     else:
        print("Multiplication of two number: "+str(abs(c)))
        

def dev(a,b):
     c=a/b
     if c>0:
        print("Division of two number:"+str(c))
     else:
        print("Division of two number:"+str(abs(c)))
        





no1=int(input())
no2=int(input())

add(no1,no2)
substract(no1,no2)
multiply(no1,no2)
dev(no1,no2)
