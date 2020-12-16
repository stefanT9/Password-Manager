import sys
from zlib import adler32

args = sys.argv

master_password = args[1]
operation =  args[2]
master_password = master_password.encode('utf-8')

def check_hash(master_password):
    f = open('passwords.txt')
    lines = f.readlines()
    f.close()
    return lines[-1]==str(adler32(bytes(master_password)))

def remove_hash():
    f = open('passwords.txt')
    lines = f.readlines()
    f.close()
    f = open('passwords.txt','w')
    lines = lines[:-1]
    f.writelines(lines)

def add_hash(master_password):
    f = open('passwords.txt','a')
    f.write(str(adler32(bytes(master_password))))
    f.close()

def encrypt(text, key):
    text = [ord(x) for x in text]
    key = [ord(x) for x in key]

    n = len(text)
    for i in range(n):
        text[i]=text[i]+key[i%len(key)]
        text[i]= chr(text[i])
    text = ''.join(text)
    return text
    
def decrypt(text, key):
    text = [ord(x) for x in text]
    key = [ord(x) for x in key]

    n = len(text)
    for i in range(n):
        text[i]-=key[i%len(key)]
        text[i]= chr(text[i])
    text = ''.join(text)
    return text

    return text
    
def init_command(master_password):
    f = open('passwords.txt','a+')
    f.write(str(adler32(bytes(master_password))))
    f.close()
    return

def list_command(master_password):
    f = open('passwords.txt')
    lines = f.readlines()
    lines = [eval(line) for line in lines]
    lines = [(line[0],line[1], decrypt(line[2],master_password)) for line in lines]
    for line in lines:
        print(f' website: {line[0]}\n email: {line[1]}\n password: {line[2]}\n\n')

def get_command(master_password, website):
    f = open('passwords.txt')
    lines = f.readlines()
    lines = [eval(line) for line in lines]
    lines = [(line[0],line[1], decrypt(line[2],master_password)) for line in lines]
    for line in lines:
        if(line[0]==website):
            print(f' website: {line[0]}\n email: {line[1]}\n password: {line[2]}\n\n')

def add_command(master_password, website, email, password):
    f = open('passwords.txt', 'a+')
    line = (website,email,encrypt(password,master_password))
    f.write(str(line))
    f.write('\n')
    
def remove_command(master_password, website):
    f = open('passwords.txt')
    lines = f.readlines()
    lines = [eval(line) for line in lines]
    aux=[]
    for line in lines:
        if not line[0]==website:
            aux+=[line]
    f.close()
    f = open('passwords.txt','w')
    for line in aux:
        f.write(str(line))
        f.write('\n')
    f.close()

if   operation=='-init':
    init_command(master_password)
else:
    if(check_hash(master_password)):
        remove_hash()
        master_password = master_password.decode('utf-8')
        try:
            if operation=='-list':
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
        except:
            print('something went wrong')
        finally:
            master_password = master_password.encode('utf-8')
            add_hash(master_password)
    else:
        print('password is incorect')