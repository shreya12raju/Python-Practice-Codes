#Without input and without return statement
def add():
    a = 10
    b = 20
    print('Addition is:',a+b)
add()  

#with input and without return statement
def sub(a,b):
    print('Subtraction is:',a-b)

#without input and with return statement:
def mul():
    return 10*20

#with input and with return statement
def div(a,b):
    return a/b

add()
sub(100,50)
print(mul())
print(div(200,10))
