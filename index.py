from colorama import Fore
from config import *
from time import sleep
from pyrogram import Client, filters, sync
from pyrogram.errors import FloodWait
import os

client = Client('ghoul-session', api_id, api_hash)

client.start()

client.stop()
print('')
print('              УСПЕШНО')
print('        Создатель @criblle')
print('Бот был создан для каналов TT-SOFT и CacheCoding')
print('---------------------КАНАЛЫ---------------------')
print('TT-SOFT   ')
print('https://t.me/+zCLiT3qu-xhmZGNi')
print('')
print('CacheCoding')
print('https://t.me/+6vefVRO4jVMwNjUy')


@client.on_message(filters.regex('Я гуль|я гуль') & filters.me)
def ghoul_spam_handler(client, message):
    i = 1000
    while i > 0:
        try:
            client.send_message(message.chat.id, f'{i} - 7 = {i-7}')
        except FloodWait as e:
            sleep(e.x)

        i -= 7
        sleep(0/messages_per_second)

    if(end_message != ''):
        client.send_message(message.chat.id, end_message)


@client.on_message(filters.command(ghoul_table_command, prefixes=command_prefixes) & filters.me)
def ghoul_table_handler(client, message):
    i = 1000
    while i > 62:
        try:
            text = f'{i} - 7 = {i-7}'
            for j in range(1,10):
                text += f'\n{i-7*j} - 7 = {i-7*(j+1)}'
            message.edit_text(f'`{text}`')
            sleep(sleep_time_ghoul)
        except FloodWait as e:
            sleep(e.x)

        i -= 7

    if(end_message != ''):
        client.send_message(message.chat.id, end_message)
print(Fore.RED + 'Напишите 0 если хотите ВЫЙТИ и 1 чтобы ПРОДОЛЖИТЬ')
inp = int(input('<$> '))
if inp == 0:
    print(Fore.GREEN + 'Выход')
    sleep(1)
    if os.sys.platform == "win32":
         os.system("cls")
    else:
        os.system("clear")
    import Silion.py
client.run()