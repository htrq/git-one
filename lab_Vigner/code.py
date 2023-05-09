alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя .,123456789'


def encrypt():
    print("Шифрование...")
    text_shift = 0
    key_shift = 0
    text = input('Введите текст: ').lower()
    key_text = input('Введите ключ: ').lower()
    iteration = int(input('Введите кол-во итераций: '))
    position = 0
    result_text = ""

    while (len(key_text) < len(text)):
        key_text += key_text

    
    for x in range(iteration):
        if (x > 0):
            text = result_text
            result_text = ""
        for i in range(len(text)):
            for j in range(len(alphabet)):
                if (text[i] == alphabet[j]):
                    text_shift = j
                    break

            for z in range(len(alphabet)):
                if (key_text[i] == alphabet[z]):
                    key_shift = z
                    break
            position = text_shift + key_shift
            while (position >= len(alphabet)):
                position -= len(alphabet)

            #print(alphabet[position], end='')
            result_text += alphabet[position]
    print(result_text)

def decrypt():
    print("Дешифрование...")
    text_shift = 0
    key_shift = 0
    text = input('Введите текст: ').lower()
    key_text = input('Введите ключ: ').lower()
    iteration = int(input('Введите кол-во итераций: '))
    position = 0
    result_text = ""

    while (len(key_text) < len(text)):
        key_text += key_text

    for x in range(iteration):
        if (x > 0):
            text = result_text
            result_text = ""
        for i in range(len(text)):
            for j in range(len(alphabet)):
                if (text[i] == alphabet[j]):
                    text_shift = j
                    break

            for z in range(len(alphabet)):
                if (key_text[i] == alphabet[z]):
                    key_shift = z
                    break
            position = text_shift - key_shift
            while (position < -len(alphabet)):
                position += len(alphabet)
            result_text += alphabet[position]
    print(result_text)


task = input("Какую бы опрерацию вы бы хотели выполнить? 1.Шифрование 2.Дешифрование: ")
if (task == "1"):
    encrypt()
elif(task == "2"):
    decrypt()
else:
    print("Неверно введен запрос.1.Шифрование 2.Дешифрование")
