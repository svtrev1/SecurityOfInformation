from operator import xor

def get_random_number(last_value):
  squared = pow(last_value, 2)
  l1 = str(squared).zfill(8)
  l2 = l1[2:6]
  l3 = int(l2)
  value = int(str(squared).zfill(8)[2:6]) 
  return value 

def generate_random_numbers(key, length):
  numbers= []
  last_value = key
  for i in range(length):
    last_value = get_random_number(last_value)
    numbers.append(last_value % 256)
  print(numbers)
  return numbers

def crypt(text, key):
  numbers = generate_random_numbers(key, len(text))
  cryptedList = []
  for t, s in zip(text, numbers):
    cryptedList.append(chr(xor(ord(t), s)))
  newText = ''.join(cryptedList)
  return newText

def decrypt(text, key):
  numbers = generate_random_numbers(key, len(text))
  decryptedList = []
  for t, s in zip(text, numbers):
    decryptedList.append(chr(xor(ord(t), s)))
  newText = ''.join(decryptedList)
  return newText


secret_key = 7876
text = "Hello, world!"
cryptedText = crypt(text, secret_key)
print("Зашифрованный текст:", cryptedText)
decryptedText = decrypt(cryptedText, secret_key)
print("Расшифрованный текст:", decryptedText)