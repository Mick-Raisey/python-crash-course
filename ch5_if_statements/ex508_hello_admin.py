# 5-8. Hello Admin

users = ['mick', 'jack', 'admin', 'mimi', 'jacinta']

for user in users:
    if user == 'admin':
        print(f"Hello {user.title()}, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")
