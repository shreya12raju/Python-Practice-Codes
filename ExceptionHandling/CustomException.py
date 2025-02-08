class PinError(Exception):
    pass
correctPin = 1221
pin = int(input('Enter 4 digit PIN'))
try:
    if(pin == correctPin):
        print('Account Unblocked')
    else:
        raise PinError('Enter Pin is',pin)
except PinError as e:
    print('Incorrect pin: ',e)
          