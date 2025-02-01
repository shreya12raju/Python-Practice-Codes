#li = input('Enter Space Seperated Element')
#print(li, type(li)) #'10 20' <class 'str'>
#li = li.split()
#print(li) #['10', '20']
#li = list(map(int,li))
#print(li) #[10, 20]


#tup = tuple(map(int,input('Enter Space Seperated Elements ').split()))
#print(tup)

li = list(map(int,input().split()))
print([i for i in li if i%2 == 0])