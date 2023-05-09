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

    while (len(key_text) < len(text)):  # создание последовательности слов ключа
        key_text += key_text

    
    for x in range(iteration):
        if (x > 0):   # на второй итерации result_text будет передавать прошлое значение и обнулятся
            text = result_text
            result_text = ""
        for i in range(len(text)):      # перебор алфавита открытого текста и определение смещения
            for j in range(len(alphabet)):
                if (text[i] == alphabet[j]):
                    text_shift = j
                    break

            for z in range(len(alphabet)):  # перебор алфавита ключа и определение смещения
                if (key_text[i] == alphabet[z]):
                    key_shift = z
                    break
            position = text_shift + key_shift   # определение финального смещения в алфавите для шифруемой буквы
            while (position >= len(alphabet)):  # чтобы смещение не зашло за лимит элементов алфавита
                position -= len(alphabet)

            result_text += alphabet[position]   # запись зашифрованного символа, результат
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

    while (len(key_text) < len(text)):  #  создание последовательности слов ключа
        key_text += key_text

    for x in range(iteration):
        if (x > 0):
            text = result_text
            result_text = ""
        for i in range(len(text)):      # перебор алфавита зашифрованного текста и определение смещения
            for j in range(len(alphabet)):
                if (text[i] == alphabet[j]):
                    text_shift = j
                    break

            for z in range(len(alphabet)):  # перебор алфавита ключа и определение смещения
                if (key_text[i] == alphabet[z]):
                    key_shift = z
                    break
            position = text_shift - key_shift   # определение финального смещения в алфавите для расшифровки буквы
            while (position < -len(alphabet)):  # чтобы смещение не зашло за лимит элементов алфавита
                position += len(alphabet)
            result_text += alphabet[position]   # запись зашифрованного символа, результат
    print(result_text)



task = input("Какую бы опрерацию вы бы хотели выполнить? 1.Шифрование 2.Дешифрование: ")    # меню для пользователя
if (task == "1"):
    encrypt()
elif(task == "2"):
    decrypt()
else:
    print("Неверно введен запрос.1.Шифрование 2.Дешифрование")
