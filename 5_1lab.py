from operator import xor

def get_random_number(last_value):
  squared = pow(last_value, 2)
  value = int(str(squared).zfill(8)[2:6])
  return value

def crypt(char, last_value):
  last_value = get_random_number(last_value) 
  return chr(xor(ord(char), last_value % 256)), last_value

def generate_numbers(key, length):
  numbers = []
  last_value = key
  for _ in range(length):
    last_value = get_random_number(last_value)
    numbers.append(last_value % 256)
  return numbers

def decrypt(text, key):
  numbers = generate_numbers(key, len(text))
  cryptedList = []
  for t, s in zip(text, numbers):
    cryptedList.append(chr(xor(ord(t), s)))
  newText = ''.join(cryptedList)
  return newText

text = ""
print("Введите текст посимвольно. В конце введите ! для завершения ввода")
secret_key = 1234
last_value = secret_key

while True:
  char = input()
  if char == "!":
    break
  crypted_char, last_value = crypt(char, last_value) 
  print("Зашифрованный символ:", crypted_char)
  text += crypted_char

print("Зашифрованный текст:", text)
decryptedText = decrypt(text, secret_key)
print("Расшифрованный текст:", decryptedText)