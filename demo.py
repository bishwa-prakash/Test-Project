def add_numbers(a, b):
    # Missing docstring (AI should catch this)
    result = a + b
    return result

def greet_user(name):
    print("Hello " + name)  # Could be improved with f-string

def unused_function():
    x = 10   # Unused variable (AI should flag this)
    y = 20  # Unused variable
    return

if __name__ == "__main__":
    num1 = 10
    num2 = 10
    total = add_numbers(num1, num2)
    print("Sum is:", total)
    
    greet_user("Bishwa")