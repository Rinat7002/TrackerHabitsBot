from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton  # , ReplyKeyboardRemove

b1 = KeyboardButton('/start')
b2 = KeyboardButton('Добавить новую привычку')
b3 = KeyboardButton('Помощь')
b4 = KeyboardButton('/Close_kb')

b5 = KeyboardButton('Все данные')
b10 = KeyboardButton('Информация по одной привычке')

b6 = KeyboardButton('Отменить создание привычки')
# b7 = KeyboardButton('Установить напоминание')
b8 = KeyboardButton('Да')
b9 = KeyboardButton('Нет')

b11 = KeyboardButton('Вывести информацию')
b12 = KeyboardButton('Нет')

b13 = KeyboardButton('Как внедрить привычки?')
b14 = KeyboardButton('Что почитать про привычки?')
b15 = KeyboardButton('Список полезных привычек')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client2 = ReplyKeyboardMarkup(resize_keyboard=True)

kb_clients = ReplyKeyboardMarkup()
kb_client3 = ReplyKeyboardMarkup()
kb_client4 = ReplyKeyboardMarkup()

# Один из вариантов (все умещается, но надо скроллить)
# kb_client.insert(b13).insert(b2).add(b5).insert(b10).add(b15).add(b14).add(b3) #Клава без старта
# kb_client2.insert(b13).insert(b2).add(b5).insert(b10).add(b15).add(b14).add(b3).insert(b6)


# Другие варианты
# kb_client.row(b13, b2, b5, b10, b15, b14, b3) #В 1 строку все кнопки
# kb_client.add(b13).add(b2).add(b5).add(b10).add(b15).add(b14).add(b3) #Каждая кнопка с новой строки
# kb_client.insert(b13).insert(b2).insert(b5).insert(b10).insert(b15).insert(b14).insert(b3) #3 столбца по 2 и снизу помощь

kb_client.row(b13, b2).row(b5, b10).row(b15, b14).add(b3)
kb_client2.row(b13, b2).row(b5, b10).row(b15, b14).add(b3).insert(b6)
# kb_client2.insert(b13).insert(b2).add(b5).insert(b10).add(b15).add(b14).add(b3).insert(b6)

# kb_clients.add(b7).add(b6)
# kb_client3.add(b8).add(b9)
# kb_client4.add(b11).add(b12)

# kb_client.row(b1,b2,b3,b4,b5,b6,)


# Сама кнопка (после нажатия появляются часы)
inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Да', callback_data='yes_1'), \
                                             InlineKeyboardButton(text='Нет', callback_data='no_-1'))

inkb2 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Установить напоминание', callback_data='set'))

inkb3 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Конечно!', callback_data='res_1'), \
                                              InlineKeyboardButton(text='Нет, в другой раз.', callback_data='res_-1'))