#String formatting operations
person = {'name': 'damilola', 'age': 24}


# sentence = 'my name is' +  person['name'] + 'and i am' + person['age'] + 'yrs old.'
# print(sentence)


# sentence = 'my name is {} and i am {} years old.'.format(person['name'], person['age'])
# print(sentence)


# sentence = 'my name is {0} and i am {1} years old.'.format(person['name'], person['age'])
# print(sentence)


# tag = 'hi'
# text = 'this is the headline'
# sentence = '<{0}><{1}</{0}>'.format(tag, text)
# print(sentence)


# sentence = 'my name is {0[name]} and i am {1[age]} years old.'.format(person, person)
# sentence = 'my name is {0[name]} and i am {0[age]} years old.'.format(person)
# print(sentence)
#
#
# l = ['afodamz', 24]
# response = 'my nickname is {0[0]} and i am {0[1]}yrs old'.format(l)
# print(response)



# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# ps1 = Person('oluwadamilola', 24)
#
# sentence = 'my name is {0.name} and i am {0.age}yrs old'.format(ps1)
# print(sentence)



# sentence = 'My name is {name} and i am {age}yrs old.'.format(name='dami', age=24)
# print(sentence)



# sentence = 'My name is {name} and i am {age}yrs old.'.format(**person)
# print(sentence)




# for i in range(1, 11):
#     sentence = 'values {}'.format(i)
#     print(sentence)



# for i in range(1, 11):
#     sentence = 'values {:.2}'.format(i)
#     sentence = 'values {:.3}'.format(i)
#     print(sentence)



# pi = 3.141539265
#
# sentence = 'Pi is equal to {:.2f}'.format(pi)
# print(sentence)



# sentence = '1 MB is equal to {:,} bytes'.format(1000**2) #  Comma separator
# sentence = '1 MB is equal to {:,.2f} bytes'.format(100000**2) #  Comma separator and decimal places
# print(sentence)



import datetime

my_date = datetime.datetime(2018, 12, 2, 2, 52, 45) # year month day time
# print(my_date)


# sentence = '{:%B %d, %Y}'.format(my_date)
# print(sentence)


sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)

