# s1 = 'kodnest'
# s1 .upper()
# print(s1)

# Strings are Immutable
1. # once we declare the string we cannot modify it, if wetry to modify the string it will create new string
2. # If new 
3. # Python internally uses String interning
4. # String internung is the process os checking string intern pool before creating any new object.

#Whenever we want to  create new object. python first will check string intern pool, weather that object already exist or not.

#when object already exist in the string intern records then address of existing object will be reused.

# s1 = 'K'
# print(s1, id(s1))

s1 = 'Hello'
s2 = 'World'
print(s1, id(s1))
print(s2, id(s2))

print('ID of H:',id(s1[0]))
print('ID of O:',id(s2[0]))

print('s2 ID of W:',id(s2[1]))
print('s2 ID of O:',id(s1[-1]))

print('s1 ID of l:',id(s1[1]))
print('s1 ID of l:',id(s1[2]))
print('s1 ID of l:',id(s2[3]))