from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types , Dispatcher #(если types использовать буду в хэндлере)

from create_bot import dp, bot
from keyboards import kb_client, kb_client2, kb_clients, kb_client3, kb_client4, inkb, inkb2, inkb3

from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text

from data_base import mysql_db

import asyncio

import pytz
from datetime import datetime
timezone = pytz.timezone('Asia/Yekaterinburg')



class FSMcl(StatesGroup):
    user = State() 
    Habit = State()
    HH = State()
    MM = State()
    Day = State()
    Month = State()
    Year = State()
    Result = State()


class FSMC(StatesGroup):
    habit0 = State()
    month0 = State()
    year0 = State()

 
users = [388115445, 748503273] 

ids = 11111
ids2 = 22222

# @dp.message_handler(commands=['start', 'help'])   #(декоратор тут не нужен, так как есть регистрация)
async def commands_start(message : types.Message):
    await bot.send_message(message.from_user.id, 'Привет! Я бот, который поможет тебе сформировать полезные привычки, с чего начнем?', reply_markup=kb_client)
    # await bot.send_message(message.from_user.id, f"Ваш ID {message.from_user.id}" ) #Ваш ID и тут бот пишет ID пользователя


async def com_help(message : types.Message):
    await bot.send_message(message.from_user.id, 'Если нужна помощь, возникли вопросы, появились проблемы с ботом, то напиши мне @Wizard700')


async def comtest(message : types.Message):
    await bot.send_message(message.from_user.id, 'Вы вызвали команду Close keyboard', reply_markup=ReplyKeyboardRemove())


async def info_introducing_habits(message: types.Message):
    introduction = '''
Внедрение привычек – это процесс формирования поведенческих рутин, которые становятся автоматическими и повторяются регулярно. 
Это может быть изменение питания, начало занятий спортом, ежедневное чтение, или любая другая привычка, которую вы стремитесь развить. 
Хотя внедрение новых привычек может быть сложным, это достижимо с правильным подходом и настойчивостью. 
Важно понимать, что формирование новой привычки требует времени, настойчивости и последовательности. 
Необходимо быть готовым к сомнениям, отклонениям и побочным эффектам, но при упорстве и позитивном настрое вы сможете успешно внедрить новую привычку в свою жизнь.
    '''

    await bot.send_message(message.from_user.id, introduction, reply_markup=kb_client)

    await bot.send_chat_action(message.from_user.id, types.ChatActions.TYPING)
    await asyncio.sleep(5)
    await bot.send_message(message.from_user.id, 'Теперь перейдем к тому, как именно внедрить полезные привычки.')

    await bot.send_chat_action(message.from_user.id, types.ChatActions.TYPING)
    await asyncio.sleep(2)
    await bot.send_message(message.from_user.id,
                           '1. Для начала стоит определить какие привычки вы хотите внедрить. Список возможных полезных привычек можно узнать по кнопке "Список полезных привычек".')

    await bot.send_chat_action(message.from_user.id, types.ChatActions.TYPING)
    await asyncio.sleep(3)
    await bot.send_message(message.from_user.id,
                           '2. Затем определите для себя сколько раз в неделю вы хотите выполнять эту привычку, рекомендуется выполнять ежедневно чтобы сформировать автоматизм и не сдаться из-за банальной лени.')

    await bot.send_chat_action(message.from_user.id, types.ChatActions.TYPING)
    await asyncio.sleep(3)
    await bot.send_message(message.from_user.id,
                           '3. После того, как вы определились с частотой привычки, можно добавить привычку по кнопке "Добавить привычку" и установить напоминание, чтобы не забыть ее выполнять')


    await bot.send_chat_action(message.from_user.id, types.ChatActions.TYPING)
    await asyncio.sleep(3)
    await message.reply(
        'Поздравляю! Теперь ты уже можешь начать внедрять полезные привычки. Хочешь чтобы я рассказал еще советы по внедрению полезных привычек и их особенности?',
        reply_markup=inkb3)


