#5-10. Checking Usernames

current_users = ['mick', 'Admin', 'mImI', 'jacinta', 'jack']
new_users = ['MiMi', 'jasmine', 'sid', 'admin']
current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f'The username {user} is already taken!')
    else:
        print(f'The username {user} is available')
