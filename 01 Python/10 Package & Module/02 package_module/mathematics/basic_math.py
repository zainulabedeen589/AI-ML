def add(a,b):
    """this is my basic add function"""
    return a+b

def subtract(a,b):
    return a-b

def divide(a,b):
    if b == 0 :
        raise ValueError("this is not possible change your b ")
    return a/b

def multi(a,b):
    return a*b


if __name__ == "__main__":
    print("this is a print from basic math ")
    print(add(5,676))
    print(multi(56,67))