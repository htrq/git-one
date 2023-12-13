import psycopg2
from tabulate import tabulate

def print_all_laptop_info():
    try:
        cursor = conn.cursor()
        cursor.execute('select * from public.laptop')
        laptops = cursor.fetchall()
        columns_laptop = ['code', 'model', 'speed', 'ram', 'hd', 'price', 'screen']
        print(tabulate(laptops, headers=columns_laptop))
    except:
        print("Ошибка при отправке запроса к базе данных x(")
    
def print_all_pc_info():
    try:
        cursor.execute('select * from public.pc')
        pc = cursor.fetchall()
        columns_pc = ['code', 'model', 'speed', 'ram', 'hd', 'cd', 'price']
        print(tabulate(pc, headers=columns_pc))
    except:
        print("Ошибка при отправке запроса к базе данных x(")

def print_all_printer_info():
    try:
        cursor.execute('select * from public.printer')
        printer = cursor.fetchall()
        columns_printer = ['code', 'model', 'color', 'type', 'price']
        print(tabulate(printer, headers=columns_printer))
    except:
        print("Ошибка при отправке запроса к базе данных x(")

def print_all_product_info():
    try:
        cursor.execute('select * from public.product')
        product = cursor.fetchall()
        columns_product = ['maker', 'model', 'type']
        print(tabulate(product, headers=columns_product))
    except:
        print("Ошибка при отправке запроса к базе данных x(")

