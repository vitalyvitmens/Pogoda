from pyowm import OWM
from pyowm.utils.config import get_default_config
from pyowm.commons.exceptions import NotFoundError

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('4707c215225f3783a2e45a56dd73e1b2', config_dict)
mgr = owm.weather_manager()

observation = mgr.weather_at_place(str("minsk"))
w = observation.weather
temp = w.temperature('celsius')["temp"]
wind = w.wind()["speed"]
wind_km_h = (w.wind()["speed"]) * 3.6

print(f"\nГОРОД-ГЕРОЙ МИНСК:\nТемпература: {str(round(temp))}°C\nВлажность: {str(w.humidity)}%\n"
      f"Скорость ветра: {str(round(wind))}м/с = {str(round(wind_km_h))}км/час\nСейчас {str(w.detailed_status)}")

place = input(
    "\n!!! ПРОГРАММА ПОГОДА ОНЛАЙН ПРИВЕТСТВУЕТ ВАС !!!\nНапишите название города или страны и нажимайте ENTER: ")
try:
    observation = mgr.weather_at_place(place)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]
    wind = w.wind()["speed"]
    wind_km_h = (w.wind()["speed"]) * 3.6
    print(f"Температура: {str(round(temp))}°C\nВлажность: {str(w.humidity)}%\n"
          f"Скорость ветра: {str(round(wind))}м/с = {str(round(wind_km_h))}км/час\nСейчас: {str(w.detailed_status)}")
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
except NotFoundError:
    print(f'Не найдено место: {place}')
