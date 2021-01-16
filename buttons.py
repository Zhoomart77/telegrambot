from typing import Tuple
from aiogram import types


class Buttons:
    def main_buttons(self):
        markup = types.ReplyKeyboardMarkup(
            one_time_keyboard=True,
            resize_keyboard=True,
            row_width=2
        )

        order_food_to_deliver_btn = types.KeyboardButton(
            text='Заказать еду на вынос 🍕',
        )

        book_table_btn = types.KeyboardButton(
            text='Забронировать столик ⏰',
        )

        show_menu_btn = types.KeyboardButton(
            text='Перейти в меню 🗒',
        )

        set_feedback_btn = types.KeyboardButton(
            text='Отзывы ✅',
        )

        markup.add(
            order_food_to_deliver_btn,
            book_table_btn,
            show_menu_btn,
            set_feedback_btn,
        )

        return markup


    def feedback_buttons(self):
        markup = types.ReplyKeyboardMarkup(
            one_time_keyboard=True,
            resize_keyboard=True,
        )

        send_feedback_btn = types.KeyboardButton(
            text='Оставить отзыв ✍',
        )

        read_feedbacks_btn = types.KeyboardButton(
            text='Прочитать отзывы 👍',
        )


        markup.add(
            send_feedback_btn,
            read_feedbacks_btn,
        )

        return markup


    def back_to_menu(self):
        markup = types.ReplyKeyboardMarkup(
            one_time_keyboard=True,
            resize_keyboard=True,
        )

        back_to_menu_btn = types.KeyboardButton(
            text='Назад в меню',
        )

        markup.add(back_to_menu_btn)

        return markup



class InlineButtons:
    def show_menu_buttons(self):
        markup = types.InlineKeyboardMarkup(
            row_width=2
        )
        
        primary_meal_btn = types.InlineKeyboardButton(
            text='Фирменные блюда',
            callback_data='primary_meal'
        )

        breakfast_btn = types.InlineKeyboardButton(
            text='Завтраки',
            callback_data='breakfast'
        )

        lunch_btn = types.InlineKeyboardButton(
            text='Обеды',
            callback_data='lunch'
        )

        dinner_btn = types.InlineKeyboardButton(
            text='Ужин',
            callback_data='dinner'
        )

        resto_site_btn = types.InlineKeyboardButton(
            text='Перейти на сайт',
            callback_data='resto',
            url='https://freehtml5.co/preview/?item=resto-free-responsive-bootstrap-4-template-for-restaurants'
        )

        markup.add(
            primary_meal_btn,
            breakfast_btn,
            lunch_btn,
            dinner_btn,
            resto_site_btn
        )

        return markup

    
    def make_order(self, definiton: tuple):
        """Функция которая создаёт inline-кнопку Заказать 🔥"""
        markup = types.InlineKeyboardMarkup(
            row_width=2
        )

        order_btn = types.InlineKeyboardButton(
            text='Заказать 🔥',
            callback_data=f'{definiton[0]} {definiton[1]}',
        )

        markup.add(order_btn)

        return markup