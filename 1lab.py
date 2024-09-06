def code_ham(message):
    bin_message = ""
    list_ctrl=[] #список сумм контрольных битов

    for s in message: # перевод в бинарный
        bin_message += format(ord(s), '08b')
    bin_message="0100010000111101"
    print(bin_message)
    
    count_ctrl = 0 #количество контрольных битов
    for i in range(len(bin_message)): #подсчет количества контрольных битов
        if (i & (i - 1)) == 0:
            count_ctrl += 1

    for i in range(count_ctrl): #добавление 0 на места контрольных битов
        bin_message = bin_message[:2**i-1] + '0' + bin_message[2**i-1:]
    print(bin_message)

    for i in range(count_ctrl): #подсчет сумм контрольных битов
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
        list_ctrl.append(ctrl)

    for i in range(count_ctrl): #замена контрольных битов на новые значения
        bin_message = bin_message[:2**i-1] + str(list_ctrl[i]%2) + bin_message[2**i:]

    print(bin_message)

code_ham("he")