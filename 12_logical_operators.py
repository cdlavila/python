"""
Logical operators
  and - and
  or - or
  not - not
"""
print('\nLogical operators')
username = 'Carlos10'
password = '123456'
is_deactivated = False
print(username == 'Carlos10' and password == '54321')  # false
print(username == 'Carlos10' or password == '54321')  # true
print(username == 'Carlos10' and not is_deactivated)  # true