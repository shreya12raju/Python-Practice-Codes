def checkAge(age):
    if(age<18):
        raise ValueError('Age must be reater than 18')
try:
    checkAge(12)
except ValueError as e:
    print('Error Message:',e)