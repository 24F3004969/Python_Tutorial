def double(func):  
    def wrapper():  
       return func()
    return wrapper    
@double
def f1():  
    print("Hello There")  
print(f1())