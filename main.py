import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import logging
import random
from keybords import kb1, kb2, kb3, kb4
from csv import DictWriter, DictReader
import csv
import os
import re
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
#from aiogram.types.bot_command import BotCommand
import requests

def file_exists(file_name):
    return os.path.exists(file_name)

# подключаем логирование
logging.basicConfig(level=logging.INFO)

# создаем обьект бота
bot = Bot(token=config.token)

# диспечер
dp = Dispatcher()

        


def read_file(file_name):
    data = []
    with open(file_name, "r", encoding='utf-8') as file:
        f_reader = csv.DictReader(file, delimiter=';')
        for row in f_reader:
            data.append(row)
    return data

def write_to_csv(user_info):
    file_name = 'appointments.csv'
    fieldnames = ['Name', 'Chat ID', 'Appointment Date']

    if not os.path.exists(file_name):
        with open(file_name, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

    with open(file_name, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(user_info)
        
def delete_file(file_name):
    confirm = input(f"Вы уверены, что хотите удалить файл '{file_name}'? (да/нет): ")
    if confirm.lower() == 'да':
        try:
            os.remove(file_name)
            print(f"Файл '{file_name}' успешно удален.")
        except FileNotFoundError:
            print(f"Файл '{file_name}' не найден.")
        except Exception as e:
            print(f"Ошибка при удалении файла '{file_name}': {e}")
    else:
        print("Удаление отменено.")
        
      
def create_specialists_file(file_name):
    if os.path.exists(file_name):
        choice = input(f"Хотите ли вы удалить или обновить таблицу '{file_name}'? \nЕсли хотите создать таблицу со специалистами заново, то удалите предыдущую, введя: Удалить. \nДля обновления данных введите: Обновить.\n---->")
        if choice.lower() == 'удалить':
            delete_file(file_name)
        else:
            print("Готово.")
    else:
        print(f"Таблица '{file_name}' создана.")
        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['Name', 'Phone'])  # Добавляем заголовки 'Name' и 'Phone'
    
    print("Введите новые данные.")
    
    with open(file_name, 'a+', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        file.seek(0)  # Переходим в начало файла для чтения существующих данных
        existing_data = set(tuple(row) for row in csv.reader(file, delimiter=';'))
        
        if not existing_data:  # Если файл пустой, записываем заголовки
            writer.writerow(['Name', 'Phone'])
        
        while True:
            name = input("Введите имя (или 'exit' для завершения): ")
            if name.lower() == 'exit':
                break
            phone = input("Введите номер телефона: ")
            
            if (name, phone) in existing_data:
                print("Такие данные уже существуют в таблице.")
            else:
                writer.writerow([name, phone])
                print("Данные успешно добавлены в таблицу.")
    
    print("Добавление данных завершено.")
    
# Пример использования функции
create_specialists_file("specialists.csv")


def create_contacts_file(file_name):
    if os.path.exists(file_name):
        choice = input(f"Хотите ли вы удалить или обновить таблицу '{file_name}'? \nЕсли хотите создать таблицу с адресом заново, то удалите предыдущую, введя: Удалить. \nДля обновления данных введите: Обновить.\n---->")
        if choice.lower() == 'удалить':
            confirm = input(f"Вы уверены, что хотите удалить данные из таблицы '{file_name}'? (да/нет): ")
            if confirm.lower() == 'да':
                with open(file_name, 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file, delimiter=';')
                    writer.writerow(['city', 'address'])
                print("Данные успешно удалены.")
            else:
                print("Удаление отменено")
        else:
            print("Готово")
    else:
        print(f"Таблица '{file_name}' не найдена.")
    
    with open(file_name, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        
        while True:
            city = input("Введите название города (или 'exit' для завершения): ")
            if city.lower() == 'exit':
                break
            address = input("Введите адрес: ")
            writer.writerow([city, address])
            print("Данные добавлены в таблицу.")

# Создание файла contacts_file.csv и добавление данных
create_contacts_file('contacts_file.csv')
        

@dp.message(lambda message: message.text.lower() == 'специалисты')
async def cmd_specialist(message: types.Message):
    data = read_file('specialists.csv')
    
    response = "Список специалистов:\n"
    for row in data:
        name = row.get('Name', 'Unknown')
        phone = row.get('Phone', 'Unknown')
        response += f"Имя: {name}, Телефон: {phone}\n"
    
    await message.answer(response, reply_markup=kb4)
        
@dp.message(lambda message: message.text.lower() == 'адрес')
async def cmd_specialist(message: types.Message):
    data = read_file('contacts_file.csv')
    for row in data:
        print(row)  # Вывод содержимого каждой строки
        city = row.get('city', 'Unknown')
        address = row.get('address', 'Unknown')  # Исправлено на 'address'
        info = f"{city}: {address}"
        await message.answer(info, reply_markup=kb4)
    

    
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Добрый день, {name}. Вы обратились в Центр юридической помощи Москвы и Московской области. Я Ваш персональный ассистент. Чем я могу быть полезен?', reply_markup=kb1)

@dp.message(Command('Меню'))
@dp.message(lambda message: message.text.lower() == 'меню')
async def cmd_menu(message: types.Message):
    await message.answer('Вы вошли меню бота', reply_markup=kb2)

@dp.message(Command('О нас'))
@dp.message(lambda message: re.match(r'.*нас.*', message.text.lower()) and len(message.text) > 2)
async def cmd_info(message: types.Message):
    await message.answer('Центр юридической помощи Москвы и Московской области - партнерство ведущих юристов московского региона. \nНаша история насчитывает 25 лет работы. Узнайте подробности получив нашу презентацию, воспользовавшись меню виртуального ассистента', reply_markup=kb4)

@dp.message(lambda message: re.match(r'.*запис.*', message.text.lower()) and len(message.text) > 4)
async def cmd_record(message: types.Message):
    name = message.chat.first_name
    chat_id = message.chat.id
    await message.answer('Пожалуйста, выберите дату приема:', reply_markup=kb3)
async def update_keyboard(message: types.Message):
    await bot.send_message(message.chat.id, 'Вы записаны', reply_markup=kb2)
    
@dp.message(lambda message: message.text in ['2024-04-11', '2024-04-12','2024-04-13','2024-04-14','2024-04-15','2024-04-16','2024-04-17','2024-04-18','2024-04-19','2024-04-20','2024-04-21','2024-04-22','2024-04-23','2024-04-24','2024-04-25','2024-04-26','2024-04-27','2024-04-28','2024-04-29','2024-04-30','2024-04-31'])
async def handle_chosen_date(message: types.Message):
    name = message.chat.first_name
    chat_id = message.chat.id
    appointment_date = message.text
    user_info = {'Name': name, 'Chat ID': chat_id, 'Appointment Date': appointment_date}
    write_to_csv(user_info)
    await update_keyboard(message)


@dp.message(Command('Контакты'))
@dp.message(lambda message: message.text.lower() == 'контакты')
async def cmd_info(message: types.Message):
    await message.answer('Номер телефона: 7 (985) 477-23-19 \nАдминистратор: @Kiselev_VK\nСлужба поддержки: vkiselev-opec@mail.ru', reply_markup=kb2)
    

   
@dp.message(Command('Цены'))
@dp.message(lambda message: message.text.lower() == 'цены')
async def cmd_info(message: types.Message):
    await message.answer('Подробную информацию о ценах вы можете получить у администратора @Kiselev_VK', reply_markup=kb4)
    
@dp.message(Command('Сайт'))
@dp.message(lambda message: message.text.lower() == 'сайт')
async def cmd_info(message: types.Message):
    await message.answer('https://cupmmo.tilda.ws/', reply_markup=kb4)
    

@dp.message(Command('Промо'))
@dp.message(lambda message: message.text.lower() == 'промо')
async def cmd_info(message: types.Message):
    await message.answer('https://cupmmo.tilda.ws/promo/', reply_markup=kb4)

@dp.message(Command('Презентация'))
@dp.message(lambda message: message.text.lower() == 'презентация')
async def cmd_info(message: types.Message):
    await message.answer('https://cupmmo.tilda.ws/presentation/', reply_markup=kb4) 
    
@dp.message(lambda message: re.match(r'.*режим.*', message.text.lower()) and len(message.text) > 4)
async def cmd_record(message: types.Message):
    await message.answer('Режим работы:\nПонедельник: с 9-00 до 18-00 (без перерыва на обед)\nВторник: с 9-00 до 18-00 (без перерыва на обед)\nСреда: с 9-00 до 18-00 (без перерыва на обед)\nЧетверг: с 9-00 до 18-00 (без перерыва на обед)\nПятница: с 9-00 до 16-45 (без перерыва на обед)\nСуббота: выходной\nВоскресенье: выходной', reply_markup=kb2)
        
async def on_startup(dp):
    await bot.set_my_commands([
        Command("Режим работы", "Получить информацию о режиме работы")
    ])

    
@dp.message(Command('Закрыть'))
@dp.message(lambda message: message.text.lower() == 'закрыть')
async def cmd_close(message: types.Message):
    await message.answer('Вы вернулись в стартовое меню', reply_markup=kb2)   
            


        





async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    raspisanie = ['расписание', 'график работы', 'начинаете', 'заканчиваете', 'перерыв', 'обед']
    if 'цены' in msg_user:
        await message.answer(f'Узнать о наших ценах можно по телефону справочной службы, опубликованному на веб-сайте')
    elif any(item for item in raspisanie if item in msg_user and len(item) >= 3):
        await message.answer(f'Мы работаем с понедельника по пятницц с 9-00 до 18-00 без перерыва на обед')
    elif 'записаться' in msg_user:
        await message.answer(f'Отлично, я запишу вас на прием')
    else:
        await message.answer(f'Я не знаю такого слова')





async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())