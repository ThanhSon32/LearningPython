def myfunc():
    print('Hello World')

def myfunc2(name):
    print('Hello {}'.format(name))

def myfunc3(a):
    if a== True:
        return 'Hello'
    elif a == False:
        return 'Goodbye'

def myfunc(x,y,z):
    if z == True:
        return x
    else:
        return y

def myfunc(a,b):
    return a+b

def is_even(value):
  if value % 2 == 0:
    return True
  else:
    return False

def is_greater(a,b):
    if a>b:
        return True
    else:
        return False

def myfunc(*args):
    return sum(args)

def myfunc(*args):
    result = []
    for arg in args:
        if arg%2 == 0:
            result.append(arg)
    return result;

def myfunc(a):
    result = ''
    for letter in range(len(a)):
        if letter % 2 == 0:
            result+=a[letter].upper()
        else:
            result+=a[letter].lower()
    return result