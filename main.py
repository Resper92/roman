import re


def check_passwor(password):
    check_pas = re.compile(r'[a-zA-Z0-9!@#$%^&*()_+={}\[\]|:;"\'<>,.?/-=`~]+$')
    if check_pas.match (password):
        print('valid')
    else:
        print('not valid')


with open('password.txt')as p:
    for i in p:
        print(check_passwor(i.strip()))
