#TASK 1
def is_valid_part(part):
    try:
        i_part = int(part)
        # part.startswith('0') NEW SYNTAX !!! PARTY BRACKETS {{}}{{}}{{}}{{}}{{}}
        if part[0] == '0' and not i_part == 0: return False
        return 0 <= i_part < 256
    except ValueError as ve: return False


#print(
    #is_valid_part('AAA'),
    #is_valid_part('257'),
   # is_valid_part('-255'),
   # is_valid_part('01') ,
   # is_valid_part('0'))

#TASK 2
def is_valid_ip(ip:str):
    parts = ip.split('.')
    if len(parts) != 4: return False
    for part in parts:
         if not is_valid_part(part): return False
    return True

(
print(is_valid_ip("192.168.1.1")),
print(is_valid_ip("192.168.256.1")),
print(is_valid_ip("192.168.1")) ,
print(is_valid_ip("192.168.01.1")),
# print(is_valid_ip("0.0.0.0")),
# print(is_valid_ip("255.255.255.255")),
# print(is_valid_ip("192.168.1.01"))
)


