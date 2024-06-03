def is_valid_email(email):
    if '@' not in email or '.' not in email or email.index('@') > email.index('.'):
        return False
    if email.startswith('@') or email.endswith('.'):
        return False
    at_count = email.count('@')
    dot_count = email.count('.')
    if at_count != 1 or dot_count != 1:
        return False
    valid_symbols = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    for char in email:
        if char != '@' and char != '.' and char not in valid_symbols:
            return False
    return True
emails = [
    "aaa@bbb.ccc",
    "@aaa.bbbccc",
    ".aaa@bbb",
    "bbb@ccc.aaa",
    "abc@ccc.aaa.",
    "abc@@ccc.aaa"
]
for email1 in emails:
    print(is_valid_email(email1))