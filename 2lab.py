import random
import math

def generate_array(max_value): #заполнение массива простыми числами
    arr = []
    for i in range(2, max_value):
        is_simple = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_simple = False
                break
        if is_simple: 
            arr.append(i)
    return arr

def generate_keys(p, q): #генерация открытого и закрытого ключа
    n = p * q #модуль
    f = (p - 1)*(q - 1)
    print('f:', f)
    e = random.randrange(1, f)
    while (math.gcd(e, f) != 1):
        e = random.randrange(1, f)
    print('e:', e)
    d = pow(e, -1, f)
    print('d:', d)
    print('n:', n)
    return (e, n), (d, n)

def code_RSA(public_key, message):
    e, n = public_key
    m = []
    for c in message:
        m.append(pow(ord(c), e) % n)
    return m

def decode_RSA(private_key, m):
    d, n = private_key
    message = ""
    for c in m:
        message += chr((pow(c, d)) % n)
    return message

arr = generate_array(200)
p = random.choice(arr)
q = random.choice(arr)
while p == q:
    q = random.choice(arr)
print('p:', p)
print('q:', q)
public_key, private_key = generate_keys(p, q)
message_in = "Hello, world!"
print("message_in: ", message_in)
m = code_RSA(public_key, message_in)
print("crypted_message: ", m)
message_out = decode_RSA(private_key, m)
print("message_out: ", message_out)

