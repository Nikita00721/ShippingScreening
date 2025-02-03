import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo, KeyboardButton, ReplyKeyboardMarkup

TOKEN = "7892759186:AAF1j-Gsi4hJY8LxrI9RgTWeumj1YeDQNfk"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    web_app = WebAppInfo(url="https://amvera-nkremnev3003-run-shipping.io")
    button = KeyboardButton(text="Открыть Mini App", web_app=web_app)

    keyboard = ReplyKeyboardMarkup(
        keyboard=[[button]],
        resize_keyboard=True
    )

    await message.answer("Нажмите кнопку, чтобы открыть приложение:", reply_markup=keyboard)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
