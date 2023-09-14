import pymysql
from data_base.config_db import host, user, password, db_name
from create_bot import bot


def mysql_connection():
    try:
        global connection
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

        print("Mysql Successfully connected...")
        print("#" * 20)
        print("#" * 20)

    except Exception as ex:
        print("My sql Connection refused...")
        print(ex)
        print("#" * 20)
        print("#" * 20)


def close_connection_to_db():
    print("Mysql Connection to db is closed")
    connection.close()


def mysql_start():
    try:
        global connection
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

        print("Mysql Successfully connected...")
        print("#" * 20)

        #try:
            # create table
        with connection.cursor() as cursor:
            create_table_query = "CREATE TABLE IF NOT EXISTS menu3 (id INT UNSIGNED NOT NULL " \
                                 "AUTO_INCREMENT PRIMARY KEY, user TEXT, Habits TEXT, HH TEXT, MM TEXT," \
                                 " Day TEXT, Month TEXT, Year TEXT, Result TEXT);"
            cursor.execute(create_table_query)


            change_table_collation()
            print("Changed table collation")

            type = "ALTER TABLE `menu3` CHANGE `id` `id` INT NOT NULL AUTO_INCREMENT;"
            cursor.execute(type)
            print("Mysql auto_inkrement")


            print("Mysql Table created/connected successfully")



        # finally:
        #     print("Mysql Connection to db is closed")
        #     connection.close()


    except Exception as ex:
        print("My sql Connection refused...")
        print(ex)

#Смена кодировки
def change_table_collation():
    with connection.cursor() as cursor:
        show_columns_query = "SHOW COLUMNS FROM menu3"
        cursor.execute(show_columns_query)
        columns = cursor.fetchall()

        for column in columns:
            column_name = column['Field']

            # Генерируем SQL-запрос для изменения кодировки столбца
            alter_query = f"ALTER TABLE menu3 MODIFY COLUMN {column_name} VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci"

            # Выполняем SQL-запрос
            cursor.execute(alter_query)
        connection.commit()


# Добавление данных в таблицу
async def mysql_add_command3(state):
    async with state.proxy() as data:
        mysql_connection()
        try:
            with connection.cursor() as cursor:
                insert_query = "INSERT INTO menu3 (user, Habits, HH, MM, Day, Month, Year, Result) VALUES (%s, %s, %s, %s, %s, %s, %s,  %s);"
                cursor.execute(insert_query, tuple(data.values()))
                connection.commit()  # save
        finally:
            close_connection_to_db()


async def mysql_update_yes(hab):
    mysql_connection()
    try:
        with connection.cursor() as cursor:
            update_query = "UPDATE menu3 SET Result = %s WHERE Habits = %s"
            cursor.execute(update_query, ('✅', hab))
            connection.commit()
    finally:
        close_connection_to_db()

async def mysql_update_no(hab):
    mysql_connection()
    try:
        with connection.cursor() as cursor:
            update_query = "UPDATE menu3 SET Result = %s WHERE Habits = %s"
            cursor.execute(update_query, ('❌', hab))
            connection.commit()
    finally:
        close_connection_to_db()

#Вывод у текущего пользователя всех его привычек, уведомлений
async def mysql_read4(ids, message):
    mysql_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM menu3 WHERE user = %s', (ids,))
            for ret in cursor.fetchall():
                await bot.send_message(message.from_user.id, f"{ret['user']}:{ret['Habits']}:{ret['HH']}:{ret['MM']}:{ret['Day']}:{ret['Month']}:{ret['Year']}:{ret['Result']}")
                #await bot.send_message(message.from_user.id, ret) # можно и так, но выведет весь словарь ret (со всеми скобками  и всеми данными)
    finally:
        close_connection_to_db()

h = [] #Дни, когда была привычка
r = [] #Результат по привычке в конкретные дни из h

a = []
for i in range(1,32):
    a.append(i)


# По конкретной привычке за определенный месяц и определенный год
async def mysql_read5(ids, hab2, month1, year1, name_month, message):
    mysql_connection()
    try:
        await bot.send_message(message.from_user.id, f'Информация по привычке: "{hab2}" за месяц {name_month}, {year1} года')
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM menu3 WHERE user = %s AND Habits = %s AND Month = %s AND Year = %s', (ids, hab2, month1, year1))
            for ret in cursor.fetchall():
                global h, r
                h.append(ret['Day'])
                r.append(ret['Result'])

                for i in range(len(a)):
                    if a[i] == int(ret['Day']):
                        a[i] = str(ret['Day']) + str(ret['Result'])

            await bot.send_message(message.from_user.id, ''.join(str(a)))
            element = a.clear()
            for i in range(1, 32):
                a.append(i)

    finally:
        close_connection_to_db()