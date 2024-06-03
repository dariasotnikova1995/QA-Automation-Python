import re
def validate_email(email):
    pattern = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
email = [
    "aaa@bbb.ccc",
    "a+a@a.aa",
    "aa.a@a.aa"
]
for emails in email:
    print(validate_email(emails))