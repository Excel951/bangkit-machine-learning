from validations import validate_user

# validate_user('', -1)
print(validate_user('',1))
print(validate_user('myuser',1))
print(validate_user(88,1))
print(validate_user([],1))
print(validate_user(['name'],1))