def update_table_attribute():
    while True:
        print("Введите название таблицы в которую нужно внести изменения('laptop', 'PC', 'printer', 'product')")
        print("'back' вернутся в меню")
        response_code_insert = str(input("☻>> "))
        match response_code_insert:
            case 'back':
                break
            case 'laptop':
                print("Введите код ноутбука в который нужно внести изменения")
                response_code_insert = input("☻>> ")
                print("Введите колонку в которую нужно внести изменения('model', 'speed', 'ram', 'hd', 'price', 'screen')")
                response_column_insert = input("☻>> ")
                match response_column_insert:
                    case 'model':
                        model = input("Введите модель ноутбука(обратите внимание, чтобы модель была в таблице 'products'): ")
                        if (len(model) > 15):
                            print("Название модели не должно быть больше 15, сброс ввода")
                            continue
                        try:
                            cursor.execute(f"update public.laptop set model='{model}' where code='{response_code_insert}'")
                            conn.commit()
                            print("Строка обновлена")
                        except:
                            conn.commit()
                            print("Строка не обновлена, проверьте действительно ли существует такой код ноутбука и/или модель в таблице 'products")
                    case 'speed':
                        try:
                            speed = int(input("Введите скорость ноутбука во флопсах или как хочешь, неважно столбец не имеет связи реальностью: "))
                        except:
                            print("Должно быть только целое число, сброс ввода")
                            continue
                        if (len(str(speed)) > 10):
                            print("Слишком много символов для поля 'speed', не больше 10, сброс ввода")
                            continue
                        try:
                            cursor.execute(f"update public.laptop set speed='{speed}' where code='{response_code_insert}'")
                            conn.commit()
                            print("Строка обновлена")
                        except:
                            conn.commit()
                            print("Строка не обновлена, проверьте правильность введенных данных")
                    case 'ram':
                        try:
                            ram = int(input("Введите ОЗУ (ГБ) ноутбука: "))
                        except:
                            print("Должно быть только число, сброс ввода")
                            continue
                        if (len(str(ram)) > 10):
                            print("Слишком много символов для поля 'ram', не больше 10, сброс ввода")
                            continue
                        try:
                            cursor.execute(f"update public.laptop set ram='{ram}' where code='{response_code_insert}'")
                            conn.commit()
                            print("Строка обновлена")
                        except:
                            conn.commit()
                            print("Строка не обновлена, проверьте правильность введенных данных")
                    case 'hd':
                        try:
                            hd = int(input("Введите поле hd ноутбука(число в пределах 5, 12, 15, 20..): "))
                        except:
                            print("Должно быть только целое число, сброс ввода")
                            continue
                        if (len(str(hd)) > 3):
                            print("Слишком много символов для поля 'hd', не больше 3, сброс ввода")
                            continue
                        try:
                            cursor.execute(f"update public.laptop set hd='{hd}' where code='{response_code_insert}'")
                            conn.commit()
                            print("Строка обновлена")
                        except:
                            conn.commit()
                            print("Строка не обновлена, проверьте правильность введенных данных")
                    case 'price':
                        try:
                            price = int(input("Введите стоимость ноутбука: "))
                        except:
                            print("Должно быть только целое число, сброс ввода")
                            continue
                        if (len(str(price)) > 8):
                            print("Слишком много символов для поля 'price', не больше 8, сброс ввода")
                            continue
                        try:
                            cursor.execute(f"update public.laptop set price='{price}' where code='{response_code_insert}'")
                            conn.commit()
                            print("Строка обновлена")
                        except:
                            conn.commit()
                            print("Строка не обновлена, проверьте правильность введенных данных")
                    case 'screen':
                        try:
                            screen = int(input("Введите диагональ ноутбука(в дюьмах 12, 15, 20..): "))
                        except:
                            print("Должно быть только целое число, сброс ввода")
                            continue
                        if (len(str(screen)) > 3):
                            print("Слишком много символов для поля 'screen', не больше 3, сброс ввода")
                            continue
                        try:
                            cursor.execute(f"update public.laptop set screen='{screen}' where code='{response_code_insert}'")
                            conn.commit()
                            print("Строка обновлена")
                        except:
                            conn.commit()
                            print("Строка не обновлена, проверьте правильность введенных данных")
                    case _:
                        print("Нужно ввести приведенную выше колонку! Сброс ввода")
            case 'PC':
            # columns_pc = ['code', 'model', 'speed', 'ram', 'hd', 'cd', 'price']
                print("Введите код PC в который нужно внести изменения")
                response_code_insert = input("☻>> ")
                print("Введите колонку в которую нужно внести изменения('model', 'speed', 'ram', 'hd', 'cd', 'price')")
                response_column_insert = input("☻>> ")
                match response_column_insert:
                    case 'model':
                        model = input("Введите модель ноутбука(обратите внимание, чтобы модель была в таблице 'products'): ")
                        if (len(model) > 15):
                            print("Название модели не должно быть больше 15, сброс ввода")
                            continue
                        try:
                            cursor.execute(f"update public.PC set model='{model}' where code='{response_code_insert}'")
                            conn.commit()
                            print("Строка обновлена")
                        except:
                            conn.commit()
                            print("Строка не обновлена, проверьте действительно ли существует такой код ноутбука и/или модель в таблице 'products")
                    case 'speed':
                        try:
                            speed = int(input("Введите скорость ПК во флопсах или как хочешь, неважно столбец не имеет связи реальностью: "))
                        except:
                            print("Должно быть только целое число, сброс ввода")
                            continue
                        if (len(str(speed)) > 10):
                            print("Слишком много символов для поля 'speed', не больше 10, сброс ввода")
                            continue
                        try:
                            cursor.execute(f"update public.PC set speed='{speed}' where code='{response_code_insert}'")
                            conn.commit()
                            print("Строка обновлена")
                        except:
                            conn.commit()
                            print("Строка не обновлена, проверьте правильность введенных данных")
                    case 'ram':
                        try:
                            ram = int(input("Введите ОЗУ (ГБ) ПК: "))
                        except:
                            print("Должно быть только число, сброс ввода")
                            continue
                        if (len(str(ram)) > 10):
                            print("Слишком много символов для поля 'ram', не больше 10, сброс ввода")
                            continue
                        try:
                            cursor.execute(f"update public.PC set ram='{ram}' where code='{response_code_insert}'")
                            conn.commit()
                            print("Строка обновлена")
                        except:
                            conn.commit()
                            print("Строка не обновлена, проверьте правильность введенных данных")
                    case 'hd':
                        try:
                            hd = int(input("Введите поле hd ПК(число в пределах 5, 12, 15, 20..): "))
                        except:
                            print("Должно быть только целое число, сброс ввода")
                            continue
                        if (len(str(hd)) > 3):
                            print("Слишком много символов для поля 'hd', не больше 3, сброс ввода")
                            continue
                        try:
                            cursor.execute(f"update public.PC set hd='{hd}' where code='{response_code_insert}'")
                            conn.commit()
                            print("Строка обновлена")
                        except:
                            conn.commit()
                            print("Строка не обновлена, проверьте правильность введенных данных")
                    case 'cd':
                        try:
                            cd = int(input("Введите скорость записи дисковода ПК(например: 6х, 8х, 24х, вводите только число): "))
                        except:
                            print("Должно быть только целое число, сброс ввода")
                            continue
                        if (len(str(cd)) > 4):
                            print("Слишком много символов для поля 'cd', не больше 4, сброс ввода")
                            continue
                        try:
                            cursor.execute(f"update public.PC set cd='{cd}x' where code='{response_code_insert}'")
                            conn.commit()
                            print("Строка обновлена")
                        except:
                            conn.commit()
                            print("Строка не обновлена, проверьте правильность введенных данных")
                    case 'price':
                        try:
                            price = int(input("Введите стоимость ПК: "))
                        except:
                            print("Должно быть только целое число, сброс ввода")
                            continue
                        if (len(str(price)) > 8):
                            print("Слишком много символов для поля 'price', не больше 8, сброс ввода")
                            continue
                        try:
                            cursor.execute(f"update public.PC set price='{price}' where code='{response_code_insert}'")
                            conn.commit()
                            print("Строка обновлена")
                        except:
                            conn.commit()
                            print("Строка не обновлена, проверьте правильность введенных данных")
                    case _:
                        print("Нужно ввести приведенную выше колонку! Сброс ввода")
            case 'printer':
                print("Введите код принтера в который нужно внести изменения")
                response_code_insert = input("☻>> ")
                print("Введите колонку в которую нужно внести изменения('model', 'color', 'type', 'price')")
                response_column_insert = input("☻>> ")
                match response_column_insert:
                    case 'model':
                        model = input("Введите модель принтера(обратите внимание, чтобы модель была в таблице 'products'): ")
                        if (len(model) > 15):
                            print("Название модели не должно быть больше 15, сброс ввода")
                            continue
                        try:
                            cursor.execute(f"update public.printer set model='{model}' where code='{response_code_insert}'")
                            conn.commit()
                            print("Строка обновлена")
                        except:
                            conn.commit()
                            print("Строка не обновлена, проверьте действительно ли существует такой код принтера и/или модель в таблице 'products")
                    case 'color':
                        color = input("Введите цвет принтера(один символ): ")
                        if (len(color)> 1):
                            print("Цвет принтера не более чем 1 символ, сброс ввода")
                            continue
                        try:
                            cursor.execute(f"update public.printer set color='{color}' where code='{response_code_insert}'")
                            conn.commit()
                            print("Строка обновлена")
                        except:
                            conn.commit()
                            print("Строка не обновлена, проверьте правильность введенных данных")
                    case 'type':
                        type = input("Введите тип/категорию продукта: ")
                        if (len(type)> 10):
                            print("Тип/категория продука не больше 10 символов, сброс ввода")
                            continue
                        try:
                            cursor.execute(f"update public.printer set type='{type}' where code='{response_code_insert}'")
                            conn.commit()
                            print("Строка обновлена")
                        except:
                            conn.commit()
                            print("Строка не обновлена, проверьте правильность введенных данных")
                    case 'price':
                        try:
                            price = int(input("Введите стоимость принтера: "))
                        except:
                            print("Должно быть только целое число, сброс ввода")
                            continue
                        if (len(str(price)) > 8):
                            print("Слишком много символов для поля 'price', не больше 8, сброс ввода")
                            continue
                        try:
                            cursor.execute(f"update public.printer set price='{price}' where code='{response_code_insert}'")
                            conn.commit()
                            print("Строка обновлена")
                        except:
                            conn.commit()
                            print("Строка не обновлена, проверьте правильность введенных данных")
            case 'product':
                #maker model type
                print("Введите модель продукта в который нужно внести изменения")
                response_code_insert = input("☻>> ")
                print("Введите колонку в которую нужно внести изменения('maker', type')")
                response_column_insert = input("☻>> ")
                match response_column_insert:
                    case 'maker':
                        maker = input("Введите производителя продукта: ")
                        if (len(maker) > 10):
                            print("Название производителя продукта не более 10 символов, сброс ввода")
                            continue
                        try:
                            cursor.execute(f"update public.product set maker='{maker}' where model='{response_code_insert}'")
                            conn.commit()
                            print("Строка обновлена")
                        except:
                            conn.commit()
                            print("Строка не обновлена, проверьте действительно ли существует такая модель?")
                    case 'type':
                        type = input("Введите тип/категорию продукта: ")
                        if (len(type)> 10):
                            print("Тип/категория продука не больше 10 символов, сброс ввода")
                            continue
                        try:
                            cursor.execute(f"update public.product set type='{type}' where model='{response_code_insert}'")
                            conn.commit()
                            print("Строка обновлена")
                        except:
                            conn.commit()
                            print("Строка не обновлена, проверьте правильность введенных данных")
                    case _:
                        print("Нужно ввести приведенную выше колонку! Сброс ввода")
            case _:
                print("""
Нужно ввести приведенную выше таблицу!

- Полностью ломай. Ломай меня полностью. 
- Я хочу, чтоб ты ломал меня.
                """)
                                        


