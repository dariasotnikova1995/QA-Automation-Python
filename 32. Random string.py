import random
def get_random_string(length: int) -> str:
    random_string = ""
    for _ in range(length):
        random_ascii = random.randint(48, 122)
        while not (48 <= random_ascii <= 57 or 65 <= random_ascii <= 90 or 97 <= random_ascii <= 122):
            random_ascii = random.randint(48, 122)
        random_string += chr(random_ascii)
    return random_string
print(get_random_string(10))