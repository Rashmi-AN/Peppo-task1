from hmac import compare_digest
from user import User

users = [
    User(1,'rashmi','rashmi123')
]

username_mapping = {u.username:u for u in users}
uid_mapping = {u.id:u for u in users}

def auth(username,password):
    user = username_mapping.get(username,None)
    if user and compare_digest(user.password,password):
        return user

def identity(payload):
    user_id = payload['identity']
    return uid_mapping.get(user_id,None)