def insert_into_table_func():
    # columns_laptop = ['code', 'model', 'speed', 'ram', 'hd', 'price', 'screen']
    while True:
        print("Введите название таблицы('laptop', 'PC', 'printer', 'product')")
        print("'back' вернутся в меню")
        response_code_insert = str(input("☻>> "))
        match response_code_insert:
            case 'back':
                break
            case 'laptop':
                try:
                    code = int(input("Введите код ноутбука(убедитесь, чтобы не было такого же кода ноутбука): "))
                except:
                    print("Код ноутбука только целое число, сброс ввода")
                    continue
                if (len(str(code)) > 5):
                    print("Код ноутбука не должен быть больше 5, сброс ввода")
                    continue
                
                model = input("Введите модель ноутбука(обратите внимание, чтобы модель была в таблице 'products'): ")
                if (len(model) > 15):
                    print("Название модели не должно быть больше 15, сброс ввода")
                    continue
                
                try:
                    speed = int(input("Введите скорость ноутбука во флопсах или как хочешь, неважно столбец не имеет связи реальностью: "))
                except:
                    print("Должно быть только целое число, сброс ввода")
                    continue
                if (len(str(speed)) > 10):
                    print("Слишком много символов для поля 'speed', не больше 10, сброс ввода")
                    continue
                
                try:
                    ram = int(input("Введите ОЗУ (ГБ) ноутбука: "))
                except:
                    print("Должно быть только число, сброс ввода")
                    continue
                if (len(str(ram)) > 10):
                    print("Слишком много символов для поля 'ram', не больше 10, сброс ввода")
                    continue
                
                try:
                    hd = int(input("Введите поле hd ноутбука(число в пределах 5, 12, 15, 20..): "))
                except:
                    print("Должно быть только целое число, сброс ввода")
                    continue
                if (len(str(hd)) > 3):
                    print("Слишком много символов для поля 'hd', не больше 3, сброс ввода")
                    continue
                
                try:
                    price = int(input("Введите стоимость ноутбука: "))
                except:
                    print("Должно быть только целое число, сброс ввода")
                    continue
                if (len(str(price)) > 8):
                    print("Слишком много символов для поля 'price', не больше 8, сброс ввода")
                    continue

                try:
                    screen = int(input("Введите диагональ ноутбука(в дюьмах 12, 15, 20..): "))
                except:
                    print("Должно быть только целое число, сброс ввода")
                    continue
                if (len(str(screen)) > 3):
                    print("Слишком много символов для поля 'screen', не больше 3, сброс ввода")
                    continue
                
                try:
                    cursor.execute(f"insert into public.laptop(code, model, speed, ram, hd, price, screen) \
                    values('{code}', '{model}', '{speed}', '{ram}', '{hd}', '{price}', '{screen}')")
                    conn.commit()
                    print("Строка добавлена")
                except:
                    print("Строка не добавлена, в таблице 'products' скорее всего отсутствует первичный ключ для атрибута 'model' \
                        Создайте сначала строку в таблице 'products', где укажите соответствующий первичный ключ 'model'")
                    conn.commit()
                continue
            case 'product':
                maker = input("Введите производителя ноутбука: ")
                if (len(maker) > 10):
                    print("Название производителя продукта не более 10 символов, сброс ввода")
                    continue
                
                model = input("Введите модель продукта(убедитесь чтобы не было такой же модели): ")
                if (len(model) > 10):
                    print("Название модели не должно быть больше 10, сброс ввода")
                    continue
                
                type = input("Введите тип/категорию продукта: ")
                if (len(type)> 10):
                    print("Тип/категория продука не больше 10 символов, сброс ввода")
                    continue

                try:
                    cursor.execute(f"insert into public.product(maker, model, type) \
                    values('{maker}', '{model}', '{type}')")
                    conn.commit()
                    print("Строка добавлена")
                except:
                    conn.commit()
                    print("Строка не добавлена")
                    
                continue
            case 'PC':
                # columns_pc = ['code', 'model', 'speed', 'ram', 'hd', 'cd', 'price']
                try:
                    code = int(input("Введите код ПК(убедитесь, чтобы не было такого же кода ПК): "))
                except:
                    print("Код ПК только целое число, сброс ввода")
                    continue
                if (len(str(code)) > 5):
                    print("Код ПК не должен быть больше 5, сброс ввода")
                    continue
                
                model = input("Введите модель ПК(обратите внимание, чтобы модель была в таблице 'products'): ")
                if (len(model) > 15):
                    print("Название модели не должно быть больше 15, сброс ввода")
                    continue
                
                try:
                    speed = int(input("Введите скорость ПК во флопсах или как хочешь, неважно столбец не имеет связи реальностью: "))
                except:
                    print("Должно быть только целое число, сброс ввода")
                    continue
                if (len(str(speed)) > 10):
                    print("Слишком много символов для поля 'speed', не больше 10, сброс ввода")
                    continue
                
                try:
                    ram = int(input("Введите ОЗУ (ГБ) ПК: "))
                except:
                    print("Должно быть только число, сброс ввода")
                    continue
                if (len(str(ram)) > 10):
                    print("Слишком много символов для поля 'ram', не больше 10, сброс ввода")
                    continue
                
                try:
                    hd = int(input("Введите поле hd ПК(число в пределах 5, 12, 15, 20..): "))
                except:
                    print("Должно быть только целое число, сброс ввода")
                    continue
                if (len(str(hd)) > 3):
                    print("Слишком много символов для поля 'hd', не больше 3, сброс ввода")
                    continue
                
                try:
                    cd = int(input("Введите скорость записи дисковода ПК(например: 6х, 8х, 24х, вводите только число): "))
                except:
                    print("Должно быть только целое число, сброс ввода")
                    continue
                if (len(str(cd)) > 4):
                    print("Слишком много символов для поля 'cd', не больше 4, сброс ввода")
                    continue

                try:
                    price = int(input("Введите стоимость ПК: "))
                except:
                    print("Должно быть только целое число, сброс ввода")
                    continue
                if (len(str(price)) > 8):
                    print("Слишком много символов для поля 'price', не больше 8, сброс ввода")
                    continue
                
                try:
                    cursor.execute(f"insert into public.PC(code, model, speed, ram, hd, cd, price) \
                    values('{code}', '{model}', '{speed}', '{ram}', '{hd}', '{cd}x', '{price}')")
                    conn.commit()
                    print("Строка добавлена")
                except:
                    conn.commit()
                    print("Строка не добавлена, в таблице 'products' скорее всего отсутствует первичный ключ для атрибута 'model' \
                        Создайте сначала строку в таблице 'products', где укажите соответствующий первичный ключ 'model'")
                continue
                
            case 'printer':
                # columns_printer = ['code', 'model', 'color', 'type', 'price']
                try:
                    code = int(input("Введите код принтера(убедитесь, чтобы не было такого же кода принтера): "))
                except:
                    print("Должно быть только целое число, сброс ввода")
                    continue
                if (len(str(code)) > 5):
                    print("Код устройства не более 5 символов, сброс ввода")
                    continue
                
                model = input("Введите модель принтера(убедитесь, чтобы в таблице 'products' была такая модель): ")
                if (len(model) > 10):
                    print("Название модели не должно быть больше 10, сброс ввода")
                    continue
                
                color = input("Введите цвет принтера(один символ): ")
                if (len(color)> 1):
                    print("Цвет принтера не более чем 1 символ, сброс ввода")
                    continue

                type = input("Введите тип/категорию принтера: ")
                if (len(type)> 13):
                    print("Тип/категория продука не больше 13 символов, сброс ввода")
                    continue

                try:
                    price = int(input("Введите стоимость принтера: "))
                except:
                    print("Должно быть только целое число, сброс ввода")
                    continue
                if (len(str(price)) > 8):
                    print("Слишком много символов для поля 'price', не больше 8, сброс ввода")
                    continue

                try:
                    cursor.execute(f"insert into public.printer(code, model, color, type, price) \
                    values('{code}', '{model}', '{color}', '{type}', '{price}')")
                    conn.commit()
                    print("Строка добавлена")
                except:
                    conn.commit()
                    print("Строка не добавлена")
                continue

            case _:
                print("""
Нужно ввести приведенную выше таблицу!

- Полностью ломай. Ломай меня полностью. 
- Я хочу, чтоб ты ломал меня.
                """)

