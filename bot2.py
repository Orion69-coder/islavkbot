import random, vk_api, vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
vk_session = vk_api.VkApi(token='b6d18486bf812ec70aca7ef25d8d7fc3091a4c950ff2402af8fedd183d9720cd84c08af74d083eca1ead2')
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
longpoll = VkBotLongPoll(vk_session, 200606276)
vk = vk_session.get_api()
from vk_api.longpoll import VkLongPoll, VkEventType
Lslongpoll = VkLongPoll(vk_session)
Lsvk = vk_session.get_api()
from datetime import datetime
import pyowm
import math as m
token = 'da29c406488b2b5965e3e1074985c0ba'
owm = pyowm.OWM(token)
mgr = owm.weather_manager()
obs = mgr.weather_at_place('Тверь')
w = obs.weather
temp = w.temperature('celsius')
tempa = temp['temp']
if tempa>0:
    tempa = m.ceil(tempa)
if tempa<0:
    tempa = m.floor(tempa)
tempa = str(tempa)
WeatherMessage = 'Погода в городе Тверь сейчас ' + tempa + '℃'

keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Айла, какая сегодня погода?', color=VkKeyboardColor.NEGATIVE)
keyboard.add_button('Клавиатура', color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_location_button()
keyboard.add_line()
keyboard.add_vkpay_button(hash="action=transfer-to-group&group_id=200606276")

current_datetime = datetime.now()
hour = current_datetime.hour
minute = current_datetime.minute

print("Айла проснулась")

if (hour >= 4) and (hour < 12):
    print('Доброе утро')
if (hour >=12) and (hour < 18):
    print('Добрый день')
if (hour >= 18) and (hour < 24):
    print('Добрый вечер')
if (hour >= 1) and (hour < 4):
    print('Доброй ночи')


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if (hour >= 4) and (hour < 12):
            if 'Айла, Ку' in str(event) or 'Айла, Привет' in str(event) or 'Айла, Хай' in str(event) or 'Айла, Хелло' in str(event) or 'Айла, Хеллоу' in str(event) or 'Айла, привет' in str(event) or 'Айла, хай' in str(event) or 'Айла, хелло' in str(event) or 'Айла, хеллоу' in str(event)or 'Айла, ку' in str(event) or 'Айла, Ку' in str(event): 
                if event.from_chat:
                    vk.messages.send(
                        key = ('7e3ac258d29d744c98c97a9c2fb640240c6d6d52'),          
                        server = ('https://lp.vk.com/wh200606276'),
                        ts=('190'),
                        random_id = get_random_id(),
                        message = 'Доброе утро',
                        chat_id = event.chat_id
                        )

        if (hour >=12) and (hour < 18):
            if 'Айла, Ку' in str(event) or 'Айла, Привет' in str(event) or 'Айла, Хай' in str(event) or 'Айла, Хелло' in str(event) or 'Айла, Хеллоу' in str(event) or 'Айла, привет' in str(event) or 'Айла, хай' in str(event) or 'Айла, хелло' in str(event) or 'Айла, хеллоу' in str(event)or 'Айла, ку' in str(event) or 'Айла, Ку' in str(event): 
                if event.from_chat:
                     vk.messages.send(
                        key = ('7e3ac258d29d744c98c97a9c2fb640240c6d6d52'),          
                        server = ('https://lp.vk.com/wh200606276'),
                        ts=('190'),
                        random_id = get_random_id(),
                        message = 'Добрый день',
                        chat_id = event.chat_id
                        )

        if (hour >= 18) and (hour < 24):
            if 'Айла, Ку' in str(event) or 'Айла, Привет' in str(event) or 'Айла, Хай' in str(event) or 'Айла, Хелло' in str(event) or 'Айла, Хеллоу' in str(event) or 'Айла, привет' in str(event) or 'Айла, хай' in str(event) or 'Айла, хелло' in str(event) or 'Айла, хеллоу' in str(event)or 'Айла, ку' in str(event) or 'Айла, Ку' in str(event): 
                if event.from_chat:
                    vk.messages.send(
                        key = ('7e3ac258d29d744c98c97a9c2fb640240c6d6d52'),          
                        server = ('https://lp.vk.com/wh200606276'),
                        ts=('190'),
                        random_id = get_random_id(),
                        message = 'Добрый вечер',
                        chat_id = event.chat_id
                        )

        if (hour >= 1) and (hour < 4):
            if 'Айла, Ку' in str(event) or 'Айла, Привет' in str(event) or 'Айла, Хай' in str(event) or 'Айла, Хелло' in str(event) or 'Айла, Хеллоу' in str(event) or 'Айла, привет' in str(event) or 'Айла, хай' in str(event) or 'Айла, хелло' in str(event) or 'Айла, хеллоу' in str(event)or 'Айла, ку' in str(event) or 'Айла, Ку' in str(event): 
                if event.from_chat:
                    vk.messages.send(
                        key = ('7e3ac258d29d744c98c97a9c2fb640240c6d6d52'),          
                        server = ('https://lp.vk.com/wh200606276'),
                        ts=('190'),
                        random_id = get_random_id(),
                        message = 'Доброй ночи',
                        chat_id = event.chat_id
                        )
        if 'Что ты можешь?' in str(event) or r'клавиатура' in str(event) or r'Клавиатура' in str(event) or 'Что ты можешь' in str(event) or 'что ты можешь?' in str(event) or 'что ты можешь' in str(event) or r'функции' in str(event) or r'Функции' in str(event) or r'Айлочка' in str(event) or r'айлочка' in str(event):
            if event.from_chat:
                vk.messages.send(
                    keyboard = keyboard.get_keyboard(),
                    key = ('7e3ac258d29d744c98c97a9c2fb640240c6d6d52'),          
                    server = ('https://lp.vk.com/wh200606276'),
                    ts=('190'),
                    random_id = get_random_id(),
              	    message='Что я могу для тебя сделать?',
             	    chat_id = event.chat_id
            	    )
        if "Айла, какая сегодня погода?" in str(event):
            if event.from_chat:
                vk.messages.send(
                    key = ('7e3ac258d29d744c98c97a9c2fb640240c6d6d52'),          
                    server = ('https://lp.vk.com/wh200606276'),
                    ts=('190'),
                    random_id = get_random_id(),
              	    message = WeatherMessage,
            	    chat_id = event.chat_id
                    )