@dp.callback_query_handler(Text(startswith='res_1'))
async def yes2(callback: types.CallbackQuery):
    chat_id = callback.message.chat.id
    await callback.answer('Хорошо, продолжим!', show_alert=True)

    await bot.send_chat_action(chat_id, types.ChatActions.TYPING)
    await asyncio.sleep(2)

    txt_stages_implementations_habits = '''
В формировании любой привычки основа лежит на 4 стадиях:
1. Стимул , он побуждает мозг инициировать то или иное поведение. Это информация о подкреплении.
2. Желание - основной фактор мотивации. То , чего мы хотим, это не конкретная привычка, а изменения, которые она приносит с собой. Ты не хочешь смотреть ютуб, ты хочешь получать удовольствие, дофамин.
3. Реакция - получение подкрепления. Возникнет ли реакция, зависит от мотивации и от количества сложностей, которые ассоциируются с поведением (оно и есть реакция).
4. Вознаграждение - нужно для удовлетворения желания, а также учит нас какие действия стоит запомнить на будущее.
'''

    await bot.send_message(chat_id, txt_stages_implementations_habits)

    await bot.send_chat_action(chat_id, types.ChatActions.TYPING)
    await asyncio.sleep(3)

    txt_four_principles = '''
Также чтобы сформировать полезную привычку важно помнить о 4 принципах:
1. Заметность
2. Привлекательность
3. Простота
4. Удовлетворенность
'''
    await bot.send_message(chat_id, txt_four_principles)

    await bot.send_chat_action(chat_id, types.ChatActions.TYPING)
    await asyncio.sleep(5)

    txt_recomends = '''
Базовые рекомендации по внедрению полезные привычек:    
1. Делать привычку каждый день, не пропускать более 2х дней.
2. Сила в маленьких шагах. Начните с малого, даже 5 минут в день лучше чем 0. (На 1% лучше каждый день.)
3. Формируйте конкретные намерения, используя формулу: Я буду делать [привычка] в [время] в [место].
4. Привычки легче выполнять после определенного "триггера". Например после чистки зубов я сразу буду идти читать книгу в течении 20 минут.
5. Измените окрудающую среду. Например если вы хотите чаще играть на гитаре, то стоит ее поставить на видное место, там где вы часто бываете.
6. Сложную задачу можно разделить на более мелкие привычки. Например написать диплом - открыть Word файл, найти статьи, написать текст в течении 10 минут.
7. Используйте трекер привычек, чтобы отслеживать результаты и мотивировать себя успехами.
8. Искать позитивные моменты, за что вы будете любить делать поелнзые привычки.
9. Лучше разиваться вместе с другими людьми и делиться своими успехами друг другу.
10. Помните , что внедрение полезные привычек может занять продолжительное время и результат может прийти не сразу.  Это марафон, игра в долгую.

'''
    await bot.send_message(chat_id, txt_recomends)


@dp.callback_query_handler(Text(startswith='res_-1'))
async def no2(callback: types.CallbackQuery):
    await callback.answer('Понял вас, тогда можете сразу добавлять привычки.', show_alert=True)


async def list_habits(message : types.Message):
    list_habits = '''
Список полезных привычек:

Чтобы стать эффективнее:
Ведите дневник достижений.
Достигайте одну микроцель каждый день.
Ежедневно записывайте три хорошие вещи, которые случились с вами за день.
Планируйте свой день, составляя список того, что нужно сделать, и придерживайтесь его выполнения.
Используйте визуализацию, чтобы связать определения новых слов или значения.
Практикуйте аффирмации.

Чтобы стать счастливее:
Улыбайтесь каждый день.
Гуляйте или катайтесь на велосипеде минимум 20 минут каждый день.
Посвятите 30 минут своего времени в день любимому занятию, которое приносит удовольствие и расслабляет вас.

Если вы хотите лучше справляться со стрессом:
Практикуйте медитацию, осознанность. 
Глубоко дышите на протяжении двух минут. Сконцентрируйтесь на дыхании.
Сделайте 10-минутную растяжку.

Спорт, активность:
Делайте зарядку утром.
Практикуйте заняте йогой.
Занимайтесь спортом.
Начните бегать.

Духовность, развитие:
Ведите тезаурус. Записывайте туда мысли о том, что вас вдохновляет, какие цвета, текстуры, формы бросаются в глаза.
Читайте книги ежедневно.
Слушайте подкасты, аудиокниги.
Изучайте иностранные языки.
Освойте новый навык.
Освойте игру на музыкальном инструменте.
Практикуйте дофаминовое голодание.
Записывайте свои мысли в ежедневник.

Финансы:
Откладывайте 10% ежемесячно.
Инвестируйте в акции, криптовалюту, недвижимость.

Здоровье:
Практикуйте контрасный душ.
Пейте чаще воды в течении дня.
Кушайте чаще фрукты и овощи.
Откжитесь от сладкого.
Ложитесь спать и просыпаться в одно и то же время.
Ухаживайте за собой.
'''

    await bot.send_message(message.from_user.id, list_habits)




