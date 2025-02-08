def disp(a,b):
    try:
        print('Task Started')
        print(a/b)
       
    except:
        print('Some error Handled')
    else:
        print('Task Executed without any execption')
    finally:
        print('Task Ended')
disp(10,0)
disp(10,5)
disp(20,2)

'''
try: Used to keep the logic in which we may
get some error.

except: Will be executed when execption occurres
in try block logic

else: Will be executed when try block logic executed
without any error.

Finally: Will always executed irrespective of
execption occurred or not.
'''