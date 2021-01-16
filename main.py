from aiogram import executor, types
from configs import dispatcher, bot, resize_image, BotStates
from buttons import InlineButtons, Buttons
from aiogram.types import Message, CallbackQuery, message
from db import PostgreSQL

btns = Buttons()
ibtns = InlineButtons()


@dispatcher.message_handler(commands=["start"], state='*')
async def welcome(message: Message):
    """Функция которая срабатывает при отправке боту команды /start."""
    welcome_sticker = open('/home/azatot/Desktop/tenor.gif', 'rb')

    await bot.send_animation(
        chat_id=message.from_user.id,
        animation=welcome_sticker
    )

    return await bot.send_message(
        chat_id=message.from_user.id,
        text=f'''
        *Здравствуйте, {message.from_user.first_name}*
        Компания Resto рада видеть Вас в нашем Телеграм боте!
        Вам будут доступны следующие функции:
        ''',
        parse_mode=types.ParseMode.MARKDOWN,
        reply_markup=btns.main_buttons()
    )



@dispatcher.message_handler(content_types=["text"])
async def main_response(message: Message):
    """После того как пользователь нажмёт на одну из кнопок, ему будет предложено соответствующее действие."""
    if message.text == 'Заказать еду на вынос 🍕':
       
        return await bot.send_message(
            chat_id=message.from_user.id,
            text="Здесь будет меню заказа..."
        )

    elif message.text == 'Забронировать столик ⏰':
       
        return await bot.send_message(
            chat_id=message.from_user.id,
            text="Здесь будет забронировать столик..."
        )
    
    elif message.text == 'Перейти в меню 🗒':
       
        return await bot.send_message(
            chat_id=message.from_user.id,
            text="😋😋😋😋😋 Основное Меню 🍴 😋😋😋😋😋",
            reply_markup=ibtns.show_menu_buttons()
        )

    elif message.text == 'Отзывы ✅':
       
        return await bot.send_message(
            chat_id=message.from_user.id,
            text="Выберите опцию:",
            reply_markup=btns.feedback_buttons()
        )



@dispatcher.callback_query_handler()
async def show_menu(callback: CallbackQuery):
    """Функция которая выводит список блюд по категориям.
        Всё зависит от нажатой inline-кнопки."""
    psql = PostgreSQL()

    if callback.data == 'breakfast':
        for breakfast in psql.select(
            (
                'name', 'image_path', 'price', 'meal_type'
            ),
            'meals',
            {"meal_type": 2}
        ):
            image = resize_image(breakfast[1])
            await bot.send_photo(
                chat_id=callback.from_user.id,
                photo=open(image, 'rb'),
                caption=f'_Название:_ *{breakfast[0]}*\n_Цена:_ *{breakfast[2]} сом*',
                parse_mode=types.ParseMode.MARKDOWN,
                reply_markup=ibtns.make_order((breakfast[-1], breakfast[0]))
            )
        else:
            return await bot.send_message(
                chat_id=callback.from_user.id,
                text='Нажмите "Назад" чтобы вернуться в Главное Меню!',
                reply_markup=btns.back_to_menu()
            )

    elif callback.data == 'lunch':
        for lunch in psql.select(
            (
                'name', 'image_path', 'price', 'meal_type'
            ),
            'meals',
            {"meal_type": 3}
        ):
            image = resize_image(lunch[1])
            await bot.send_photo(
                chat_id=callback.from_user.id,
                photo=open(image, 'rb'),
                caption=f'_Название:_ *{lunch[0]}*\n_Цена:_ *{lunch[2]} сом*',
                parse_mode=types.ParseMode.MARKDOWN,
                reply_markup=ibtns.make_order((lunch[-1], lunch[0]))
            )
        else:
            return await bot.send_message(
                chat_id=callback.from_user.id,
                text='Нажмите "Назад" чтобы вернуться в Главное Меню!',
                reply_markup=btns.back_to_menu()
            )

    elif callback.data == 'dinner':
        for dinner in psql.select(
            (
                'name', 'image_path', 'price', 'meal_type'
            ),
            'meals',
            {"meal_type": 4}
        ):
            image = resize_image(dinner[1])
            await bot.send_photo(
                chat_id=callback.from_user.id,
                photo=open(image, 'rb'),
                caption=f'_Название:_ *{dinner[0]}*\n_Цена:_ *{dinner[2]} сом*',
                parse_mode=types.ParseMode.MARKDOWN,
                reply_markup=ibtns.make_order((dinner[-1], dinner[0]))
            )
        else:
            return await bot.send_message(
                chat_id=callback.from_user.id,
                text='Нажмите "Назад" чтобы вернуться в Главное Меню!',
                reply_markup=btns.back_to_menu()
            )


    elif callback.data == 'primary_meal':
        for primary_meal in psql.select(
            (
                'name', 'image_path', 'price', 'meal_type'
            ),
            'meal',
            {"meal_type": 1}
        ):
            image = resize_image(primary_meal[1])
            await bot.send_photo(
                chat_id=callback.from_user.id,
                photo=open(image, 'rb'),
                caption=f'_Название:_ *{primary_meal[0]}*\n_Цена:_ *{primary_meal[2]} сом*',
                parse_mode=types.ParseMode.MARKDOWN,
                reply_markup=ibtns.make_order((primary_meal[-1], primary_meal[0]))
            )
        else:
            return await bot.send_message(
                chat_id=callback.from_user.id,
                text='Нажмите "Назад в меню" чтобы вернуться в Главное Меню!',
                reply_markup=btns.back_to_menu()
            )


if __name__ == '__main__':
    executor.start_polling(dispatcher=dispatcher)

# sudo apt-get install build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev python3.8-dev python3.9-dev