async def read_about_habits(message: types.Message):
    about_habits = '''
Книги на тему привычек:
1. «Атомные привычки» - Джеймс Клир
2. «Триггеры» - Маршалл Голдсмит и Марк Рейтер
3. «Власть привычки. Почему мы живём и работаем именно так, а не иначе» - Чарлз Дахигг
4. «Мини-привычки: меньшие привычки, большие результаты» - Стивен Гиз
5. «Мой продуктивный год: Как я проверил самые известные методики личной эффективности на себе» - Бэйли Крис

Полезные ресурсы о привычках:
1. Телеграм канал о привычках 52 недели одержимости: https://t.me/kurs_obrazovanie
2. Как прививать привычки: https://spectator.ru/entry/6458
3. Формирование полезных привычек: https://goo.su/3tZUS
4. Полезные привычки и как их формировать: https://goo.su/SYar
5. Формируем полезные привычки и наполняемся радостью: https://goo.su/DxeeIR 
6. Повтор полезных действий: как научиться формировать привычки: https://goo.su/WzW505U
7. Как бороться с ленью: https://spectator.ru/entry/6335

Приложения и сайты для фомирования привычек:
1. HWYD https://spectator.ru/entry/6358
2. TickTick https://ticktick.com/webapp/#q/all/habit
3. Notion https://vc.ru/u/1928077-notionbox/712460-shablon-trekera-privychek-v-notion

'''
    await bot.send_message(message.from_user.id, about_habits, reply_markup=kb_client)


async def com_newhabit(message : types.Message):
    global ids2
    ids2 = message.from_user.id
    await message.reply('Хорошо, теперь напиши мне какую привычку ты хочешь сформировать? Например: "Чтение"', reply_markup=kb_client2)
    print(ids,ids2)
    await FSMcl.next()


#Выход из состояний, если пользователь захочет прервать процесс создания привычки
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Вы прервали процесс создания привычки', reply_markup=kb_client)

hab = 'habitss'
hab2 = 'zero0'


today = datetime.now(timezone)

month1 = str(today)[5:7]  #Месяц текущий
year1 = str(today)[0:4] #Год текущий


months = {
    '01' : 'январь', 
    '02' : 'февраль', 
    '03' : 'март', 
    '04' : 'апрель',
    '05' : 'май',
    '06' : 'июнь',
    '07' : 'июль',
    '08' : 'август',
    '09' : 'сентябрь',
    '10' : 'октябрь',
    '11' : 'ноябрь',
    '12' : 'декабрь'
    }

name_month = months.get(month1)


