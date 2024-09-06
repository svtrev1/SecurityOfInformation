def code_ham(message):
    bin_message = ""
    list_ctrl=[] #список контрольных битов

    for s in message: #перевод в бинарный
        bin_message += format(ord(s), '08b')
    
    count_ctrl = 0 
    for i in range(len(bin_message)): #подсчет количества контрольных битов
        if (i & (i - 1)) == 0:
            count_ctrl += 1

    for i in range(count_ctrl): #добавление 0 на места контрольных битов
        bin_message = bin_message[:2**i-1] + '0' + bin_message[2**i-1:]

    for i in range(count_ctrl): #подсчет контрольных битов
        start_position = 2**i - 1
        step = 2**i
        ctrl = 0
        pause = False
        while 1:
            for i in range(step): 
                position = start_position + i    
                if (position >= len(bin_message)):
                    pause = True
                    break
                else:
                    ctrl += int(bin_message[position])
            start_position = position + 1 + step
            if (pause):
                break
        list_ctrl.append(ctrl%2)

    for i in range(count_ctrl): #замена контрольных битов на новые значения
        bin_message = bin_message[:2**i-1] + str(list_ctrl[i]) + bin_message[2**i:]

    return bin_message

def decode_ham(message):
    bin_message = message
    

    # добавление ошибки вручную
    print(message, "правильное сообщение")
    bin_message = bin_message[:6] + "1" + bin_message[7:]
    print(bin_message, "ошибочное сообщение")


    message_list_ctrl = []

    count_ctrl = 0 
    for i in range(len(bin_message)): #подсчет количества контрольных битов
        if (i & (i - 1)) == 0 and i !=0: 
            count_ctrl += 1

    for i in range(count_ctrl): #подсчет контрольных битов для изначального сообщения
        message_list_ctrl.append(int(message[2**i-1]))

    for i in range(count_ctrl): #замена контрольных битов на 0
        bin_message = bin_message[:2**i-1] + str(0) + bin_message[2**i:]

    list_ctrl=[] 
    for i in range(count_ctrl): #подсчет контрольных битов
        start_position = 2**i - 1
        step = 2**i
        ctrl = 0
        pause = False
        while 1:
            for i in range(step): 
                position = start_position + i    
                if (position >= len(bin_message)):
                    pause = True
                    break
                else:
                    ctrl += int(bin_message[position])
            start_position = position + 1 + step
            if (pause):
                break
        list_ctrl.append(ctrl%2)

    for i in range(count_ctrl): #замена контрольных битов на новые значения
        bin_message = bin_message[:2**i-1] + str(list_ctrl[i]) + bin_message[2**i:]

    error_position = 0
    if (bin_message != message): # проверка на ошибку и ее исправление
        for i in range(count_ctrl):
            if message_list_ctrl[i] != list_ctrl[i]:
                error_position += 2**i
        print("Ошибка в позиции: ", error_position)
        bin_message = bin_message[:error_position - 1] + str(1 - int(bin_message[error_position - 1])) + bin_message[error_position:]
    else:
        print("Ошибок не обнаружено!")

    for i in range(count_ctrl, -1, -1): # удаление контрольных битов
        bin_message = bin_message[:2**i-1] + bin_message[2**i:]

    new_message = ""
    for i in range(0, len(bin_message), 8): # декодируем сообщение
        byte = bin_message[i:i+8] #вырезаем байт
        char = chr(int(byte,2)) #байт в десятичное по аски, затем в символ
        new_message += char

    print("Полученное сообщение: ", new_message)

message = "hello"
print("Изначальное сообщение: ", message)
bin_message = code_ham(message)
decode_ham(bin_message)

