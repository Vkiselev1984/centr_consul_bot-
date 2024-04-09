from aiogram import types

button1 = types.KeyboardButton(text='Меню')
keybord1 = [
    [button1],
    ]
kb1 = types.ReplyKeyboardMarkup(keyboard=keybord1, resize_keyboard=True)

button2 = types.KeyboardButton(text='О нас')
button3 = types.KeyboardButton(text='Записаться')
button4 = types.KeyboardButton(text='Контакты')
button5 = types.KeyboardButton(text='Режим работы')

keybord2 = [
    [button2, button3],
    [button4, button5],
    ]
kb2 = types.ReplyKeyboardMarkup(keyboard=keybord2, resize_keyboard=True)

button6 = types.KeyboardButton(text='2024-04-11')
button7 = types.KeyboardButton(text='2024-04-12')
button8 = types.KeyboardButton(text='2024-04-13')
button9 = types.KeyboardButton(text='2024-04-14')
button10 = types.KeyboardButton(text='2024-04-15')
button11 = types.KeyboardButton(text='2024-04-16')
button12 = types.KeyboardButton(text='2024-04-17')
button13 = types.KeyboardButton(text='2024-04-18')
button14 = types.KeyboardButton(text='2024-04-19')
button15 = types.KeyboardButton(text='2024-04-20')
button16 = types.KeyboardButton(text='2024-04-21')
button17 = types.KeyboardButton(text='2024-04-22')
button18 = types.KeyboardButton(text='2024-04-23')
button19 = types.KeyboardButton(text='2024-04-24')
button20 = types.KeyboardButton(text='2024-04-25')
button21 = types.KeyboardButton(text='2024-04-26')
button22 = types.KeyboardButton(text='2024-04-27')
button23 = types.KeyboardButton(text='2024-04-28')
button24 = types.KeyboardButton(text='2024-04-29')
button25 = types.KeyboardButton(text='2024-04-30')
button26 = types.KeyboardButton(text='2024-04-31')

keybord3 = [
    [button6, button7, button8],
    [button9, button10, button11],
    [button12, button13, button14],
    [button15, button16, button17],
    [button18, button19, button20],
    [button21, button22, button23],
    [button24, button25, button26],
]
kb3 = types.ReplyKeyboardMarkup(keyboard=keybord3, resize_keyboard=True)

button27 = types.KeyboardButton(text='Цены')
button28 = types.KeyboardButton(text='Специалисты')
button29 = types.KeyboardButton(text='Адрес')
button30 = types.KeyboardButton(text='Промо')
button31 = types.KeyboardButton(text='Презентация')
button32 = types.KeyboardButton(text='Сайт')
button33 = types.KeyboardButton(text='Закрыть')

keybord4 = [

    [button27, button28],
    [button29, button30],
    [button31, button32],  
    [button33], 
]

kb4 = types.ReplyKeyboardMarkup(keyboard=keybord4, resize_keyboard=True)