async def namehabit(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user'] = message.from_user.id
        data['Habit'] = message.text
        global hab
        hab = data['Habit']
    await FSMcl.next()

    #Варианты: Установить уведомление/Не устанавливать (в таком случае в бд занести пробел или ? в графу часы и минуты)
    await message.reply('Укажите в какое время спрашивать о выполнении привычки, например: "10:00" ') 
    await FSMcl.next() 


async def time_notyfy_no(message: types.Message, state: FSMContext):
    await message.reply('Напоминание не установлено')


hh = 0
mm = 0    

async def time_notify(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['HH'] = str(message.text[0:2])
        data['MM'] = str(message.text[3:5])
        global hh
        global mm
        hh = data['HH']
        mm = data['MM']

        today = datetime.now(timezone)

        data['Day'] = str(today)[8:10] #День
        data['Month'] = str(today)[5:7] #Месяц
        data['Year'] = str(today)[0:4] #год

        data['Result'] = '?'

        await message.reply('Устанавливаем напоминание в назначенное время?', reply_markup=inkb2)
        await FSMcl.next()
        #Тут еще добавить, "Хорошо, напоминанание установлено в HH:MM"
        #И добавить отмену, "Напоминание не установлено", хотите выбрать другое время? (выбор: Да, рдугое время/Нет, не люблю уведомления)
        #(Но из БД не удалять, вдруг пользователь не любит уведомления)

        #Добавить удаление из БД привычки + удаление напоминания 

        #Добавить удаление напоминания, но привычка остается

    await mysql_db.mysql_add_command3(state)
    await state.finish()


async def time_notify2(callback: types.CallbackQuery):
    await callback.answer('Напоминание установлено', show_alert=True)

    # Получаем текущее время в указанном часовом поясе
    current_time = datetime.now(timezone)

    # Алгоритм по отправке напоминания (самая простой вариант высчитать секунды)
    t1 = (current_time.hour*60*60) + (current_time.minute*60) + (current_time.second) #time now(second)
    t2 = (int(hh)*60*60) + (int(mm)*60) #time planned (second)
    s = 0

    if t2 > t1:
        s = t2-t1
    if t1 > t2:
        s = 86400 - (t1-t2)

    users = [ids2] 
    for user_id in users:
        await asyncio.sleep(int(s)) #секунды
        await bot.send_message(user_id, f'Выполнил(а) сегодня привычку "{hab}" ?', reply_markup=inkb)


@dp.callback_query_handler(Text(startswith='yes_1'))
async def yes(callback : types.CallbackQuery):
    await mysql_db.mysql_update_yes(hab)
    await callback.answer('Привычка выполнена', show_alert=True)


@dp.callback_query_handler(Text(startswith='no_-1'))
async def no(callback : types.CallbackQuery):
    await mysql_db.mysql_update_no(hab)
    await callback.answer('Привычка не выполнена', show_alert=True)


#Вывод у текущего пользователя всех его привычек, уведомлений, но вывод некрасивый через
async def habits_info(message : types.Message):
    global ids
    ids = message.from_user.id
    await mysql_db.mysql_read4(ids, message)

#Вывод 2ой
async def habits_info2(message : types.Message, state: FSMContext):
 #чтобы выдать данные одного пользователя, а не всех 
    await bot.send_message(message.from_user.id, 'Информацию по какой привычке выдать?')
    await FSMC.next()
    #добавить инлайн выбор нужной привычки из списка доступных


#Информация по привычке конкретной за определенный месяц и определнный год
async def test(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['habit0'] = message.text
        global hab2
        hab2 = message.text
        await bot.send_message(message.from_user.id, 'Введите число месяца, за который нужно узнать информацию о привычке, например: "01" (если январь) ')
        await FSMC.next()

async def test2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['month0'] = message.text
        global month1
        month1 = message.text
        global name_month
        name_month = months.get(month1)
        await bot.send_message(message.from_user.id, 'Введите год, за который нужно узнать информацию о привычке, например: "2022" ')
        await FSMC.next()



async def test3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['year0'] = message.text
        global year1
        year1 = message.text
        global ids
        ids = message.from_user.id
        await mysql_db.mysql_read5(ids, hab2, month1, year1, name_month, message)
        await FSMC.next()



#Регистрация хэндлеров(вместо декораторов)
def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start'])
    dp.register_message_handler(com_help, lambda message: 'Помощь' in message.text)

    dp.register_message_handler(info_introducing_habits,
                                lambda message: 'Как внедрить привычки?' in message.text)
    dp.register_message_handler(read_about_habits, lambda message: 'Что почитать про привычки?' in message.text)
    dp.register_message_handler(list_habits, lambda message: 'Список полезных привычек' in message.text)

    dp.register_message_handler(habits_info, lambda message: 'Все данные' in message.text)
    dp.register_message_handler(habits_info2,  lambda message: 'Информация по одной привычке' in message.text)

    dp.register_message_handler(test, state=FSMC.habit0)
    dp.register_message_handler(test2, state=FSMC.month0)
    dp.register_message_handler(test3, state=FSMC.year0)

    # dp.register_message_handler(user, state=FSMcl.user)
    dp.register_message_handler(comtest, commands=['Close_kb'])

    dp.register_message_handler(com_newhabit, lambda message: 'Добавить новую привычку' in message.text)

    dp.register_message_handler(cancel_handler, state = "*", commands='Отменить создание привычки')
    dp.register_message_handler(cancel_handler, Text(equals='Отменить создание привычки', ignore_case=True), state = "*")

    dp.register_message_handler(namehabit, state=FSMcl.user)
    dp.register_message_handler(namehabit, state=FSMcl.Habit)

    dp.register_message_handler(time_notify, state=FSMcl.HH)
    dp.register_message_handler(time_notify, state=FSMcl.MM)
    dp.register_message_handler(time_notify, state=FSMcl.Day)
    dp.register_message_handler(time_notify, state=FSMcl.Month)
    dp.register_message_handler(time_notify, state=FSMcl.Year)
    dp.register_message_handler(time_notify, state=FSMcl.Result)


    dp.register_callback_query_handler(time_notify2, Text(startswith='set'))

    
