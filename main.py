import sys
from cryptography.fernet import Fernet

args = sys.argv

master_password = args[1]
operation =  args[2]


def authenticate(password):
    return True

def encrypt(text, key):
    f = Fernet(key)
    return f.encrypt(text)
    
def decrypt(text, key):
    f = Fernet(key)
    return f.decrypt(text)

def init_command(master_password):
    f = open('passwords.txt','a+')
    print(f)
    f.close()
    return

def list_command(master_password):
    return []

def get_command(master_password, website):
    return ''

def add_command(master_password, website, email, password):
    return

def remove_command(master_password, website):
    return
if   operation=='-init':
    init_command(master_password)

elif operation=='-list':
    list_command(master_password)
elif operation=='-add':
    website  = args[3]
    username = args[4]
    password = args[5]
    add_command(master_password,website,username,password)

elif operation=='-get':
    website  = args[3]
    get_command(master_password, website)

elif operation=='-remove':
    website  = args[3]
    remove_command(master_password, website)