# user_database = {101: 'admin_user', 102: 'dev_guy', 103: 'guest_99'}
# def id(idname):
#     return idname
# def name(user):
#     return user
# swapped={name(value):id(key) for (key,value) in user_database.items()}
# print(swapped)
user_database = {101: 'admin_user', 102: 'dev_guy', 103: 'guest_99'} 
swapped={value:key for (key,value) in user_database.items()}
print(swapped)