def delete_from_table_func():
    while True:
        print("Введите название таблицы в которой нужно удалить строку('laptop', 'PC', 'printer', 'product')")
        print("'back' вернутся в меню")
        response_code_insert = str(input("☻>> "))
        match response_code_insert:
            case 'back':
                break
            case 'laptop':
                print("Введите код ноутбука в который нужно удалить из таблицы")
                response_code_insert = input("☻>> ")
                try:
                    cursor.execute(f"delete from public.laptop where code='{response_code_insert}'")
                    conn.commit()
                    print("Строка удалена")
                except:
                    print("Строка не удалена, проверьте действительно ли существует такой код ноутбука")
            case 'PC':
            # columns_pc = ['code', 'model', 'speed', 'ram', 'hd', 'cd', 'price']
                print("Введите код PC в который нужно который нужно удалить")
                response_code_insert = input("☻>> ")
                try:
                    cursor.execute(f"delete from public.PC where code='{response_code_insert}'")
                    conn.commit()
                    print("Строка удалена")
                except:
                    print("Строка не удалена, проверьте действительно ли существует такой код PC")
            case 'printer':
                print("Введите код принтера в который нужно удалить")
                response_code_insert = input("☻>> ")
                try:
                    cursor.execute(f"delete from public.printer where code='{response_code_insert}'")
                    conn.commit()
                    print("Строка удалена")
                except:
                    print("Строка не удалена, проверьте действительно ли существует такой код принтера")
            case 'product':
                #maker model type
                print("Введите модель продукта в который нужно удалить, убедитесь, что в удаляемой строке поле модель не является первичным ключем в другой таблице")
                response_code_insert = input("☻>> ")
                try:
                    cursor.execute(f"delete from public.product where model='{response_code_insert}'")
                    conn.commit()
                    print("Строка удалена")
                except:
                    print("Строка не удалена, убедитесь, что в удаляемой строке поле модель не является первичным ключем в другой таблице")
            case _:
                print("""
Нужно ввести приведенную выше таблицу!

- Полностью ломай. Ломай меня полностью. 
- Я хочу, чтоб ты ломал меня.
                """)



