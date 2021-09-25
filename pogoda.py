from pyowm import OWM
from pyowm.utils.config import get_default_config
# from tkinter import *
# root = Tk()
# root.mainloop()

config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here, ru. Russian
owm = OWM('4707c215225f3783a2e45a56dd73e1b2', config_dict)

# ---------- 4707c215225f3783a2e45a56dd73e1b2 ---------------------

mgr = owm.weather_manager()

observation = mgr.weather_at_place(str("minsk"))
w = observation.weather

temp = w.temperature('celsius')["temp"]
wind = w.wind()["speed"]
a = temp
b = wind
c = ((w.wind()["speed"]) * 3.6)

print("\nГОРОД-ГЕРОЙ МИНСК: ")
print("Температура: " + str(round(a)) + "°C")
print("Влажность: " + str(w.humidity) + " %")
print("Скорость ветра: " + str(round(b)) + " м/с" + " = " + str(round(c)) + " км/час")
print("Сейчас " + str(w.detailed_status))

place = input(
    "\n!!! ПРОГРАММА ПОГОДА ОНЛАЙН ПРИВЕТСТВУЕТ ВАС !!!\nНапишите название города или страны и нажимайте ENTER: ")

observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')["temp"]
wind = w.wind()["speed"]
a = temp
b = wind
c = ((w.wind()["speed"]) * 3.6)

print("Температура: " + str(round(a)) + "°C")
print("Влажность: " + str(w.humidity) + " %")
print("Скорость ветра: " + str(round(b)) + " м/с" + " = " + str(round(c)) + " км/час")
print("Сейчас: " + str(w.detailed_status))

if temp < 0:
    print("!!! МОРОЗ !!! ОДЕВАЙ: ШАПКУ УШАНКУ + ФУФАЙКУ + ВАЛЕНКИ !!!")
if 10 > temp > 0:
    print("!!! ПОГОДА ДУБАК, ОДЕВАЙСЯ КАК ТАНК !!!")
if 20 > temp > 10:
    print("!!! ПОГОДА ХОЛОДНАЯ, ОДЕВАЙСЯ ПОТЕПЛЕЕ !!!")
if 27 > temp > 20:
    print("!!! ПОГОДА НОРМАЛЬНАЯ, ОДЕВАЙ ЧТО УГОДНО !!!")
if temp > 27:
    print("!!! ПОГОДА ЖАРКАЯ, ОДЕВАЙ ШОРТЫ + МАЙКУ !!!")
