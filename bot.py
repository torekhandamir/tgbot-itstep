import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
)
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from api import TOKEN

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет!"), KeyboardButton(text="Помощь")]
    ],
    resize_keyboard=True
)

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="начать", callback_data="start")],
        [InlineKeyboardButton(text="помощь", callback_data="help")],
        [InlineKeyboardButton(text="рандомное число", callback_data="random")]
    ]
)

@dp.callback_query()
async def callback_handler(callback:  types.CallbackQuery):
    if callback.data == "start":
        await callback.message.answer("напиши /start ,что бы начать работу с ботом")
    elif callback.data == "help":
        await callback.message.answer("фльтернативная помощь или напиши /help")
    elif callback.data == "random":
        await callback.message.answer("хочешь рандормное число?напиши /random")

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я тестовый бот <b>test</b>", reply_markup=main_keyboard)

@dp.message(Command("random"))    
async def random_command(message: types.Message):
    number = random.randint(1,1000)
    await message.answer(f"Случайное число: {number}")

@dp.message(Command("help"))
async def help_command(message: types.Message):
    command_text = (
        "Доступные команды:\n"
        "/start - Начать работу с ботом\n"
        "/help -  показывает список команд\n"
        "/random - случайное число"
    )
    await message.answer(command_text)
@dp.message(lambda message: message.text == "Привет!")
async def hello(message: types.Message):
    await message.answer("Привет!!! Как дела?", reply_markup=inline_keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())