# conn = psycopg2.connect('postgresql://postgres:heiadQ8K@localhost:5432/COmputers')

dbname = str(input("Введите название базы данных(пустое поле присвоит 'Computers'): "))
if (dbname == ''):
    dbname = 'Computers'

host = str(input("Введите адрес хоста (пустое поле присвоит localhost): "))
if (host == ''):
    host = 'localhost'

port = str(input("Введите порт подключения(пустое поле присвоит '5432'): "))
if (port == ''):
    port = '5432'
    
user = str(input("Введите имя пользователя(пустое поле присвоит 'postgres'): "))
if (user == ''):
    user = 'postgres'

response_password = str(input("Введите пароль: "))



try:
    # conn = psycopg2.connect(dbname='Computers', user='postgres', password='heiadQ8K', host='localhost', port='5432')
    conn = psycopg2.connect(dbname=dbname, user=user, password=response_password, host=host, port=port)
    cursor = conn.cursor()
    print("""         
⠀⠀⠀⠀⡠⠤⡀⠀⠀⢀⡴⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⠁⠀⢳⢲⠖⡞⠀⠀⢳⡤⠤⢤⣶⡤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠤⢤⣀⠆⠀⡶⠀⢀⠀⠀⡶⠀⢀⣀⣀⡈⠿⠁⠻⠏⠉⠓⣄⠀⠀⠀⠀⠀⠀
⠰⠖⠒⡾⠀⠀⠀⠈⠉⠁⠀⠀⠀⠭⠭⢤⡄⠀⠀⠀⠀⠀⠀⠀⢣⠀⣠⡄⣀⠀
⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠛⢣⣬⡄
⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣳⠐⣾⣠⠃
⠀⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠏⠉⠉⠀⠀
⠀⠀⠀⠘⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠌⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⡄⡠⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⣴⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠀⠀⠀⠑⠔⠁⠉⠉⠉⠉⠹⠤⠏⠀⠈⠒⠃⠀⠀⠀

"Meow-meow v.1" — Консольное приложение строго для бд из 10 лабы
Если получилось подключится к бд, но появляется ошибка при sql запросах, 
то проверьте правильность столбцов бд из задания и столбцов бд у вас на компьютере.
Copyright ©  by nobody

""")
except:
    print("Невозможно установить соединение с БД, проверьте правильность введенных данных")
    exit()


