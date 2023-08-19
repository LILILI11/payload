
from hashlib import md5

username="admin"
admin_ip= "127.0.0.1"

CSRF_token= md5((username + admin_ip).encode()).hexdigest()

print(CSRF_token)