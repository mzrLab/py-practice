# string formating


myName = 'Ali'
# variable injection
print('hey my name is {}'.format(myName))

# word counting
print('Ali sawari Ali'.count(myName))

#  from:to character
print('Ok so lets see this'[0:10])

# from:to:skip character
print('Ok so lets see this'[0:10:2])

# reverser
print('this is another simple string'[::-1])

# uppercase and lowercase
print('want this to be upper?'.upper())
print('WANT THIS TO BE LOWER?'.lower())

# splitting, output will be a list
print('Hello world its a nice day huh?'.split(' '))

# encoding the string
print('Lets see this in encode'.encode('ansi'))