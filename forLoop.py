'''for control_variable in iterable_object'''
for i in 'Kodnest':
    print(i)

for j in [10,20,30]:
    print(j+5)

for num in range(1,11):
    print(num)    

for num in range(11,21,2):
    print(num, end=" ")   

#WAP to print all even numbers from 1-10
for num in range(1,10):
    if(num%2==0):
      print(num) 

i = 0
while(i<10):
    print(i+100)
    i = i+1

#WAP to print numbers from 1-10 but if number is 6 then skip printing.   
for i in range(1,11):
    if(i==6):
        continue
    print(i)

#WAP to print numbers from 1-10 but if number is 6 then skip printing.   
for i in range(1,11):
    if(i==5):
        break
    print(i)
