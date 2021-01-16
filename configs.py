from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from PIL import Image
import os

BOT_TOKEN = os.environ.get('BOT_TOKEN')


bot = Bot(BOT_TOKEN)
memory = MemoryStorage()
dispatcher = Dispatcher(bot=bot, storage=memory)



def resize_image(img_path):
    """Функция изменяет размер любой картинки на тот размер который Вы указали #image.resize(width, height)# """
    image = Image.open(img_path)
    new_image = image.resize((480, 512))
    new_image.save(img_path)
    return img_path