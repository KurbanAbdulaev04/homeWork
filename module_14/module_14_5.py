from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import crud_functions
list_products = crud_functions.get_all_products()

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Купить')],
    [KeyboardButton(text='Регистрация')]
], resize_keyboard=True)


menu = InlineKeyboardMarkup(
    inline_keyboard=(
        [InlineKeyboardButton(text='Продукт 1', callback_data='product_buying'),
         InlineKeyboardButton(text='Продукт 2', callback_data='product_buying'),
         InlineKeyboardButton(text='Продукт 3', callback_data='product_buying'),
         InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')
         ],
    )
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


#=================================Регистрация================================

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State('1000')


@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    await state.update_data(username=message.text)
    inp_username = await state.get_data()
    name = crud_functions.is_included(inp_username)
    if name is False:
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()
    else:
        await message.answer('Пользователь существует, введите другое имя')
        await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    crud_functions.add_user(data['username'], data['email'], data['age'])
    await message.answer("Регистрация прошла успешно!")
    await state.finish()


#=================================все сообщения================================
@dp.message_handler()
async def all_massages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)