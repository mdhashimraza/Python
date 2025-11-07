def decorator_function(original_function):
    def wrapper_function():
        print("Before function excution")
        original_function()
        print("After function excution")
    return wrapper_function

@decorator_function
def greet():
    print("Hello, World!")
greet()

