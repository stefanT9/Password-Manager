import sys
args = sys.argv

master_password = args[1]
operation =  args[2]

def encrypt(text, key):
    return text
    key = bytes(key.encode('utf-8'))
    
    aes = AES.new(key,AES.mode_ecb)
    return aes.encrypt(text)
    
def decrypt(text, key):
    return text
    key = bytes(key.encode('utf-8'))
    
    aes = AES.new(key,AES.mode_ecb)
    return aes.decrypt(text)
    
def init_command(master_password):
    f = open('passwords.txt','a+')
    print(f)
    f.close()
    return

def list_command(master_password):
    f = open('passwords.txt')
    lines = f.readlines()
    lines = [eval(line) for line in lines]
    lines = [(line[0],line[1], decrypt(line[2],master_password)) for line in lines]
    for line in lines:
        print(line)

def get_command(master_password, website):
    f = open('passwords.txt')
    lines = f.readlines()
    lines = [eval(line) for line in lines]
    lines = [(line[0],line[1], decrypt(line[2],master_password)) for line in lines]
    lines = lines[:-2]
    for line in lines:
        if(line[0]==website):
            print(line)

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