while True:
    print("""Меню команд:
quit Выйти из консольного приложения
laptops Вывести все данные о ноутбуках
PC Вывести все данные о компьютерах
printers Вывести все данные о принтерах
products Вывести все данные о продуктах
insert_into_table Добавить сущность в таблицу
update_table Внести изменения в таблицу
delete_from_table Удалить строку в таблице
""")
    # try:
    response_code = str(input("☻>> "))
#     except:
#         print("""
# Нужно ввести приведенные выше команды!

# - Полностью ломай. Ломай меня полностью. 
# - Я хочу, чтоб ты ломал меня.
# """)
#         continue
            
    match response_code:
        case 'quit':
            print("""
⡆⣐⢕⢕⢕⢕⢕⢕⢕⢕⠅⢗⢕⢕⢕⢕⢕⢕⢕⠕⠕⢕⢕⢕⢕⢕⢕⢕⢕⢕
⢐⢕⢕⢕⢕⢕⣕⢕⢕⠕⠁⢕⢕⢕⢕⢕⢕⢕⢕⠅⡄⢕⢕⢕⢕⢕⢕⢕⢕⢕
⢕⢕⢕⢕⢕⠅⢗⢕⠕⣠⠄⣗⢕⢕⠕⢕⢕⢕⠕⢠⣿⠐⢕⢕⢕⠑⢕⢕⠵⢕
⢕⢕⢕⢕⠁⢜⠕⢁⣴⣿⡇⢓⢕⢵⢐⢕⢕⠕⢁⣾⢿⣧⠑⢕⢕⠄⢑⢕⠅⢕
⢕⢕⠵⢁⠔⢁⣤⣤⣶⣶⣶⡐⣕⢽⠐⢕⠕⣡⣾⣶⣶⣶⣤⡁⢓⢕⠄⢑⢅⢑
⠍⣧⠄⣶⣾⣿⣿⣿⣿⣿⣿⣷⣔⢕⢄⢡⣾⣿⣿⣿⣿⣿⣿⣿⣦⡑⢕⢤⠱⢐
⢠⢕⠅⣾⣿⠋⢿⣿⣿⣿⠉⣿⣿⣷⣦⣶⣽⣿⣿⠈⣿⣿⣿⣿⠏⢹⣷⣷⡅⢐
⣔⢕⢥⢻⣿⡀⠈⠛⠛⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⡀⠈⠛⠛⠁⠄⣼⣿⣿⡇⢔
⢕⢕⢽⢸⢟⢟⢖⢖⢤⣶⡟⢻⣿⡿⠻⣿⣿⡟⢀⣿⣦⢤⢤⢔⢞⢿⢿⣿⠁⢕
⢕⢕⠅⣐⢕⢕⢕⢕⢕⣿⣿⡄⠛⢀⣦⠈⠛⢁⣼⣿⢗⢕⢕⢕⢕⢕⢕⡏⣘⢕
⢕⢕⠅⢓⣕⣕⣕⣕⣵⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣷⣕⢕⢕⢕⢕⡵⢀⢕⢕
⢑⢕⠃⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⢕⢕⢕
⣆⢕⠄⢱⣄⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢁⢕⢕⠕⢁
⣿⣦⡀⣿⣿⣷⣶⣬⣍⣛⣛⣛⡛⠿⠿⠿⠛⠛⢛⣛⣉⣭⣤⣂⢜⠕⢑⣡⣴⣿""")
            print("Пока!")
            exit()
        case 'laptops':
            print_all_laptop_info()
        case 'PC':
            print_all_pc_info()
        case 'printers':
            print_all_printer_info()
        case 'products':
            print_all_product_info()
        case 'insert_into_table':
            insert_into_table_func()
        case 'update_table':
            update_table_attribute()
        case 'delete_from_table':
            delete_from_table_func()
        case _:
            print("""
Нужно ввести приведенную выше команду! Даже без пробелов!

- Полностью ломай. Ломай меня полностью. 
- Я хочу, чтоб ты ломал меня.
            """)
cursor.close()
conn.close()