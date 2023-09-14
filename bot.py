import logging
from aiogram import executor
from create_bot import dp
from data_base import mysql_db
from handlers import client, other, admin

async def on_startup(_):
    print('Бот вышел в онлайн')
    logging.info('Start bot(logging.info)')
    mysql_db.mysql_start()

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                     level=logging.INFO,
                     filename='bot.log'
                     )

#logging.basicConfig(level=logging.INFO)


client.register_handlers_client(dp)
#admin.register_handlers_admin(dp)
other.register_handlers_other(dp)









if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)