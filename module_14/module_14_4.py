from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import crud_functions
list_products = crud_functions.get_all_products()

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Купить')]
], resize_keyboard=True)



menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Продукт 1', callback_data='product_buying'),
        InlineKeyboardButton(text='Продукт 2', callback_data='product_buying'),
        InlineKeyboardButton(text='Продукт 3', callback_data='product_buying'),
        InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')]
    ]
)



@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer('Привет! Хотите что-нибудь приобрести.', reply_markup=kb)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    list_photo = ['img.png', 'img_1.png', 'img_2.png', 'img_3.png']
    for i in range(len(list_photo)):
        product = list_products[i]
        await message.answer(f'Название: {product[0]} | Описание: {product[1]}| Цена: {product[2]}')
        with open(f'../photo/{list_photo[i]}', 'rb') as img:
            await message.answer_photo(img)

    await message.answer('Выберите продукт для покупки:', reply_markup=menu)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler()
async def all_massages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
