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
         

no1=int(input("Enter Value of a: "))
no2=int(input("Enter Value of b: "))

add(no1,no2)
substract(no1,no2)