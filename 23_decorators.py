def message_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@message_decorator
def say_hello():
    print("Hello, world!")

# We call the function
say_hello()
