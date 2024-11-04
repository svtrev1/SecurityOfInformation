import os
from PIL import Image

def bit1(image, bin_message):
    pixels = image.load()
    i = 0
    message_length = len(bin_message) 

    for y in range(image.height):
        if i >= message_length:
            break
        for x in range(image.width):
            if i >= message_length:
                break
            r, g, b = pixels[x, y]
            for channel in range(3):
                channel_value = r if channel == 0 else g if channel == 1 else b 
                if i < message_length:
                    bit = int(bin_message[i]) 
                    # print("before: ", channel_value)
                    channel_value = (channel_value & 0b11111110) | bit
                    # print("after", channel_value)
                    if (channel == 0):
                        r = channel_value
                    elif (channel == 1):
                        g = channel_value
                    else:
                        b = channel_value
                    i += 1
            pixels[x, y] = (r, g, b)
    return image

def bit3(image, bin_message):
    pixels = image.load()
    i = 0
    message_length = len(bin_message) 

    for y in range(image.height):
        if i >= message_length:
            break
        for x in range(image.width):
            if i >= message_length:
                break
            r, g, b = pixels[x, y]
            for channel in range(3):
                channel_value = r if channel == 0 else g if channel == 1 else b 
                if i < message_length:
                    bit = int(bin_message[i:i+3]) 
                    print("bit: ", bit)
                    print("before: ", channel_value)
                    channel_value = (channel_value & 0b11111000) | bit
                    print("after", channel_value)
                    if (channel == 0):
                        r = channel_value
                    elif (channel == 1):
                        g = channel_value
                    else:
                        b = channel_value
                    i += 3
            pixels[x, y] = (r, g, b)
    return image

def out(image):
    pixels = image.load()
    i = 0
    message = ""
    isMarker = False
    for y in range(image.height):
        if isMarker:
            break
        for x in range(image.width):
            if isMarker:
                break
            r, g, b = pixels[x, y]
            for channel in range(3):
                channel_value = r if channel == 0 else g if channel == 1 else b 
                # print("channel_value: ", channel_value)
                channel_bin = format(channel_value, 'b')
                # print("channel_bin: ", channel_bin)
                message += channel_bin[-1]
                i += 1
                if message[-24:] == "011001010110111001100100":
                    isMarker = True
                    break
    message = message[:-24]
    return message

def out3(image):
    pixels = image.load()
    i = 0
    message = ""
    isMarker = False
    for y in range(image.height):
        if isMarker:
            break
        for x in range(image.width):
            if isMarker:
                break
            r, g, b = pixels[x, y]
            for channel in range(3):
                channel_value = r if channel == 0 else g if channel == 1 else b 
                print("channel_value: ", channel_value)
                channel_bin = format(channel_value, 'b')
                print("channel_bin: ", channel_bin)
                l = channel_bin[-3:]
                message += l
                i += 1
                if message[-24:] == "011001010110111001100100":
                    isMarker = True
                    break
    message = message[:-24]
    return message


file = "dog.png"
message = "Ever since 1886, when her great torch was lifted into place 305 feet above Liberty Island in New York Harbor, the colossal statue of Liberty Enlightening the World has symbolized America for millions of eager newcomers. Many wept as they neared the American shore, recalling all they had left behind and apprehensive about what they might find in the new land. But with their first glimpse of the statue, one Italian immigrant recalled, they were steadied ... by the concreteness of the symbol of America's freedom, and they dried their tear. The statue was the work of Alsatian sculptor Frederic Auguste Bartholdi and was intended to commemorate both a century of amity between France and the United States and the concept of political freedom shared by the two nations. The book that Liberty holds in her left hand symbolizes the Declaration of Independence. The main figure is attached to an iron framework designed by Gustave Eiffel, builder of France's Eiffel Tower. The statue was paid for by French contributors; American schoolchildren participated in a nationwide drive to raise funds for the pedestal. On a tablet within are inscribed the last five lines of a sonnet,The New Colossus, by Emma Lazarus, herself an immigrant:"
message += "end"
print("MESSAGE:", message)
org_image = Image.open(file) 

bin_message = ""
for s in message: 
    bin_message += format(ord(s), '08b')
print("bin_message: ", bin_message)

image = bit1(org_image, bin_message)
image.save("dog_coded.png")
image = bit3(org_image, bin_message)
image.save("dog_coded3.png")

copy_image = Image.open("dog_coded.png")
new_message_bin = out(copy_image)
new_message = ""
for i in range(0, len(new_message_bin), 8): 
    byte = new_message_bin[i:i+8] 
    char = chr(int(byte,2)) 
    new_message += char
print("bin_message", new_message)

copy_image3 = Image.open("dog_coded3.png")
new_message_bin3 = out3(copy_image3)
new_message3 = ""
for i in range(0, len(new_message_bin3), 8): 
    byte = new_message_bin3[i:i+8] 
    char = chr(int(byte,2)) 
    new_message3 += char
print("bin_message", new_message3)


