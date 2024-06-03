def call_counter(path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(path, 'a+') as file:
                file.seek(0)
                count = file.read().count(func.__name__) + 1
                file.write(f"Function '{func.__name__}' was called {count} times\n")
            return func(*args, **kwargs)
        return wrapper
    return decorator
@call_counter('data.txt')
def add(a, b):
    return a + b
print(add(4, 6))
print(add(3, 5))
